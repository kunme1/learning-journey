"""来源：__init__.py；配套：学习笔记-优化版.md。
整理日期：2026-11-24；原始文件保留。
"""

# 原__init__.py仅写元数据和__all__，并未显式绑定两个子模块。
# 供采用的初始化片段如下：放回真正的__init__.py时，__package__为utils，走相对导入。
# 新知识：from . import引用当前包，直接import utils后即可访问已加载子模块；
# 行为变化：普通import utils也会提前加载子模块，不再等到star或明确导入时才加载。
if __package__:
    from . import my_fun, my_var
else:
    # 本文件名带“-优化版”，Python不会把它当初始化文件自动执行。
    # 为便于直接运行对照，按__file__补入p5目录后导入原utils的两个子模块。
    # 不覆盖原__init__.py；不修改持久环境配置，且不产生打印。
    from pathlib import Path
    import sys
    module_root = str(Path(__file__).resolve().parents[1])
    if module_root not in sys.path:
        sys.path.insert(0, module_root)
    from utils import my_fun, my_var

__version__ = "1.0.0"
__author__ = "kunme1"  # 原作者数据保留，不作为英文拼写错误改写。
__all__ = ["my_fun", "my_var"]
