import termios
import tty
import sys


def read_key():
    ch = sys.stdin.read(1)
    # 普通按键 直接返回
    if ord(ch) != 27:
        return ch

    # 否则，要么就是 ESC，要么就是其他特殊按键
    # 只需要再尝试读两个字符
    ch2 = sys.stdin.read(2)
    if ch2 == "[A":
        return "UP"
    if ch2 == "[B":
        return "DOWN"
    if ch2 == "[D":
        return "LEFT"
    if ch2 == "[C":
        return "RIGHT"

    # 不知道，那么直接返回得了
    return ch


if __name__ == "__main__":
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)
        while True:
            user_input = read_key()
            if user_input == "q":
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
