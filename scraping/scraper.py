from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import os


def load_config():
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r") as f:
        return json.load(f)


def get_soup(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    req = Request(url, headers=headers)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup


def scrape_top_filmes(url, n_filmes=25):
    soup = get_soup(url)
    itens = soup.find_all("li", class_="ipc-metadata-list-summary-item")

    filmes = []

    for item in itens[:n_filmes]:
        titulo = item.find("h3", class_="ipc-title__text").text.strip()

        meta = item.find_all("span", class_="cli-title-metadata-item")
        ano = meta[0].text.strip()

        nota = item.find("span", class_="ipc-rating-star--rating").text.strip()

        filmes.append((titulo, ano, nota))

    return filmes

