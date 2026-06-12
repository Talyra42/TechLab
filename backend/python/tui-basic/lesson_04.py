import sys
import time

ESC = "\033"
TARGET_STR = "你好，我是 Claude，正在思考中..."


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


for ch in TARGET_STR:
    write(ch)
    time.sleep(0.05)

write("\n")
