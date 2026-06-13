import sys
import shutil
import unicodedata

ESC = "\033"


def write(s: str):
    sys.stdout.write(s)
    sys.stdout.flush()


def display_width(s: str) -> int:
    counter = 0
    in_escape = False

    for char in s:
        if char == ESC:
            in_escape = True
            continue
        if char == "m" and in_escape:
            in_escape = False
            continue

        if unicodedata.east_asian_width(char) in "WF":
            if not in_escape:
                counter += 2
        else:
            if not in_escape:
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
    styled_text = f"普通文字{ESC}[1m加粗的部分{ESC}[0m后面还有很多文字内容测试换行"
    print(wrap(styled_text, 20))
