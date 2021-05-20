import requests
from bs4 import BeautifulSoup
import json


def return_json(name, start_date, end_date):
    name = name
    URL = "https://github.com/" + name
    scrap_url = requests.get(URL)
    scrap_soup = BeautifulSoup(scrap_url.text, "html.parser")

    # configuration settings -> Activity Overview
    activity_overview = scrap_soup.find_all("h5", {"class": "mb-3 text-normal"})

    width = 11

    if activity_overview:  # Activity Overview 세팅이 되어있는 경우
        width = 10

    data_count = []
    data_date = []
    data = scrap_soup.find_all("rect", {"width": width})

    if activity_overview:  # Activity Overview 세팅이 되어있는 경우
        data = data[:-5]

    for a in data:
        if start_date[0:4] == end_date[0:4] == a["data-date"][0:4]:
            if (start_date[5:7] + start_date[8:10] <= a["data-date"][5:7] + a["data-date"][8:10] <= end_date[
                                                                                                    5:7] + end_date[
                                                                                                           8:10]):
                data_date.append(a["data-date"])
                data_count.append(int(a["data-count"]))

        # Different Year
        else:
            if (start_date[0:4] == a["data-date"][0:4]) and (
                    start_date[5:7] + start_date[8:10] <= a["data-date"][5:7] + a["data-date"][8:10]):
                data_date.append(a["data-date"])
                data_count.append(int(a["data-count"]))

            if (end_date[0:4] == a["data-date"][0:4]) and (
                    a["data-date"][5:7] + a["data-date"][8:10] <= end_date[5:7] + end_date[8:10]):
                data_date.append(a["data-date"])
                data_count.append(int(a["data-count"]))

    data_json = {"date": data_date, "count": data_count}

    return data_json
