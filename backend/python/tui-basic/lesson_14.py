import termios
import select
import tty
import sys
import os


def read_key(_fd):
    ch = os.read(_fd, 1).decode()
    if ord(ch) != 27:
        return ch

    # 处理单点 ESC 的识别问题
    ready, _, _ = select.select([sys.stdin], [], [], 0.05)
    if not ready:
        return "ESC"

    ch2 = os.read(_fd, 2).decode()
    if ch2 == "[A":
        return "UP"
    if ch2 == "[B":
        return "DOWN"
    if ch2 == "[D":
        return "LEFT"
    if ch2 == "[C":
        return "RIGHT"

    return ch


if __name__ == "__main__":
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)
        while True:
            user_input = read_key(fd)
            if user_input == "q":
                break
            print(user_input)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
