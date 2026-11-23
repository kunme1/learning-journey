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
