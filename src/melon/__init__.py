"""Synchronous client for Melon's chart endpoints.

Every endpoint returns an envelope whose parsed payload is in ``response``.
The methods in :class:`MelonClient` unwrap that envelope and validate it with
the matching model.
"""

from melon.chart import ChartClient
from melon.album import AlbumClient

class MelonClient(ChartClient, AlbumClient):
    """Reusable synchronous HTTP client for Melon chart and chart-graph APIs."""
    def __init__(self, timeout: float = 10.0):
        """Create the underlying HTTP client with the timeout in seconds."""
        super().__init__(timeout=timeout)