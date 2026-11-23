# 第06课：开发工具与 IDE

> 本次整理日期：2026-11-14（北京时间）；历史资料补齐，原学习日期未确认。来源为本课同目录原笔记、代码和配图。

> 基于 [原笔记](note.md) 整理。课程演示使用 PyCharm，本次学习使用已有的 VS Code 与 Python 环境；标注为「补充」的内容帮助区分工具职责。

> 排版调整：2026-11-14（北京时间）。以原笔记顺序为主线，图文和补充就近组织；沿用原有转写与验证记录，本次未修改原始材料或重新执行程序。

05:安装问题,直接跳过
例如VS Code,PyCharm   
```
IDE:集成开发环境:代码编写，分析功能，调试
```

![课程截图：IDE 的英文全称及代码编写、分析、调试等功能说明](image.png)

**图片文字版：**IDE 是 Integrated Development Environment（集成开发环境），提供代码编写、代码分析与调试等功能。

### 补充：本课目标

- 知道 IDE 的全称和用途。
- 区分 VS Code、Python 扩展、解释器的职责。
- 理解为什么可以沿用现有环境学习课程。

### 补充：IDE 是什么

**IDE：Integrated Development Environment，集成开发环境。**

| 英文词 | 中文含义 |
| --- | --- |
| Integrated | 集成的 |
| Development | 开发 |
| Environment | 环境 |

IDE 把代码编辑、代码分析、调试等功能组织在一个工具中，方便开发者完成程序开发。PyCharm 是针对 Python 开发的 IDE。

课程中的概念截图：

这里使用的PyCharm，已有VS Code现有环境3.13.9，跳过

### 补充：分清三个角色

| 工具 | 主要职责 | 本课中的理解 |
| --- | --- | --- |
| VS Code | 编辑文件、管理工作区、提供终端等 | 你当前写代码和笔记的工具；可通过扩展增加语言支持 |
| VS Code 的 Python 扩展 | 提供 Python 运行、调试、解释器选择等集成入口 | 帮 VS Code 更方便地处理 Python 项目 |
| Python 解释器 | 实际执行 Python 代码 | 即使打开了 VS Code，也要有可用的解释器 |

**安装编辑器或扩展，不等于安装 Python 解释器。** 安装微软 Python 扩展后，仍需使用已安装的 Python。参见 [VS Code Python 官方说明](https://code.visualstudio.com/docs/languages/python)。

### 补充：本次学习为什么沿用 VS Code

原记录中的 Python 版本是 **3.13.9**，此前已经成功运行 `hello.py`。因此可以沿用已有工具学习语法，理解课程操作的目的，再在 VS Code 中完成相应操作。

原笔记中“05 安装问题直接跳过”可以更准确地记成：

> 第05课涉及安装问题排查；当前环境已能运行程序，先继续学习。以后遇到安装或运行问题，再回看对应部分。

不同工具的按钮和项目管理方式可能不同，但执行的是同一种 Python 语言。

### 补充：检查终端能否找到 Python

**运行位置：VS Code 的 PowerShell 终端，任意目录。**

```powershell
python --version
```

- `python`：使用当前终端找到的 Python。
- `--version`：显示版本后退出。

本次学习曾得到：

```text
Python 3.13.9
```

切换解释器或环境后，版本可能不同；版本号是检查结果，不应写进 Python 代码中。

### 补充：选择 VS Code 使用的解释器

**操作位置：VS Code 命令面板，不是终端。**

1. 按 **Ctrl + Shift + P** 打开命令面板。
2. 搜索 **Python: Select Interpreter**。
3. 从列表中选择本项目要使用的解释器。

VS Code 的运行、调试等 Python 功能会使用所选解释器；已经打开的终端可能仍保留原环境。若在终端手动输入 `python`，需要同时关注终端自己的环境。

### 补充：易错点

| 容易混淆 | 正确理解 |
| --- | --- |
| “VS Code 就是 Python” | VS Code 是开发工具，Python 解释器负责运行代码 |
| “装了 Python 扩展就不用装解释器” | 扩展与解释器是不同组件 |
| “老师用 PyCharm，我必须换工具” | 可以继续使用 VS Code，理解每一步对应的作用即可 |
| “跳过安装就是安装知识不重要” | 本次是已有环境可用，不需要重复配置；排错时仍可回看课程 |

### 补充：-11-14 查漏补充

本课没有原始.py文件，无本地代码可评审；英文全称拼写与含义正常，未发现需要修改的问题。不涉及程序效率优化。

## 5. 自测与答案

1. **谁负责执行 `print("hello world")`？**  
   Python 解释器。VS Code 和扩展负责提供编辑与运行等入口。

2. **终端能运行 Python，为什么还要关注 VS Code 选择的解释器？**  
   编辑器运行、调试与终端命令可能使用不同的环境，需要确认本项目实际使用的是哪一个。

## 6. 本次优化与资料

- 保留课程截图，将放在普通代码块里的 IDE 定义改为正文和词义表。
- 将“直接跳过”改成有原因、以后可回查的学习记录。
- **补充：**编辑器、扩展、解释器的区别，以及版本检查和解释器选择方法。
- 官方资料：[VS Code Python 支持](https://code.visualstudio.com/docs/languages/python)、[Python 环境选择](https://code.visualstudio.com/docs/python/environments#_select-an-environment)。
