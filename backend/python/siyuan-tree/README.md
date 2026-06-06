# siyuan-tree

一个交互式 CLI 小工具，把**思源笔记**的文档树结构导出成树状图 / JSON / Markdown，方便归档或喂给 AI 识别。

## 功能

- 🌳 递归读取笔记本下的文档层级，渲染成彩色树状图
- ✅ 交互式多选要导出的笔记本（基于 `questionary`），也可一键导出全部
- 🎨 终端美化输出（基于 `rich`）
- 📦 三种输出格式：`tree` / `json` / `markdown`，统一保存到 `output/`

## 环境要求

- Python ≥ 3.11
- [uv](https://docs.astral.sh/uv/)（包管理）
- 思源笔记已启动（默认端口 `6806`）

## 安装

```bash
uv sync
```

## 配置

打开 [main.py](main.py)，修改顶部配置：

```python
SIYUAN_URL = "http://127.0.0.1:6806"   # 思源地址，一般不用改
API_TOKEN  = "你的 Token"               # ← 必填
MAX_DEPTH  = 999                        # 导出层级深度，999 = 不限制
```

> Token 位置：思源笔记 → 设置 → 关于 → API Token

## 使用

```bash
# 交互式选择笔记本，终端显示彩色树，并写入 output/res.txt
uv run python main.py

# 导出全部笔记本（跳过交互选择）
uv run python main.py --all

# 导出为 JSON（最适合喂给 AI），写入 output/res.json
uv run python main.py -a -f json

# 导出为 Markdown，自定义文件名 → output/tree.md
uv run python main.py -a -f markdown -o tree.md
```

### 参数

| 参数 | 说明 |
|------|------|
| `-a`, `--all` | 导出全部笔记本，跳过交互式选择 |
| `-f`, `--format {tree,json,markdown}` | 输出格式，默认 `tree` |
| `-o`, `--output FILE` | 输出文件名（默认 `res.txt`/`res.json`/`res.md`） |
| `-h`, `--help` | 显示帮助 |

> 交互模式下：**空格**勾选、**回车**确认、**Ctrl+C** 取消。

## 输出

所有导出文件统一存放在项目的 `output/` 目录（该目录已被 `.gitignore` 忽略）。
不指定 `-o` 时，按格式使用默认文件名：

| 格式 | 默认文件 | 内容 |
|------|----------|------|
| `tree` | `output/res.txt` | 纯文本树（终端另显示彩色版） |
| `json` | `output/res.json` | 嵌套结构，含 `id` / `title` / `path` / `children` |
| `markdown` | `output/res.md` | 嵌套列表，AI 友好 |

`json` 输出示例：

```json
{
  "notebooks": [
    {
      "id": "20210101...",
      "name": "我的笔记本",
      "docs": [
        {
          "id": "20210808...",
          "title": "父文档",
          "path": "/父文档",
          "children": [
            { "id": "...", "title": "子文档", "path": "/父文档/子文档", "children": [] }
          ]
        }
      ]
    }
  ]
}
```

## 工作原理

通过思源的本地 HTTP API：

1. `POST /api/notebook/lsNotebooks` 列出所有（未关闭的）笔记本
2. `POST /api/query/sql` 按 `hpath` 逐层查询 `blocks` 表中的文档块（`type='d'`），递归构建文档树
