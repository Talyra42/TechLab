#!/usr/bin/env python3
"""
思源笔记结构导出脚本
运行前请确认：
  1. 思源笔记已启动（默认端口 6806）
  2. 在思源「设置 - 关于」中找到 API Token 并填入下方
"""

import json
import sys
import urllib.request
import urllib.error

# ── 配置 ──────────────────────────────────────────
SIYUAN_URL = "http://127.0.0.1:6806"
API_TOKEN = "sh9d8aw3rslyeb7q"  # ← 替换成你的 Token
MAX_DEPTH = 999  # 导出层级深度，999 = 不限制
# ─────────────────────────────────────────────────


def post(endpoint: str, payload: dict = None) -> dict:
    url = f"{SIYUAN_URL}{endpoint}"
    data = json.dumps(payload or {}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Token {API_TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"[错误] 无法连接思源笔记：{e}")
        print("  请确认思源已启动，且地址/端口正确。")
        sys.exit(1)

    if result.get("code") != 0:
        print(f"[错误] API 返回异常：{result.get('msg')}")
        sys.exit(1)
    return result["data"]


def get_notebooks() -> list:
    data = post("/api/notebook/lsNotebooks")
    return data.get("notebooks", [])


def get_docs(notebook_id: str, parent_path: str = "/") -> list:
    """通过 SQL 查询某笔记本下某路径的直接子文档"""
    # blocks 表中 type='d' 是文档块，hpath 是可读路径
    # 用 LIKE 匹配直接子级：hpath 匹配 /parent/% 且不含更深的 /
    sql = f"""
        SELECT id, hpath, content
        FROM   blocks
        WHERE  type = 'd'
          AND  box  = '{notebook_id}'
          AND  hpath LIKE '{parent_path.rstrip("/")}/%'
          AND  hpath NOT LIKE '{parent_path.rstrip("/")}/%/%'
        ORDER  BY hpath
    """
    rows = post("/api/query/sql", {"stmt": sql})
    return rows or []


def print_tree(notebook_id: str, parent_path: str, indent: int):
    if indent >= MAX_DEPTH:
        return
    docs = get_docs(notebook_id, parent_path)
    for doc in docs:
        title = doc.get("content") or doc.get("hpath", "").split("/")[-1]
        prefix = "│   " * (indent - 1) + ("├── " if indent > 0 else "")
        print(f"{prefix}{title}")
        # 递归子级
        print_tree(notebook_id, doc["hpath"], indent + 1)


def main():
    if API_TOKEN == "your_token_here":
        print("[提示] 请先在脚本顶部填写你的 API Token，然后重新运行。")
        print("       Token 位置：思源笔记 → 设置 → 关于 → API Token")
        sys.exit(0)

    print("正在连接思源笔记……\n")
    notebooks = get_notebooks()

    if not notebooks:
        print("未找到任何笔记本（或全部已关闭）。")
        return

    for nb in notebooks:
        if nb.get("closed"):
            continue
        nb_name = nb.get("name", nb["id"])
        print(f"📓 {nb_name}")
        print_tree(nb["id"], "/", 1)
        print()

    print("✅ 导出完成")


if __name__ == "__main__":
    main()
