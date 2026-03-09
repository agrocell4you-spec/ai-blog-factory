import os
print("BLOGGER_TOKEN:", os.getenv("BLOGGER_TOKEN"))


from trends import get_trending_keywords
from news import get_news
from rewrite import rewrite_article
from translator import translate_korean
from blogger import post_to_blogger
from pdf_generator import create_pdf
from telegram_sender import send_pdf

articles_pdf = []

keywords = get_trending_keywords()

for keyword in keywords:

    news_list = get_news(keyword)

    text = " ".join([n["summary"] for n in news_list])

    article_en = rewrite_article(text)

    article_kr = translate_korean(article_en)

    title = keyword

    post_to_blogger(title, article_en)

    articles_pdf.append(
        f"<b>{title}</b><br/><br/>{article_en}<br/><br/>{article_kr}"
    )

create_pdf(articles_pdf)


send_pdf()
