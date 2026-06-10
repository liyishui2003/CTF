# CTF-07: IntroToBurp —— OTP 绕过

> 第七道题。OTP 参数校验缺失，空 body 直接绕过。
> 关联：上一题 ← [[CTF-06_多页面导航与HTML属性隐藏.md]] | 回到 [[README.md]]

## 题目信息

- **题目**：IntroToBurp（picoCTF）
- **核心考点**：OTP 双因素认证绕过、请求篡改、参数校验缺失
- **工具**：Burp Suite / curl / Chrome DevTools Network

---

## 解题过程

### 1. 观察

页面是一个注册表单（`register.html`），填写信息提交后跳转到 `/dashboard` 页面，要求输入 **OTP（一次性密码）**。

```html
<input id="csrf_token" name="csrf_token" type="hidden" 
       value="IjE4Y2RiZGI5ODRlZmY0ZjJmNDg1NTJkNzMzMTRhZGQyNTczNDQwMzci...">
```

注册后会得到一个 Flask session cookie。

### 2. 尝试

- 随便填 OTP（如 `111`）→ 失败
- 搜索源代码 → 无 flag
- 检查 cookie → Flask session 格式，解码失败（zlib 压缩，无密钥无法解）
- SSTI 尝试 → 不像

### 3. 绕过

提示 "IntroToBurp" —— 使用 Burp Suite 拦截请求并修改。

核心思路：**OTP 参数校验可能只是检查了参数值是否正确，但忘了检查参数是否存在。**

将 OTP 请求的 `--data-raw "otp=111"` 改为空 `--data-raw ""`：

```bash
curl "http://titan.picoctf.net:XXXXX/dashboard" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -b "session=..." \
  --data-raw ""   # ← 去掉 otp 参数
```

返回：

```
Welcome, 111 you sucessfully bypassed the OTP request.
Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a}
```

---

## 延伸知识

### 一、Burp Suite 是什么

Burp Suite（通常简称 Burp）是 Web 安全测试中最常用的**抓包改包工具**。

| 功能 | 用途 |
|------|------|
| Proxy | 拦截浏览器与服务器之间的 HTTP/HTTPS 请求 |
| Repeater | 手动修改并重放请求 |
| Intruder | 自动化爆破（密码、参数等） |
| Decoder | 编解码（Base64、URL、Hex 等） |

**替代方案**（不装 Burp 也能做）：

1. **Chrome DevTools → Network** — 右键请求 → Copy as cURL → 改完用终端执行
2. **Edit and Resend**（Chrome 新版）— Network 面板右键即可
3. **`curl` 命令** — 直接手动构造请求

### 二、OTP 绕过常见方式

| 方式 | 操作 | 原理 |
|------|------|------|
| **空参数** | 删除 `otp=` 字段 | 服务端未校验参数存在性 |
| **空值** | `otp=` 或 `otp=0` | 默认值被当作有效 |
| **类型混淆** | `otp[]=` 或 `otp=true` | 弱类型比较导致绕过 |
| **负数** | `otp=-1` | 边界检查缺失 |
| **万能 OTP** | `000000`, `123456` | 测试环境遗留 |
| **直接访问** | 跳过 OTP 页面到目标 URL | OTP 检查仅在客户端 |

本题属于第一种：**服务端只检查了「otp 的值是否等于 X」，但没检查「otp 参数是否存在」**。当参数缺失时，条件判断直接跳过。

伪代码对比：

```python
# 有漏洞的写法
if request.form.get('otp') == expected_otp:
    grant_access()

# 实际上空 body 时 request.form.get('otp') 返回 None
# None == expected_otp → False，但还是进了 grant_access()
# 因为登录状态下直接访问 /dashboard 本就不该检查 OTP
```

更可能的情况是：

```python
@app.route('/dashboard', methods=['POST'])
def dashboard():
    otp = request.form.get('otp')
    if otp:  # 如果 otp 有值则校验，没值就直接过
        if otp != session['otp']:
            return "Invalid OTP"
    # 返回 flag
    return f"Welcome! Your Flag: {flag}"
```

看到没？`if otp:` 在 Python 中，空字符串、`None` 都被视为 `False`，所以**不传 otp 参数直接绕过校验**。
---

## 关联知识点

- [[CTF-05_Cookie里的神秘配方]] — Base64 编码 / Cookie 分析
- [[CTF-04_HeapDump泄露与内存取证]] — 端点发现
- [[cleanCode-规范]] — 输入校验的重要性
- [[../README]]
