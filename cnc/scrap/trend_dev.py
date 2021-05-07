import requests
from bs4 import BeautifulSoup


def get_dev_name(lang):
    lang = lang
    URL = "https://github.com/trending/developers/" + lang + "?since=monthly"
    scrap_url = requests.get(URL)
    scrap_soup = BeautifulSoup(scrap_url.text, "html.parser")

    names = []
    count = 0

    repos = scrap_soup.find_all("h1", {"class": 'h3 lh-condensed'})

    for repo in repos:
        if count == 3:  # iterate 3
            break
        count += 1

        name = repo.a.get_text()
        name = name.replace("\n", "")
        name = name.lstrip().rstrip()
        names.append(name)

    return names


def get_dev_id(lang):
    lang = lang
    URL = "https://github.com/trending/developers/" + lang + "?since=monthly"
    scrap_url = requests.get(URL)
    scrap_soup = BeautifulSoup(scrap_url.text, "html.parser")

    ids = []
    count = 0

    repos = scrap_soup.find_all("p", {"class": 'f4 text-normal mb-1'})

    for repo in repos:
        if count == 3:  # iterate 3
            break
        count += 1

        id = repo.a.get_text()
        id = id.replace("\n", "")
        id = id.lstrip().rstrip()
        ids.append(id)

    return ids