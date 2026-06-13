import sys
import time

ESC = "\033"


def write(s: str) -> None:
    sys.stdout.write(s)
    sys.stdout.flush()


def fake_stream():
    for word in [
        "你好，这里是 *",
        "*Talyra42** 的代码测试部分，可以看看**",
        "这段文本*",
        "*是否加粗之类的，",
        "多多*",
        "*测试*",
        "*一下吧。\n1 + 1 = 2，",
        "**2 * 2 = 4**\n",
    ]:
        time.sleep(0.02)
        yield word


def render_markdown(stream):
    buffer = ""
    is_bold = 1

    for chunk in stream:
        for char in chunk:
            if char == "*":
                buffer += char
            else:
                if buffer == "*":
                    write(buffer)
                    buffer = ""
                write(char)
            if buffer == "**":
                write(f"{ESC}[{str(is_bold)}m")
                is_bold ^= 1
                buffer = ""
    write(f"{ESC}[0m")


if __name__ == "__main__":
    render_markdown(fake_stream())
