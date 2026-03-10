from rss_collector import collect_articles
from content_cleaner import clean_html
from ai_writer import create_blog_article
from blogger import post_to_blogger
from pdf_generator import create_pdf
from telegram_sender import send_pdf


def main():

    articles = collect_articles()

    pdf_articles = []

    for art in articles:

        title = art["title"]

        clean_text = clean_html(art["summary"])

        blog = create_blog_article(clean_text)

        post_to_blogger(title, blog)

        pdf_articles.append(
            f"<b>{title}</b><br/><br/>{blog}"
        )

    create_pdf(pdf_articles)

    send_pdf()


if __name__ == "__main__":
    main()