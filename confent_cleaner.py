import re


def clean_html(text):

    clean = re.sub("<.*?>", "", text)
    clean = clean.replace("\n", " ")

    return clean