# CTF-11 Scavenger Hunt 寻宝游戏

## 题目信息
- **平台**：PicoCTF
- **题目**：Scavenger Hunt
- **类型**：Web / 信息收集

## 题目描述
flag 被拆成多个碎片，藏在网站的各个角落。你需要像寻宝一样到处翻找。

## 解题过程

### Part 1 — HTML 注释
查看页面源码，找到 HTML 注释：
```html
<!-- Here's the first part of the flag: picoCTF{t -->
```

### Part 2 — CSS 文件
引用了一个外部 CSS 文件（通常是 `mycss.css` 或类似的），在最底部：
```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

### Part 3 — robots.txt
JS 文件里有提示：
```js
/* How can I keep Google from indexing my website? */
```
→ 答案是 `robots.txt`。访问 `/robots.txt`：
```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

"Access" 大写 A 是提示 → `.htaccess`

### Part 4 — .htaccess
访问 `/.htaccess`：
```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

"Store" 大写 S 是提示 → `.DS_Store`（macOS 目录 metadata 文件）

### Part 5 — .DS_Store
访问 `/.DS_Store`：
```
Congrats! You've completed the scavenger hunt! Part 5: _9588550}
```

### 拼接 Flag
```
picoCTF{t + h4ts_4_l0 + t_0f_pl4c + 3s_2_lO0k + _9588550}
= picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}
```

## 知识点

### 常见的"藏东西"的文件路径

| 文件 | 作用 | 路径 |
|------|------|------|
| `robots.txt` | 告诉搜索引擎爬虫哪些页面不能爬 | `/robots.txt` |
| `.htaccess` | Apache 的目录级配置文件 | `/.htaccess` |
| `.DS_Store` | macOS 的目录图标/位置元数据 | `/.DS_Store` |
| `sitemap.xml` | 网站地图，列出所有页面 | `/sitemap.xml` |

### 启示
- 注释里也可能藏敏感信息！不要以为注释不会被看到
- 外部资源文件（CSS、JS）也是藏东西的好地方
- 出题人经常在文件名/注释里用 **大写字母做双关提示**（Access → .htaccess, Store → .DS_Store）
- 不要只关注主要页面，**"没人看"的文件往往最有价值**

## 参考
- PicoCTF Scavenger Hunt
- [robots.txt 协议](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
