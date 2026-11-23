# 76 包(package)（优化版）

> 整理日期：2026-11-24（北京时间）；截止／首次扫描：2026-11-24T01:55:08+08:00。课节首次学习日期未完整登记，历史资料补齐，原学习日期未确认；相关问答另按11月23日、24日的可靠记录标注。采用首次读取快照，不能还原消息发送瞬间版本。
> 来源：[76 包(package).md](<76 包(package).md>)；[76 包(package).py](<76 包(package).py>)。原始笔记、代码、图片保留。下文补充不表示用户已掌握或执行。

## 包与模块的层次

![原图 image.png](<image.png>)

**图片文字版（来源：image.png）：**

包用文件夹组织多个模块。图示utils下有my_fun.py、my_var.py、my_config.py及__init__.py；最外层包，下一层模块，模块内函数／变量／类。图中__init__.py用于标识本课的普通包并描述信息。

**纠正（核对P76逐字稿与官方定义）：**本课使用带__init__.py的普通包；缺少该文件也可能形成命名空间包，不能一概说绝对无法导入。__init__.py可以为空，第一次加载包时执行顶层初始化；不是只能写作者和版本。

## 导入与调用

![原图 image-1.png](<image-1.png>)

**图片文字版（来源：image-1.png）：**

有包时的五种导入与调用：

|导入|调用|
|---|---|
|import utils.my_fun|utils.my_fun.log_separator1()|
|from utils import my_fun|my_fun.log_separator1()|
|from utils import *|my_fun.log_separator1()（本包all列出它时）|
|from utils.my_fun import log_separator1|log_separator1()|
|from utils.my_fun import *|log_separator1()（模块公开导出时）|




![原图 image-2.png](<image-2.png>)

**图片文字版（来源：image-2.png）：**

再次列出五种导入。图中补充：若希望 `from utils import *` 导入指定子模块，在__init__.py写：
```python
__all__ = ["my_fun", "my_var"]
```

此清单约定星号导出名，不是访问权限，也不等于仅import utils就已经加载全部子模块。

