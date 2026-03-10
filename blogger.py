import requests
import os

BLOG_ID = os.environ["BLOG_ID"]
BLOGGER_TOKEN = os.environ["BLOGGER_TOKEN"]


def post_to_blogger(title, content):

    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"

    headers = {
        "Authorization": f"Bearer {BLOGGER_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "title": title,
        "content": content
    }

    try:

        res = requests.post(url, headers=headers, json=data)

        print("Blogger status:", res.status_code)

    except Exception as e:
        print("Blogger upload error:", e)