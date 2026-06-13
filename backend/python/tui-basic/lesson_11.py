import sys
import unicodedata

ESC = "\033"


def write(s: str):
    sys.stdout.write(s)
    sys.stdout.flush()


def render_markdown(stream):
    res = ""
    buffer = ""
    is_bold = 1

    for chunk in stream:
        for char in chunk:
            if char == "*":
                buffer += char
            else:
                if buffer == "*":
                    res += buffer
                    buffer = ""
                res += char
            if buffer == "**":
                res += f"{ESC}[{str(is_bold)}m"
                is_bold ^= 1
                buffer = ""
    res += f"{ESC}[0m"
    return res


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
        if c == "\n":
            res += buffer + "\n"
            buffer = ""
            continue
        if display_width(buffer + c) > max_width:
            res += buffer + "\n"
            buffer = c
        else:
            buffer += c
    res += buffer
    return res


if __name__ == "__main__":
    markdown = "Hello **Talyra42**! This is Good Job!\n**2 * 2 = 4**!"
    styled = render_markdown(markdown)
    wrapped = wrap(styled, 20)
    write(wrapped + "\n")
