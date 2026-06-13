import sys
import shutil
import unicodedata

ESC = "\033"


def write(s: str):
    sys.stdout.write(s)
    sys.stdout.flush()


def display_width(s: str) -> int:
    counter = 0

    for char in s:
        if unicodedata.east_asian_width(char) in "WF":
            counter += 2
        else:
            counter += 1

    return counter


def wrap(text: str, max_width: int):
    buffer = ""
    res = ""

    for c in text:
        if display_width(buffer + c) > max_width:
            res += buffer + "\n"
            buffer = c
        else:
            buffer += c
    res += buffer
    return res


if __name__ == "__main__":
    print(f"终端宽度为：{shutil.get_terminal_size().columns}")
    print(display_width("我是 Talyra42"))
    print(display_width("A"))

    print(wrap("你好，你好，测试，测试，good，good？测试测试输入输入 input out", 20))
