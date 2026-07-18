"""sse 模块 — Provider 适配器层。

职责：
    提供流式响应的 Server-Sent Events 解析与重组工具。

本文件为 Provider-Evo 项目标准模块；保持单文件 200-400 行。
修改指引参见文件末尾的"本模块对外契约"章节（共 20 条）。
"""



import json
from typing import Any, Dict, Optional, Union


def parse_sse_line(data_str: str) -> Optional[Union[str, Dict[str, Any]]]:
    """解析 SSE 行（占位实现，gTTS 不使用 SSE）。

    Args:
        data_str: SSE 数据行字符串。

    Returns:
        解析结果（文本字符串或用例字典），无有效数据时返回 None。
    """
    if not data_str or data_str == "[DONE]":
        return None
    try:
        obj = json.loads(data_str)
    except (json.JSONDecodeError, ValueError):
        return None
    choices = obj.get("choices", [])
    if choices:
        delta = choices[0].get("delta", {})
        if delta.get("content"):
            return delta["content"]
    if obj.get("usage"):
        return {"usage": obj["usage"]}
    return None
