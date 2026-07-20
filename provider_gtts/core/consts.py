


from typing import Any, Dict, List

MODELS: List[str] = ["gtts-default"]
CAPS: Dict[str, bool] = {
    "audio_gen": True,
}

BASE_URL: str = "https://translate.google.com"
CHAT_PATH: str = "/_/TranslateWebserverUi/data/batchexecute"
TTS_PATH: str = "/translate_tts"

DEFAULT_MODEL: str = "gtts-default"
GTTS_DEFAULT_LANG: str = "zh-CN"
GTTS_DEFAULT_TLD: str = "com"
GTTS_SLOW: bool = False
GTTS_MAX_CHARS: int = 100

MAX_RETRIES: int = 3

# =======================================================================
# 重导出 — 同包内协同模块的公共符号（保持外部 ``from .. import`` 路径稳定）
# =======================================================================

from .headers import (
    build_headers,
)

from .payload import (
    build_payload,
)

__all__ = [
    "build_headers",
    "build_payload",
]
