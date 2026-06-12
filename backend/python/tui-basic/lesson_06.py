"""
所有的样式都是 ESC[...m 的格式
这个叫做 SGR，例如 [31m 就是一种设置前景色的方式：

类别	    码	        含义
重置	    0	        清空所有样式（你的「万能复位」）
字体	    1 2 3 4	    加粗 / 变暗 / 斜体 / 下划线
前景色	    30–37	    黑红绿黄蓝品青白
背景色  	40–47	    同上，但是底色
亮色前景	90–97	    更亮的那一档

同时，可以通过分号进行组合

最后，永远记得需要复位，也就是 [0m
"""

import sys
import time

ESC = "\033"


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def styled(text, code):
    return f"{ESC}[{code}m{text}{ESC}[0m"


def greeting():
    for word in "你好，我是 Claude，很高兴认识你。":
        time.sleep(0.02)
        yield word


def render(stream):
    for chunk in stream:
        write(chunk)
    write("\n")


if __name__ == "__main__":
    while True:
        write(styled("You", 34))
        write(" > ")
        try:
            i = input()
        except:  # noqa: E722
            write(styled("\nGood Bye.\n", 2))
            break
        # 我不知道橙色的编号
        write(styled("Claude", "38;2;255;165;0"))
        write(" > ")
        render(greeting())
