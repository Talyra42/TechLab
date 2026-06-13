import termios
import tty
import sys

if __name__ == "__main__":
    fd = sys.stdin.fileno()

    # 存档
    old = termios.tcgetattr(fd)

    try:
        # 改成生模式
        tty.setcbreak(fd)

        # 事务处理
        while True:
            ch = sys.stdin.read(1)
            print(f"ch: {ch}, ord(ch): {ord(ch)}")
            if ch == "q":
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
