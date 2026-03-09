from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

def translate_korean(text):

    prompt = f"Translate this into Korean:\n\n{text}"

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content