# 第04课：Python 程序初体验

> 基于 [原笔记](note.md) 整理，配套代码：[hello.py](hello.py)。标注为「补充」的内容用于帮助复习。

## 1. 本课目标

- 认识 Python 解释器，知道 `>>>` 表示什么。
- 理解 `print()` 可以输出文字。
- 能在终端里运行一个 `.py` 文件。

## 2. 核心知识

### 2.1 Python 解释器与两种使用方式

**解释器是执行 Python 代码的程序。** 编辑器负责写代码，解释器负责执行代码。

| 方式 | 怎么使用 | 适合做什么 |
| --- | --- | --- |
| 交互模式 | 在终端输入 `python`，再在 `>>>` 后输入 Python 代码 | 临时试验一两条代码 |
| 脚本模式 | 把代码保存在 `.py` 文件中，再运行 `python 文件路径` | 保存、反复运行和维护程序 |

在 VS Code 的 PowerShell 终端输入；**运行位置：任意目录**：

```powershell
python
```

通常会看到版本说明和 `>>>` 提示符。在 `>>>` 后可以输入 `print("hello world")`，输入 `exit()` 并按回车可退出交互模式。

### 2.2 分清终端提示符与 Python 提示符

| 看到的提示符 | 所在位置 | 应该输入什么 |
| --- | --- | --- |
| `PS D:\专业技能>` | PowerShell 终端 | `cd`、`python 文件路径`、`git status` 等终端命令 |
| `D:\专业技能>` | Windows CMD 的常见形式 | CMD 支持的终端命令 |
| `>>>` | 标准 Python 交互模式 | `print(...)` 等 Python 代码 |

这些提示符是程序显示的，**复制命令时不用复制提示符**。不能仅凭“显示了路径”判断环境，要结合 `PS`、`>>>` 等完整提示。

### 2.3 读懂 print()

```python
print("hello world")
```

输出：

```text
hello world
```

| 部分 | 含义 |
| --- | --- |
| `print` | Python 内置的输出函数 |
| `(...)` | 调用函数，把括号里的内容交给函数处理 |
| `"hello world"` | 字符串，也就是用引号包住的文字 |
| 引号 | 标记字符串边界，通常不会作为输出内容显示 |

`print()` 默认在输出结束后换行；`Hello World` 与 `hello world` 的大小写不同，输出也不同。参见 [Python print() 文档](https://docs.python.org/3.13/library/functions.html#print)。

## 3. 代码与输出

### 3.1 运行当前目录中的 hello.py

同目录 `hello.py` 的现有内容是：

```python
print("hello world")
```

**运行位置：VS Code 的 PowerShell 终端。** 先进入文件所在目录，再执行脚本：

```powershell
cd "D:\专业技能\learning-journey\python\黑马python+AI\04"
python .\hello.py
```

- `cd`：进入指定文件夹。
- `python`：启动终端当前找到的 Python 解释器。
- `.\hello.py`：当前目录中的 `hello.py`；`.\` 表示从当前目录开始查找。

输出：

```text
hello world
```

### 3.2 补充：直接使用绝对路径

**运行位置：任意目录的 PowerShell 终端。**

```powershell
python "D:\专业技能\learning-journey\python\黑马python+AI\04\hello.py"
```

输出仍然是 `hello world`。文件路径较长时，用英文双引号包住路径，尤其适合包含空格的目录。

原笔记里“在文件资源管理器地址栏输入 `cmd`”也是进入文件所在目录的一种方式。当前使用 VS Code 时，直接使用内置终端即可，以上示例统一采用 PowerShell。

## 4. 易错点

| 容易混淆 | 正确理解 |
| --- | --- |
| 在 `>>>` 后输入 `python hello.py` | 这是终端命令，应先退出交互模式再执行 |
| 在 PowerShell 里直接输入 `print(...)` | 这是 Python 代码，应写进 `.py` 文件或 Python 交互模式 |
| 以为修改文件后输出会立即变化 | 先保存文件，再重新运行 |
| 认为只有多行程序才需要 `.py` 文件 | 一行程序也能保存在 `.py` 文件中 |

## 5. 自测与答案

1. **`>>>` 表示什么？如何回到终端？**  
   表示正在 Python 交互模式；输入 `exit()` 并按回车退出。

2. **执行 `python .\hello.py` 时，`hello.py` 从哪里查找？**  
   从当前工作目录查找；如果找不到，检查当前目录，或改用文件的绝对路径。

## 6. 本次优化与资料

- 修复原笔记 `##3` 缺少空格的问题，统一标题层级。
- 将终端、交互模式、脚本模式分开说明，运行示例与现有 `hello.py` 的输出保持一致。
- **补充：**提示符辨认、路径解释和自测，未修改原代码。
- 官方资料：[Python 解释器使用](https://docs.python.org/3.13/tutorial/interpreter.html)、[交互模式](https://docs.python.org/3.13/tutorial/appendix.html#interactive-mode)。

