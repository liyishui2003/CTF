# CTF-12：GET aHEAD — HTTP 三种请求方法

> 第十二道题。题眼藏在标题的双关里：GET aHEAD → HEAD 方法。
> 关联：上一题 ← [[CTF-11_ScavengerHunt_寻宝游戏.md]] | [[README.md]]

---

## 题目

页面有两个按钮：
- **Red** — `method="GET"`
- **Blue** — `method="POST"`

点哪个都只切换标题和背景色，没有 flag。

---

## 解题过程

### Step 1：读题

标题 `GET aHEAD` 是双关：
- "aHEAD" 与 "a head" 同音
- **HEAD** 是 HTTP 的一个请求方法

既然 Red 和 Blue 分别对应 GET 和 POST，那还缺一种方法没试——**HEAD**。

### Step 2：发 HEAD 请求

HEAD 与 GET 类似，但**只返回响应头，不返回响应体**。

浏览器 Console（F12）执行：

```js
fetch("http://wily-courier.picoctf.net:62758/index.php", {method: "HEAD"})
  .then(r => {
    for(let [k, v] of r.headers) console.log(k + ": " + v);
  })
```

### Step 3：拿到 flag

输出中有一行：

```
flag: picoCTF{...}
```

---

## 知识点

### 三种 HTTP 请求方法

| 方法 | 参数位置 | 返回 body | 用途 |
|------|---------|----------|------|
| GET | URL 中 | ✅ | 获取资源 |
| POST | 请求体 | ✅ | 提交数据 |
| HEAD | URL 中 | ❌ | 仅获取响应头 |

### 服务端逻辑

```php
if ($_SERVER['REQUEST_METHOD'] == 'HEAD') {
    header("flag: picoCTF{...}");
}
```

出题人只在 HEAD 分支下写了 flag 头，GET 和 POST 都没有。

### 为什么 Network 看不到？

浏览器点击 Red/Blue 发的是 GET/POST。**flag 只出现在 HEAD 请求的响应头里**。发什么请求取决于你，不是服务端决定"给不给头"。

---

## 关联

| 关联到 | 原因 |
|--------|------|
| [[CTF-02_DeveloperHeader绕过登录]] | 自定义 Header / 方法也是 HTTP 层面的绕过 |
| [[../../CompetitiveProgramming/Codeforces/README.md]] | ACM 思维：枚举所有可能（GET、POST 都试了，还剩 HEAD 呢） |
