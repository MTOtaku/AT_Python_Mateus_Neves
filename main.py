from scraping.scraper import *


def main():
    config = load_config()
    url = config["url"]
    n_filmes = config["n_filmes"]
