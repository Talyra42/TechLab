import sys
import time

ESC = "\033"
LOADING_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


if __name__ == "__main__":
    # 2s 等待 0.1 间隔，需要20次
    for i in range(20):
        # 注意， \r 不是转义字符，他们自己就是控制字符
        write(
            "\r" + LOADING_FRAMES[i % len(LOADING_FRAMES)] + " 思考中..." + ESC + "[K"
        )
        time.sleep(0.1)
    # ESC + "[K" 的意思是：从光标当前位置，把这一行剩下的内容全部删掉
    write("\r" + "✓ 完成" + ESC + "[K")
    print("\n")
