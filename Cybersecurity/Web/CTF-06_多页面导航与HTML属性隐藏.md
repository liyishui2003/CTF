# CTF-06: 多页面导航与 HTML 属性隐藏

> 第六道题。flag 藏在 about.html 的自定义属性里。
> 关联：上一题 ← [[CTF-05_Cookie里的神秘配方]] | 回到 [[README.md]] | 下一题 → [[CTF-07_IntroToBurp_OTP绕过.md]]

## 题目信息

- **题目**：multipage-html（picoCTF）
- **核心考点**：多页面网站导航、HTML 标签自定义属性、Base64 隐藏
- **工具**：浏览器 DevTools、Base64 解码

---

## 解题过程

### 1. 页面观察

打开页面，首页显示：

```
Ha!!!!!! You looking for a flag?
Keep Navigating

Haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Keepppppppppppppp Searchinggggggggggggggggggg
```

提示 "Keep Navigating" —— 一语双关：
- "继续浏览" —— 别只看这一页
- "去看导航栏" —— 导航栏里有其他页面链接

### 2. 图片分析（误入歧途）

页面包含两张图片：
- `img/binding_dark.gif` — 黑色 GIF，约 20KB，实际显黑
- `img/multipage-html-img1.jpg` — 普通 JPG，约 33KB

检查结果：
- **GIF**：180×180，16 色调色板，全是深灰色（RGB 9~34 之间），肉眼全黑
- **JPG**：作者 Shihab Ul Haque，`FFD9` 正常结尾，无附加数据
- 两张图都无明文 flag，也无附加数据

实际上这是**误导**——题目不需要真正的图片隐写分析。

### 3. HTML 源码分析

查看页面源代码：

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

三个页面。首页 `index.html` 没有 flag，于是访问 `about.html`。

### 4. 找到 Flag

在 `about.html` 中发现一个自定义属性：

```html
<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9">
```

`notify_true` 不是标准 HTML 属性，值是 Base64 编码。解码：

```bash
echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9" | base64 -d
# 或 PowerShell:
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("..."))
```

得到 flag：

```
picoCTF{web_succ3ssfully_d3c0ded_df0da727}
```

---

## 延伸知识

### 一、"Keep Navigating" 的一语双关

英文中 **navigate** 有两个含义：

| 含义 | 对应操作 |
|------|---------|
| 浏览/导航（动词） | "继续浏览其他页面" |
| 导航栏（名词 → nav） | "去看看导航栏" |

CTF 出题人经常利用这种语义双关作为提示。类似的还有：

- `Try inspecting the page!!` → 查看页面源代码 / 检查元素
- `Look around` → 查找所有路由/端点
- `robots.txt` → 看爬虫规则文件

### 二、HTML 自定义属性（Custom Attributes）

标准的 HTML 自定义属性应该以 `data-` 前缀：

```html
<div data-user-id="12345" data-role="admin">
```

但在实际题目中，出题人可以随意写任何属性名（如 `notify_true`），浏览器不会报错。**这给了出题人隐藏数据的空间。**

如何发现自定义属性中的数据：
1. **查看源代码**（Ctrl+U / Cmd+U）
2. **右键 → 检查元素**（DevTools Elements 面板）
3. **搜索** `=` 号或可疑的 Base64 特征（字母数字结尾的 `=` 或 `==`）

### 三、为什么这题不是真隐写

我花了一些时间分析 GIF 和 JPG 的二进制结构：

- **GIF**：提取了色板（16 种深灰）、LSB（最低有效位）、像素分布
- **JPG**：检查了 COM 注释、APP 标记、末尾附加数据

结果都是空。原因是题目根本**不需要**图片分析 —— 图片只是页面的装饰元素。

**CTF 解题方法论：先找最容易的突破口。**

| 优先级 | 检查项 | 本题结果 |
|--------|--------|---------|
| 1 | 页面源代码 | ✅ 这里有 flag |
| 2 | HTML 注释 | ❌ 无 |
| 3 | JS/CSS 文件 | ❌ 无关 |
| 4 | 多页面/多路由 | ✅ about.html 有发现 |
| 5 | Cookie/Header | ❌ 无关 |
| 6 | 图片/文件隐写 | ❌ 误导 |

优先检查"不需要任何工具"的东西——**页面源码和网络请求**。

### 四、图片隐写入门（拓展阅读）

虽然本题不需要，但顺便了解常见的图片隐写手段：

#### 4.1 LSB（最低有效位）

每个像素的颜色值（RGB 各 1 字节）的**最低位**可以被替换为信息位。

```
原始像素: R=0b10101101, G=0b01111000, B=0b11001010
修改最低位后: R=0b10101100, G=0b01111001, B=0b11001010
                                 ^         ^         ^
                        隐藏了 0 (0b000)
```

人眼无法察觉 ±1 的颜色变化，但一长串像素的 LSB 可以拼出完整数据。

**工具**：`zsteg`（PNG/BMP）、`StegSolve`（GUI 轮番查看每层位图）

#### 4.2 GIF 的索引色隐写

GIF 使用调色板（Palette），每个像素存的是**颜色索引**而不是 RGB 值。

如果调色板的相邻颜色在视觉上非常接近（如这里的 RGB(31,31,31) 和 RGB(15,15,15)），那么像素索引的 LSB 也可以藏数据——替换后肉眼看不出来。

**本题的 GIF 分析**：
- 16 色调色板，全是深灰（RGB 9~34）
- 180×180 = 32400 像素
- 所有 16 个索引都有使用
- 肉眼看起来全黑，但像素实际分布不均匀（不是纯色）

尝试了 LSB 提取但未发现 flag，因为数据不在 GIF 里。

#### 4.3 JPG 的隐写方式

| 方式 | 原理 | 工具 |
|------|------|------|
| EXIF 元数据 | 藏在相机信息/作者/描述字段 | `exiftool` |
| 末尾附加数据 | JPG 以 FFD9 结尾，之后追加内容 | `strings`, `binwalk` |
| DCT 系数隐写（JSteg） | 修改 DCT 变换后的最低位 | `stegdetect`, `outguess` |

#### 4.4 识别图片是否藏了东西

```bash
# 1. 查看文件末尾是否有附加数据
tail -c 100 image.jpg | xxd

# 2. 检查元数据
exiftool image.jpg

# 3. 查找可打印字符串
strings image.jpg | grep -i "pico\|flag\|CTF"

# 4. 文件类型是否匹配
file image.jpg     # 应该返回正确的 MIME 类型

# 5. 比较文件大小——纯色图不应该有几十 KB
```

---
