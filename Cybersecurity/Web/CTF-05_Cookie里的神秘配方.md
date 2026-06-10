# CTF-05：Cookie 里的神秘配方

> 第五道题。Base64 藏在 cookie 里。
> 关联：上一题 ← [[CTF-04_HeapDump泄露与内存取证.md]] | 回到 [[README.md]] | 下一题 → [[CTF-06_多页面导航与HTML属性隐藏.md]]

---

## 题目

一个登录页。输完账号密码，页面提示你去看看 cookie。

F12 → Application → Cookies 一看，有个叫 `secret_recipe` 的东西：

```
secret_recipe=cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ%3D%3D
```

## 解题过程

### 1. URL 解码

`%3D` 是 `=` 的 URL 编码。解掉：

```
cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ==
```

末尾两个 `=`，Base64 的特征。

### 2. Base64 解码

```
echo "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ==" | base64 -d

picoCTF{c00k1e_m0nster_l0ves_c00kies_2C8040EF}
```

或者在浏览器 Console：

```javascript
atob("cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ==")
```

---

## 原理

### Cookie 是什么

服务器存在浏览器里的小数据块。每次请求浏览器会自动带上。

登录后服务器通过 `Set-Cookie` 响应头写进去，之后你每次访问都带着它，服务器就知道"你是谁"。

### Base64 是什么

一种把二进制数据转成文本的编码方式。特征：只含 `A-Za-z0-9+/=`。

**不是加密**，**只是编码**。任何人都能解。把 flag 用 Base64 编码放 cookie 里，相当于把密码写在便利贴上贴脑门上。

### 为什么这题不叫"破解"

因为这题**不是让你绕过什么**，是让你学会：
1. cookie 在哪看
2. Base64 怎么解
3. 敏感信息不该放 cookie

---

## 防御

| 做法 | 说明 |
|------|------|
| 敏感信息不放 cookie | 即使用 Base64 编码也不行，等于明文 |
| cookie 只存 session ID | 真正的数据放服务端 |
| HttpOnly 标记 | JS 读不到 cookie，减少 XSS 泄露风险 |
| Secure + SameSite | 限制 cookie 的作用域和发送场景 |

---

## 延伸：PHP 是什么

这题的 cookie 很可能是 PHP 的 `setcookie()` 发的。如果响应头里有 `X-Powered-By: PHP`，就能确认。

### 和后端其他语言的关系

```
PHP：     专门为网页而生的老牌后端语言。WordPress、Facebook 早期都用它
Node.js： 用 JS 写后端，相对新
Java：    企业级重型框架
```

PHP 的特点是"来一个请求起一个进程，处理完就退出"。不像 Node.js 那样一直跑在内存里。

### 怎么认出 PHP

```
响应头：X-Powered-By: PHP/8.0.1
URL：   /login.php  /api.php
```

### 代码长什么样

```php
<?php
  $flag = "picoCTF{...}";
  setcookie("secret_recipe", base64_encode($flag));
  // setcookie 会把值写到浏览器的 cookie 里
?>
```

PHP 代码嵌在 HTML 里写，简单直接。新项目用 PHP 的少了，但存量巨大，CTF 里经常遇到。

### 这题里 PHP 做了什么

```
你的浏览器                     PHP 服务器
  ── 登录请求 ──→              检查账号密码
  ←─ Set-Cookie: secret_recipe  生成 Base64 编码的 flag
  ←─ "去看看 cookie"            告诉你去看
你打开 Application 面板
  看到 cookie
  解 Base64 → flag
```

---

| 关联到 | 原因 |
|--------|------|
| [[CTF-01_Session不过期与Cookie劫持.md]] | 第一题也是 cookie，不过是改了别人的 session |
| [[cleanCode-规范]] | 防御性编程：敏感信息不该出现在意外的地方 |
