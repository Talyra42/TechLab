import sys

ESC = "\x1b"


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


# 移动光标
def move(row, col):
    # 一定注意，位置中间用的不是冒号，而是分号
    write(f"{ESC}[{row};{col}H")


# 修改颜色
def color(code):
    write(f"{ESC}[{code}m")


# 画一个框
def draw_box(top, left, width, height):
    # 上边框
    move(top, left)
    write("+" + "-" * (width - 2) + "+")

    # 左右边框
    for i in range(1, height - 1):
        move(top + i, left)
        write("|")
        move(top + i, left + width - 1)
        write("|")

    # 下边框
    move(top + height - 1, left)
    write("+" + "-" * (width - 2) + "+")


if __name__ == "__main__":
    write(ESC + "[2J")

    # 在行3，列5，绘制一个宽30，高6的框框
    draw_box(3, 5, 30, 6)

    # 绘制内容
    move(5, 8)
    color("36")
    write("我是内容")
    color("0")

    # 收尾
    move(20, 1)
