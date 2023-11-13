import time
import requests
import os
import json
from bs4 import BeautifulSoup
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.MAL
collection = db.anime_list


def get_ids():
    ids_as_text = []
    for j in range(0, 100):
        print(f"Call Number {j}")
        print(f"from id {j * 50 + 1} to {(j + 1) * 50}")
        page_url = f"https://myanimelist.net/topanime.php?limit={j * 50}"
        res = requests.get(page_url)
        soup = BeautifulSoup(res.text, "html.parser")
        ids_as_link = soup.find_all("a", {"class": "hoverinfo_trigger fl-l ml12 mr8"}, href=True)
        print(f"Found {len(ids_as_link)} Anime's")
        for id_as_link in ids_as_link:
            ids_as_text.append(id_as_link["href"])
    return ids_as_text


def extract_ids(ids_as_link):
    ids_list = []
    for id_as_link in ids_as_link:
        segments = id_as_link.split("/")
        ids_list.append(segments[4])
    return ids_list


def save_ids_in_file(lst):
    with open('ids.txt', "a") as fp:
        for item in lst:
            fp.write("%s\n" % item)
        print("IDs have been saved in ids.txt")


def read_ids_from_file():
    ids_from_file = []
    with open("ids.txt", "r") as fp:
        for line in fp:
            x = line[:-1]
            ids_from_file.append(x)
    return ids_from_file


def dump_json(lst):
    for item in lst:
        path = f"json/{item}.json"
        with open(path, "w+") as fp:
            fp.write(lst[item])


def grap_info(j, lst):
    anime_lst = {}
    for j in range(j, j + 10):
        print(f"Polling Anime Number {j}")
        url = f"https://api.jikan.moe/v4/anime/{lst[j]}/full"
        mal_anime = requests.get(url)
        anime_lst[lst[j]] = mal_anime.text
        time.sleep(1)
    return anime_lst


def read_num_json():
    dir_path = "json"
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count


if __name__ == '__main__':

    if not os.path.exists("ids.txt"):
        ids_text = get_ids()
        ids = extract_ids(ids_text)
        save_ids_in_file(ids)
    else:
        ids = read_ids_from_file()
        print("IDs are present")
        print(f"Number Of IDs: {len(ids)}")

    if read_num_json() < len(ids):
        print("Getting Anime Data")
        i = 0
        while i < len(ids):
            partial_list = grap_info(i, ids)
            dump_json(partial_list)
            i += 10

    if collection.count_documents({}) < 5000:
        print("Saving Json Files In The Database")
        file_count = 1
        for file in os.scandir("json"):
            file_count += 1
            with open(file) as f:
                collection.insert_one(json.load(f))
