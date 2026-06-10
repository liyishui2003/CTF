# CTF-09：Flag 藏在 JS 文件里

> PicoCTF — Includes.
> "This code is in a separate file!" —— 确实在另一个文件里。
> 关联：[[CTF-08_文件上传+Webshell+sudo提权.md]]

---

## 题目

一个介绍 include 指令的静态页面。标题 "On Includes"。

点击按钮弹出：`This code is in a separate file!`

## 解题过程

### Step 1：查看页面源码

```html
<script src="script.js"></script>
```

页面引用了外部 JS 文件。

### Step 2：直接访问 script.js

```
http://target/script.js
```

内容：

```javascript
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_6edef411}
```

拿到后半段 flag：`f7w_2of2_6edef411}`

### Step 3：找前半段

检查 `style.css` 或页面 HTML 注释，发现：

```
picoCTF{1nclu51v17y_1of2_
```

### Step 4：拼接

```
picoCTF{1nclu51v17y_1of2_f7w_2of2_6edef411}
```

---

## 知识点

| 概念 | 说明 |
|------|------|
| 静态文件可访问 | `<script src="...">` 引用的 JS 文件所有人都能直接访问 |
| flag 分段 | 出题人把 flag 拆成两段，分别藏在不同的静态资源里 |
| 查看页面源码 | HTML 注释、CSS、JS 都可能藏信息 |

## 反思

- JS/CSS 文件在浏览器里可以直接通过 URL 访问，不需要任何权限
- "This code is in a separate file!" 本身是提示——去那个文件看看
- 静态文件审查是信息收集的第一步，应该最先做

---

## 延展知识：前端代码保护与泄露

### Source Map（.map 文件）

压缩/混淆后的 JS 无法直接调试。`.map` 文件是一本"字典"，记录压缩后的代码与原始源码的对应关系：

| 压缩后 | .map 文件 | 原始源码 |
|--------|-----------|----------|
| `function a(b){...}` | → (行:列, 名映射) | `function sayHello(name){...}` |

浏览器 DevTools 检测到 `.map` 文件后自动加载，展示原始源码。问题是很多人**把 `.map` 文件部署到了生产环境**。

**Claude 泄露事件：** 攻击者访问 `https://claude.ai/assets/xxx.js.map`，还原了前端完整逻辑，包括 API 地址、prompt 模板、客户端校验规则。

**防御：** 构建工具（Webpack/Vite）默认生成 `.map`，但生产部署时必须排除。可配置 `sourceMap: false` 或只在构建阶段保留。

### 没有 .map 怎么办

JS 仍然可以被逆向，只是难度不同：

| 混淆程度 | 特征 | 逆向难度 |
|----------|------|----------|
| Minify 压缩 | 变量缩短、去空格 | 低 — 逻辑结构不变，可读性差但能读 |
| 重度混淆 | 字符串加密、死代码插入 | 中 — 需要工具辅助 |
| 控制流平坦化 | switch-case + 状态变量 | 高 — 需要专用工具 + 人工分析 |

### 控制流平坦化（Control Flow Flattening）

把正常的 if-else / for / while 结构拍平成一个 **while + switch + 状态变量** 的统一结构：

```js
// 原始
if (user.role === 'admin') { showPanel(); }
else { denyAccess(); }

// 平坦化后
var state = 2;
while (true) {
    switch (state) {
        case 2: state = (user.role === 'admin') ? 3 : 4; break;
        case 3: showPanel(); state = 5; break;
        case 4: denyAccess(); state = 5; break;
        case 5: return;
    }
}
```

逻辑等价，但人眼失去了"这段还是那段"的层次感。

### de4js 等逆向工具

原理：识别 switch-case 平坦化模式 → 追踪状态变量的流转路径 → 还原成 if-else / 函数调用。

但只能解到中间状态，重度混淆 + 多层变形需要人工补充。

### 结论

只要浏览器需要执行 JS，就一定能拿到完整可执行的源代码。**混淆只能增加阅读成本，不能阻止阅读。** 敏感逻辑永远应该放在服务端 API 里，不在前端做任何秘密校验。
