import requests
from bs4 import BeautifulSoup


def lang_json(name):
    name = name
    URL = "https://github-readme-stats.vercel.app/api/top-langs/?username=" + name + "&langs_count=20"
    scrap_url = requests.get(URL)
    scrap_soup = BeautifulSoup(scrap_url.text, "html.parser")

    languages = []
    attributes = []

    lang_data = scrap_soup.find_all("text", {"data-testid": "lang-name"})
    attr_data = scrap_soup.find_all("text", {"x": "215"})

    for a in lang_data:
        languages.append(a.get_text())

    for a in attr_data:
        attributes.append(a.get_text())

    data_json = {"lang": languages, "attr": attributes}

    return data_json
