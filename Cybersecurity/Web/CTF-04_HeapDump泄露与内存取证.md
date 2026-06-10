# CTF-04：HeapDump 泄露与内存取证

> 第四道题。服务器把堆快照暴露出来了。
> 关联：上一题 ← [[CTF-03_SSTI与Jinja2模板注入.md]] | 下一题 → [[CTF-05_Cookie里的神秘配方.md]]

---

## 题目

一个博客网站。响应头暴露了 `X-Powered-By: Express`，是 Node.js。

首页没什么特别的，但 `/api-docs` 有 Swagger API 文档。翻了一下，发现一个接口：

```
GET /heapdump
Description: Diagnosing the memory allocation.
```

没有鉴权，直接点 Execute 就会下载一个堆快照文件。flag 就在里面。

---

## 解题过程

### 1. 发现技术栈

拿到响应头：

```
HTTP/1.1 200 OK
X-Powered-By: Express
ETag: W/"acd455-19e7e04134a"
```

Express.js，Node 系框架。`W/` 开头的 ETag 是弱校验（weak validator）—— 服务器只保证语义等价，不保证字节级一致。静态文件默认会带 ETag，这里没什么问题，但暴露了文件 hash，可以作为信息补充。

### 2. 翻 API 文档

访问 `/api-docs`，Swagger UI 列出了所有接口，包括一个 `/heapdump`。

描述写的是 "Diagnosing the memory allocation."——直白到不能再直白，就是让你诊断内存用的。

没有鉴权、没有 token、没有 IP 白名单，直接 Execute 就能下载。

### 3. 下载 heapdump

```
GET /heapdump → 200 OK
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="heapdump-1780230655952.heapsnapshot"
Content-Length: 11326549
```

大约 11MB 的 V8 堆快照文件。

### 4. 提取 flag

直接 grep，搜 `pico`（因为知道题目是 picoCTF 的，flag 格式是 `picoCTF{...}`）：

```bash
grep -a "pico" heapdump-1780230655952.heapsnapshot
```

也可以用 Chrome DevTools：
- F12 → Memory 面板 → Load → 选择快照文件
- Ctrl+F 搜 `pico`

```
flag: picoCTF{Pat!3nt_15_Th3_K3y_8df117c1}
```

---

## 原理

### HeapDump 是什么

V8 引擎的堆快照，记录某个时刻所有 JavaScript 对象在内存中的状态。包含：
- 所有变量值（字符串、对象、闭包）
- 调用栈
- 函数定义

Express 应用运行中，所有加载到内存的变量都在里面——包括 flag。

### 为什么会泄露

Node.js 有个常用的调试/诊断包叫 `heapdump`，可以主动生成快照用于排查内存泄漏。开发时很有用，但线上暴露出去就是事故。

正常的做法：
- **绑定到内网/localhost**，不对外暴露
- **加鉴权**，比如 header 校验或 token
- **只在 debug 模式下开启**

这题的反面就是：没做任何保护，裸奔。

---

## 延伸：Node.js 是什么

这题出现了 `X-Powered-By: Express` 和 heapdump。要理解这题，得先搞清楚 Node.js 在整个 Web 里扮演什么角色。

### 浏览器里的 JS vs Node.js

```
浏览器（前端 JS）：      操作 DOM、改页面样式、发请求
Node.js（后端 JS）：    读数据库、写文件、处理 HTTP 请求、管理内存
```

语言一样（都是 JavaScript），舞台不同。Node.js = **在服务器上跑 JavaScript 的运行时**。

### Node.js 在后端的定位

Node.js 是业界主流后端技术之一。Netflix（SSR 层）、LinkedIn（API 网关）、Uber（核心行程匹配）、阿里/腾讯（BFF 层）都在用。

和后端 Java 生态的常见分工：

```
Java（Spring）—— 核心业务层
    订单、支付、账户、风控，需要强类型、高稳定性

Node.js（Express）—— 边界和胶水层
    SSR / BFF / API 聚合 / 实时通信 / CLI 工具
```

### 常见实践场景

| 场景 | 说明 |
|------|------|
| **BFF** | 前端和 Java 微服务之间的聚合层，拼数据格式 |
| **API 网关** | 请求路由、限流、鉴权（类似你实习用的 Shepherd + Ocean）|
| **SSR** | 服务端渲染页面，Netflix、Airbnb 在用 |
| **实时通信** | WebSocket、SSE（你毕设里写过 SSE）|
| **CLI 工具** | Webpack、Copilot CLI、VS Code 扩展——都是 Node.js |
| **轻量 CRUD** | 快速搭 API，像这题的 Express 博客，十几行代码起一个服务 |

### 为什么会有 heapdump

Node.js 服务跑久了可能**内存泄漏**。开发者需要看内存里有什么，于是 Node.js 提供了 heapdump 机制——给内存拍一张快照，分析哪些对象没被释放。

正常链路：

```
发现内存泄漏 → 打 heapdump → 分析对象分布 → 修代码 → 部署
```

CTF 里的问题：这个 debug 接口没关，还暴露在 Swagger 文档里，等于把钥匙插门上还贴了张纸条。

### 理解了这些再看这题

```
你访问 Swagger 页面（/api-docs）
     ↓ 看到了 /heapdump 接口
     ↓ 点 Execute
Node.js 服务器收到请求
     ↓ 拍了内存快照（heapdump）
     ↓ 返回了 11MB 的文件，里面存着 flag
你搜到 flag
```

没有 `X-Powered-By: Express`，你不会知道这是 Node.js。
不知道 Node.js 是什么，就不明白 heapdump 是什么文件。
不知道 heapdump 存了什么，就不会想到搜 `picoCTF`。

每一条信息都是链条上的一环。

---

## 防御

| 做法 | 说明 |
|------|------|
| 不暴露诊断接口 | `/heapdump`、`/debug` 等路径不该出现在线上 |
| Nginx 层拦截 | 特定路径只允许内网 IP |
| 禁用 `X-Powered-By` | `app.disable('x-powered-by')`，减少信息泄露 |
| 生产环境最小权限 | debug 工具只在开发/预发环境可用 |

---

## 与本仓库的关联

| 关联到 | 原因 |
|--------|------|
| [[软件运维]] | 排查第一招"先定界"——看到 X-Powered-By 就知道是 Express 的活 |
| [[cleanCode-规范]] | 防御性编程：不该暴露的东西别暴露 |
| [[技术栈全景]] | Node.js BFF 和你实习用的 Java 微服务 + 中间件，本质是同一套架构思路——服务拆分、API 网关、配置管理 |
| [[../../AI/毕设原理速通.md]] | 毕设的 Express + FastAPI 架构 = Node.js BFF + Python AI 服务，这题里的 Express 就是 Node.js 后端 |
