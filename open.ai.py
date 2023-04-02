import random
from uuid import uuid4

import openai
import requests

OPEN_API_KEY = "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"
openai.api_key = OPEN_API_KEY


def download_from_link(url: str, n: int):
    response = requests.get(url)
    open(f"birds/{uuid4()}.png", "wb").write(response.content)

def make_prompt():
    base = "superhero birds"
    styles = [
        "bird graphics", "bird", "bird design", "disney", "comics", "bird cartoon"
    ]
    genders = ["male", "female"]
    style, gender = "", ""
    if random.randint(0, 5) > 2:
        style = f" {random.choice(styles)} style"
    if random.randint(0, 5) > 4:
        gender = f" {random.choice(genders)} gender"

    return base + style + gender

while True:
    prompt = make_prompt()

    response = openai.Image.create(
        prompt=prompt,
        n=3,
        size="1024x1024"
    )

    for i, data in enumerate(response["data"]):
        download_from_link(url=data["url"], n=i)
