from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def create_blog_article(text):

    prompt = f"""
Write an SEO optimized blog article.

Requirements:
- 700 words
- headings
- engaging style
- unique writing

NEWS:
{text}
"""

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content