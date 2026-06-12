import sys

"""
ESC 转义符，他是不可见的，可以写作：

\x1b
\033
chr(27)

他的作用是当作一个信号，终端一旦看到他，就知道接下来的东西不是需要展示的正文，而是一条命令
转义 这个词语，也是这么来的，让我们从正常打字模式出去，进入命令模式
"""
ESC = "\x1b"


def write(s):
    sys.stdout.write(s)
    # 立刻刷新，否则会卡在缓冲区，看不到
    sys.stdout.flush()


if __name__ == "__main__":
    # 清空屏幕
    write(ESC + "[2J")

    # 移动光标到第五行第十列
    write(ESC + "[5;10H")

    # 设置前景色为红色
    write(ESC + "[31m")

    # 普通打印，落在第五行第十列
    write("Hello, TUI!")

    # 恢复颜色
    write(ESC + "[0m")

    # 移动光标到下面
    write(ESC + "[20;1H")

"""
由此可以看出来，TUI 其实就是算好位置，把字符放在对应的网格的位置上就行
"""
