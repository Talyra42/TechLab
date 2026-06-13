import sys

ESC = "\033"


def write(s: str) -> None:
    sys.stdout.write(s)
    sys.stdout.flush()


def render_markdown(s: str) -> str:
    res = ""

    bold = 1

    for i in range(len(s)):
        if s[i] == "*":
            if i + 1 < len(s) and s[i + 1] == "*":
                res = res + ESC + "[" + str(bold) + "m"
                bold = bold ^ 1
        else:
            res = res + s[i]
    return res


if __name__ == "__main__":
    write(render_markdown("**Hello World** Here is a **Good** world.\n"))
