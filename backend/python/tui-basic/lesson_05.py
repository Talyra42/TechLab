import sys
import time

ESC = "\033"


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def fake_stream():
    for word in ["你好，", "我是 ", "Claude"]:
        time.sleep(0.02)
        yield word


def render(stream):
    for chunk in stream:
        write(chunk)

    write("\n")


if __name__ == "__main__":
    render(fake_stream())
    render(["a", "b", "C"])
