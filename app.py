import random
import time

import asyncpraw
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

red_api = asyncpraw.Reddit(user_agent="g.ronnia.me by /u/ListeningTo")


@app.get("/")
async def root():
    subreddit = await red_api.subreddit("osubuddyretard")
    hot_entries_gen = subreddit.hot(limit=100)

    random_entry = random.randint(0, 100)
    counter = 0
    async for entry in hot_entries_gen:
        if counter == random_entry:
            return RedirectResponse(entry.url)
        counter += 1
