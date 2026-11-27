"""原练习：110 文件操作入门.py
配套说明：110 文件操作入门-优化版.md
"""

from pathlib import Path

# 原来的 "./望庐山瀑布.txt" 从终端工作目录查找。
# __file__ 指向本脚本，resolve().parent 取得脚本所在目录。
poem_path = Path(__file__).resolve().parent / "望庐山瀑布.txt"

# 原练习在末尾调用 f.close()。直接写 close() 会查找同名函数。
# with 会在离开缩进块时关闭文件，读取发生异常时也会关闭。
with open(poem_path, "r", encoding="utf-8") as poem_file:
    content = poem_file.read()

# content 已经读成字符串，关闭文件后仍可以输出。
print(content)
