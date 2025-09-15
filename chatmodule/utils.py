import asyncio
from urllib.parse import urlparse


def ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

def is_url(string):
    try:
        result = urlparse(string)
        # Check that scheme and netloc are present
        return all([result.scheme, result.netloc])
    except:
        return False

