import asyncio

async def retry_async(func, retries=3, delay=2):
    """Retries an async function with exponential backoff."""
    for attempt in range(retries):
        try:
            return await func()
        except Exception as e:
            if attempt == retries - 1:
                raise e
            await asyncio.sleep(delay * (2 ** attempt))
