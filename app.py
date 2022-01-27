import random

import asyncpraw
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

red_api = asyncpraw.Reddit(user_agent="g.ronnia.me by /u/ListeningTo")
subreddit = red_api.subreddit("osubuddyretard")


@app.get("/")
async def root():
    hot_entries_gen = subreddit.hot()

    random_entry = random.randint(0, 100)
    counter = 0
    for entry in hot_entries_gen:
        if counter == random_entry:
            return RedirectResponse(entry.url)
        counter += 1
