# 第07课：入门程序编写与注释

> 基于 [原笔记](note.md) 整理，配套代码：[01.快速入门.py](01.快速入门.py)。标注为「补充」的示例与现有脚本分开说明。

## 1. 本课目标

- 将程序保存在 `.py` 文件中，并能运行。
- 使用 `#` 添加注释。
- 知道快捷键是编辑器操作，理解分行与分号的基本用法。

## 2. 核心知识

### 2.1 项目与 Python 文件

项目文件夹用于组织代码、笔记和图片。**本次已经有学习仓库，因此继续在现有课程目录里写练习，无需重复创建 PyCharm 项目。**

`01.快速入门.py` 中的 `.py` 是 Python 源文件扩展名；前面的 `01.快速入门` 是你给文件取的名称。

### 2.2 注释怎么写

Python 中，**字符串之外的 `#` 开始一段注释，直到该行结束**。注释不会作为普通语句执行，可说明需求和代码用途。

```python
# 需求：在控制台输出一句问候语
print("Hello World,Hello Python")
```

输出：

```text
Hello World,Hello Python
```

| 写法 | 含义 |
| --- | --- |
| `# 需求：……` | 给阅读代码的人看的说明 |
| `print("Hello World,Hello Python")` | 实际执行的输出语句 |
| 字符串中的 `#` | 是字符串内容，不会开始注释 |

### 2.3 快速切换行注释

**操作位置：VS Code 编辑器，不是 Python 代码或终端。**

在默认 Windows 快捷键下，选中一行或多行代码，按 **Ctrl + /**，可以切换行注释；如果使用了自定义快捷键，以实际设置为准。

原笔记中的 `cltr` 应改为 **Ctrl**。快捷键说明不应放在 `python` 代码块中，否则看起来像需要执行的代码。

### 2.4 一行一句与分号

入门练习建议 **一行写一句简单语句，通常省略分号**。

| 情况 | 推荐理解 |
| --- | --- |
| 两个 `print()` 各写一行 | 不需要用 `;` 分隔 |
| 两个简单语句写在同一行 | 可以用 `;` 分隔，但不建议为了省行数这样写 |
| 一条语句跨多行写 | 可能仍是一条语句；不能把所有物理换行都当作语句结束 |

最后一种属于**补充提醒**，第08课会通过续行示例说明。语法依据见 [Python 行结构说明](https://docs.python.org/3.13/reference/lexical_analysis.html#line-structure)。

## 3. 代码与输出

### 3.1 现有脚本的实际行为

[01.快速入门.py](01.快速入门.py) 中的输出语句是：

```python
print("Hello World,Hello Python")
```

它输出的是**一行文字**，逗号位于字符串里面，不会产生换行。

**运行位置：VS Code 的 PowerShell 终端。**

```powershell
cd "D:\专业技能\learning-journey\python\黑马python+AI\07 入门程序编写"
python ".\01.快速入门.py"
```

输出：

```text
Hello World,Hello Python
```

### 3.2 补充：如果希望输出两行

下面是独立练习示例，不表示现有脚本已经被修改：

```python
print("Hello World")
print("Hello Python")
```

输出：

```text
Hello World
Hello Python
```

这是因为每次 `print()` 默认会在输出结束后换行。

### 3.3 补充：分号可以分隔同一行的简单语句

```python
print("Hello World"); print("Hello Python")
```

输出与上一段相同：

```text
Hello World
Hello Python
```

**代码写在同一行，不代表输出一定在同一行。** 输出如何换行取决于执行的代码。

## 4. 易错点

| 容易混淆 | 正确理解 |
| --- | --- |
| 把 `Ctrl + /` 写成 Python 语句 | 它是编辑器快捷键，单独写在笔记正文中 |
| 认为任何 `#` 后面的内容都是注释 | 字符串内部的 `#` 仍是文字 |
| 认为 Python 每句结尾都必须有 `;` | 一行一句的普通写法通常不需要 |
| “换行总是语句终止符” | 括号内换行、显式续行等情况需要另外理解 |
| 在代码中使用中文引号 `“ ”` | 字符串定界符要用英文半角引号 `" "` 或 `' '` |

## 5. 自测与答案

1. **`print("# 你好")` 中的 `#` 是注释吗？**  
   不是。它在字符串内部，会随文字输出。

2. **`print("A"); print("B")` 会输出几行？为什么？**  
   两行。分号只分隔代码中的简单语句，两个 `print()` 默认各自输出并换行。

## 6. 本次优化与资料

- 修正 `cltr` 拼写，把快捷键从 Python 代码块移到操作说明。
- 将“换行作为终止符”改为适用范围更准确的解释。
- 对齐现有脚本的一行输出，并以**补充**形式提供两行输出与分号对比。
- 官方资料：[Python 注释规则](https://docs.python.org/3.13/reference/lexical_analysis.html#comments)、[简单语句](https://docs.python.org/3.13/reference/simple_stmts.html)、[print()](https://docs.python.org/3.13/library/functions.html#print)。

