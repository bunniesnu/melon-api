import httpx

class BaseClient:
    def __init__(self, timeout: float):
        """Create the underlying HTTP client with the timeout in seconds."""
        self.client = httpx.Client(timeout=timeout)

    def close(self):
        """Close the underlying :class:`httpx.Client`."""
        self.client.close()

    def __enter__(self):
        """Return this client for use in a ``with MelonClient()`` block."""
        return self

    def __exit__(self, *args):
        """Close the HTTP client when the context-manager block exits."""
        self.close()
