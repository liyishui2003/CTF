# CTF-01：Session 不过期 + Cookie 劫持

> 第一道题。纪念一下。
> 关联：[[README.md]] | 下一题 → [[CTF-02_DeveloperHeader绕过登录.md]]

---

## 题目

登录网站，发现 session 永不过期。找到管理员的 session，替换成自己的，拿到 flag。

---

## 解题过程

### Step 1：发现异常

登录后 `F12` → **Application** → **Cookies**，看到 session 的过期时间：

```
session=n0ExlJxbYH5zXabqjxXczsAt_haG1obNbPpUU96FkrQ
Expires=Wed, 06 Feb 2058 07:09:50 GMT
```

2058 年。2026 年的题，session 设到了 2058 年。等于不过期。

### Step 2：找到入口

页面上有一行文字：

```
find strange page at /session
```

`page` 是页面的意思。在 URL 后面拼上 `/session`，跳转到一个新页面。

页面上直接展示了两个 session：
- `user_xxx` — 我自己的
- `admin_xxx` — 管理员的

网站把所有登录态的 session 都打印出来了。

### Step 3：替换 Cookie

复制管理员的 session。回到 `F12` → **Application** → **Cookies**：

1. 双击 `session` 这一行的 Value 列
2. 粘贴
3. 按 Enter
4. 刷新页面

页面变成了管理员视角。flag 就在那里。

---

## 知识点

### Session 过期

| | 正确的做法 | 这道题 |
|---|---|---|
| 过期时间 | 几小时到几天 | 30 年后 |
| 泄露后 | 只能用一小段时间 | 能用一辈子 |
| HttpOnly | 应开启 | 已开启 ✅ |

### 两个漏洞

| 漏洞 | 类型 |
|---|---|
| Session 永不过期 | 配置缺陷 |
| `/session` 打印所有 session | 信息泄露 |

### Cookie 劫持

拿到别人的 session Cookie：

```
Application 面板改值 → 刷新 → 变成那个人
```

不需要密码。不需要验证。这就是为什么 session 要保护好。

### 防御

- Session 设置合理过期时间
- 不对外暴露 session 列表
- 关键操作要求二次验证