**纠正：**包未定义__all__，`from utils import *` 本身仍合法，只是不自动遍历硬盘加载所有子模块；它导出当时包中已有的公开名字。当前utils只定义__all__，当 `from utils import *` 时可以按清单自动加载存在的my_fun、my_var；静态工具是否能推断此规则是另一个问题。具体实现见[utils独立笔记](<../utils/学习笔记-优化版.md>)。依据：[Python包和通配导入说明](https://docs.python.org/3.12/tutorial/modules.html#packages)。

### 原始代码：[76 包(package).py](<76 包(package).py>)


```python
# 1. 导入模块
# 形式1
# import utils.my_fun

# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()

# from utils import my_fun

# my_fun.log_separator1()

# 注意：如果要通过 from utils import * 导入包下的所有模块，需要在 __init__.py 文件中添加 __all__=[]

# from utils import *
# my_fun.log_separator1()
# my_fun.log_separator3()

# print(my_var.PI)
# print(my_var.NAME)

# 2. 导入模块中的功能
# from 绝对路径:从项目的根目录下找,相对路径: 在.py的同文件夹下
from utils.my_fun import log_separator1, log_separator3

log_separator1()
log_separator3()
```

### 当前目录为什么找不到utils

入口在 `p5 模块/76 包(package)`，utils在 `p5 模块/utils`，二者同级。一般直接按脚本路径启动时，搜索路径起点是脚本目录，不会自动把它的父目录当成“项目根”。`from utils.my_fun ...` 没有前导点，是绝对导入；从sys.path搜索。真正包内相对导入是 `from . import my_fun` 等，依赖包上下文。课件与原注释把“当前目录／项目根”简化成相对／绝对，在当前布局会误导，不能照搬。P76逐字稿确有此简化说法，本稿已与实际行为分开。

### 建议改写：[76 包(package)-优化版.py](<76 包(package)-优化版.py>)

**错误修复／新增语法：**用Path和__file__定位父目录、加入当前进程sys.path，再明确导入；不硬编码盘符。入口保护让import不再自动打印。直接运行仍只打印两条分隔线；生产项目更宜规范包布局与安装方式，这里给出适合现有教学目录、可直接运行的版本。


```python
"""来源：76 包(package).py；配套：76 包(package)-优化版.md。
整理日期：2026-11-24；原始文件保留。
"""

from pathlib import Path
import sys

# 原文件直接from utils.my_fun导入；utils是本脚本父目录中的同级文件夹，
# 单独启动脚本时该父目录通常不在搜索路径，可能ModuleNotFoundError。
# 新知识：__file__给当前文件位置；parents[1]是p5模块目录，与启动时cwd无关。
# 仅影响当前进程搜索路径，不修改环境变量或系统配置；加入的是已检查的本地课程目录。
module_root = str(Path(__file__).resolve().parents[1])
if module_root not in sys.path:
    sys.path.insert(0, module_root)

from utils.my_fun import log_separator1, log_separator3

# 原两个调用在顶层，导入也会打印；移入入口保护后只有直接运行才打印。
if __name__ == "__main__":
    log_separator1()
    log_separator3()
```

## 小结与编辑器问答（11月24日记录）

![原图 image-3.png](<image-3.png>)

**图片文字版（来源：image-3.png）：**

小结三问：包是什么、有什么作用？用目录归类模块便于管理维护。__init__.py有什么作用？标记普通包，并可做初始化和描述信息。包如何导入？整体模块、指定模块、包通配、指定成员、模块通配，共五种，调用形式取决于导入绑定的名字。

旧记录的 `76 包(package)/utils/__inti__.py` 当前不存在；本轮看到的是上一级 `utils/__init__.py`，拼写正确。记录说明当时曾改名或加显式导入，但当前文件没有那两条导入；不能拿历史界面通过当成当前版本已通过。先前AttributeError的原始运行现场不足，当前可复现的是路径导致ModuleNotFoundError，不能把所有错误都归因于init拼写。

VS Code可用“新建文件”输入 `utils/__init__.py` 建目录和文件；它不必像PyCharm有专门Python包菜单。目录图标取决于图标主题，不是解释器判包的证据。本轮只整理问答，未改主题或编辑器配置。用户片段 `main` / `__main__` 的建议、python.json设置和实际Ctrl+Space是否出现，是不同层次证据；记录中出现过已配置但列表未见，原因尚未确认。JSON截图与磁盘版本若不同，不能声称当前仍多套大括号；本轮未重读或改配置。

**复习：**为什么把文件放回p5后可能能导入，放进76子目录后失败？`__all__`控制的是哪种导入？为什么静态红线不等于运行必失败？

## 代码、命名与效率检查

当前原代码语法合法；在仅脚本目录和标准库路径的干净启动条件下，utils同级目录不可见，复现ModuleNotFoundError。将p5加入路径后可导入，优化版按文件位置补路径并保护打印入口。原先关于from路径的注释不精确，正文已纠正。

|原名|建议／保留|中文含义|位置|原因|
|---|---|---|---|---|
|utils|保留|工具包|导入语句|合法常见包名，但需要相应父目录在搜索路径上|
|__inti__.py（旧记录）|__init__.py（当前已正确）|普通包初始化文件|历史路径／当前utils|历史拼写错误已不在当前文件树，不继续列成当前未修复错误|

检查包含英文拼写、含义、缩写、大小写与下划线、单位及内置名遮蔽；除表中所列，未发现需要修改的问题。样本用户名和数据保持。未测性能，不把更短或改名当作提速。


## 参考与补漏

本次实际核对下载课程 BV1sHU9BmEne 的对应小节；参考包由 Video2Book 二次整理，纠正处与原意分开标注。不是整册已学范围。

- [模块13_模块与包：跨文件代码组织与导入机制_精读全书.md](<../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/textbooks/模块13_模块与包：跨文件代码组织与导入机制_精读全书.md>)：P76：499—553、585—681行，包和搜索路径。
- [笔记07_模块化组织与面向对象编程_笔记.md](<../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/notes/笔记07_模块化组织与面向对象编程_笔记.md>)：P76：包小节，止于204行。
- [P76_76. 核心语法-模块-包(package)_clean.txt](<../../../../../参考资料/黑马Python-AI课程笔记/计算机/编程语言/黑马程序员-Python-AI/subtitles/P76_76. 核心语法-模块-包(package)_clean.txt>)：全文：核对无__init__、__all__及“相对／绝对路径”的教学简化说法；未看视频。

