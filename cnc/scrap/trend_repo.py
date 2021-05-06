import requests
from bs4 import BeautifulSoup


def get_repository(lang):  # 언어에 따른 trend repo 반환
    lang = lang
    URL = "https://github.com/trending/" + lang + "?since=monthly"
    scrap_url = requests.get(URL)
    scrap_soup = BeautifulSoup(scrap_url.text, "html.parser")

    repositories = []
    count = 0

    repos = scrap_soup.find_all("h1", {"class": 'h3 lh-condensed'})

    for repo in repos:
        if count == 3:  # iterate 3
            break
        count += 1
        repositories.append("https://github.com" + repo.a["href"])

    return repositories


def get_description(lang):  # 언어에 따른 trend repo description 반환
    lang = lang
    URL = "https://github.com/trending/" + lang + "?since=monthly"
    scrap_url = requests.get(URL)
    scrap_soup = BeautifulSoup(scrap_url.text, "html.parser")

    description = []
    count = 0

    desc = scrap_soup.find_all("p", {"class": 'col-9 color-text-secondary my-1 pr-4'})

    for d in desc:
        if count == 3:  # iterate 3
            break
        count += 1
        text = d.get_text()
        text = text.replace("\n", "")
        text = text.lstrip().rstrip()
        description.append(text)

    return description
