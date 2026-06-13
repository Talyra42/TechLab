import termios
import select
import tty
import sys
import os

ESC = "\033"


def write(s: str):
    sys.stdout.write(s)
    sys.stdout.flush()


def read_key(_fd):
    b = os.read(_fd, 1)
    ch = b.decode()
    if ch == "\x7f":
        return "BACK"
    if ch == "\n":
        return "ENTER"
    if ord(ch) != 27:
        return ch

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


def my_input(_fd):
    buffer = ""
    while True:
        key = read_key(_fd)
        if key == "BACK" and len(buffer) > 0:
            buffer = buffer[:-1]
        elif key == "ENTER":
            return buffer
        elif len(key) == 1 and ord(key) >= 32:
            buffer += key
        write("\r" + ESC + "[K" + buffer)


if __name__ == "__main__":
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)
        while True:
            user_input = my_input(fd)
            print(f"\n> {user_input}")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
