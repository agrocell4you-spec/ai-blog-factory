from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

def rewrite_article(text):

    prompt = f"""
Rewrite the following news summary into an original SEO blog article.

Requirements:
- around 600 words
- unique writing
- SEO friendly
- headings included

TEXT:
{text}
"""

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content