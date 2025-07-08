"""
Configuration management for the Vocals SDK, mirroring the NextJS implementation.
"""

import os
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class VocalsConfig:
    """Configuration options for the Vocals SDK"""

    # Custom endpoint for token fetching (defaults to /api/wstoken)
    token_endpoint: Optional[str] = None

    # Custom headers for token requests
    headers: Optional[Dict[str, str]] = None

    # Auto-connect on initialization (defaults to True)
    auto_connect: bool = True

    # Reconnection attempts (defaults to 3)
    max_reconnect_attempts: int = 3

    # Reconnection delay in seconds (defaults to 1.0)
    reconnect_delay: float = 1.0

    # Token refresh buffer in seconds - refresh token this many seconds before expiry (defaults to 60)
    token_refresh_buffer: float = 60.0

    # WebSocket endpoint URL (if not provided, will try to get from token or use default)
    ws_endpoint: Optional[str] = None

    # Whether to use token authentication (defaults to True)
    use_token_auth: bool = True

    def __post_init__(self):
        """Initialize default values based on environment variables"""
        if self.token_endpoint is None:
            self.token_endpoint = "/api/wstoken"

        if self.headers is None:
            self.headers = {}

        if self.ws_endpoint is None:
            self.ws_endpoint = (
                os.environ.get("VOCALS_WS_ENDPOINT")
                or "ws://192.168.1.46:8000/v1/stream/conversation"
            )


# Default configuration instance
DEFAULT_CONFIG = VocalsConfig()


def get_default_config() -> VocalsConfig:
    """Get the default configuration with environment variable overrides"""
    return VocalsConfig(
        token_endpoint=os.environ.get("VOCALS_TOKEN_ENDPOINT", "/api/wstoken"),
        ws_endpoint=os.environ.get(
            "VOCALS_WS_ENDPOINT", "ws://192.168.1.46:8000/v1/stream/conversation"
        ),
        auto_connect=os.environ.get("VOCALS_AUTO_CONNECT", "true").lower() == "true",
        max_reconnect_attempts=int(
            os.environ.get("VOCALS_MAX_RECONNECT_ATTEMPTS", "3")
        ),
        reconnect_delay=float(os.environ.get("VOCALS_RECONNECT_DELAY", "1.0")),
        token_refresh_buffer=float(
            os.environ.get("VOCALS_TOKEN_REFRESH_BUFFER", "60.0")
        ),
        use_token_auth=os.environ.get("VOCALS_USE_TOKEN_AUTH", "true").lower()
        == "true",
    )
