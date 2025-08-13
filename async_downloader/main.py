import asyncio

async def dowload_url(name, url):
    print (f'โหลด {name} จาก {url}')

async def main():
    await asyncio.gather(
        dowload_url("Example", "https://example.com"),
        dowload_url("Google", "https://google.com"),
        dowload_url("Python", "https://python.org"),
        dowload_url("GitHub", "https://github.com"),
        dowload_url("Stack Overflow", "https://stackoverflow.com"),
    )
asyncio.run(main())
    

      























URLS = [
    "https://example.com",
    "https://google.com",
    "https://python.org",
    "https://github.com",
    "https://stackoverflow.com",
]
