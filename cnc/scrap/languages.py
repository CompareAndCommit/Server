import requests
from bs4 import BeautifulSoup


def lang_json(name):
    name = name
    URL = "https://github-readme-stats.vercel.app/api/top-langs/?username=" + name + "&langs_count=20"
    scrap_url = requests.get(URL)
    scrap_soup = BeautifulSoup(scrap_url.text, "html.parser")

    languages = []
    percentage = []

    lang_data = scrap_soup.find_all("text", {"data-testid": "lang-name"})
    pct_data = scrap_soup.find_all("text", {"x": "215"})

    for a in lang_data:
        languages.append(a.get_text())

    for a in pct_data:
        percentage.append(a.get_text()[:-1])  # '%' 제거

    data_json = {"lang": languages, "pct": percentage}

    return data_json
