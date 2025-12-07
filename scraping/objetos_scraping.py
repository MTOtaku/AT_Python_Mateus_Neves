from scraping.scraper import load_config, scrape_top_filmes
from models.baseMovie import Movie
from models.baseSeries import Series

def lista_obj():
    config = load_config()
    url = config["url"]


    filmes_scrap = scrape_top_filmes(url, n_filmes=25)

    catalog = []

    for titulo, ano, nota in filmes_scrap:
        filme = Movie(titulo, ano, nota)
        catalog.append(filme)

    serie1 = Series('Teste 1',2025,3,36)
    serie2 = Series('Teste 2',2010,5,60)

    catalog.append(serie1)
    catalog.append(serie2)

    for i,item in enumerate(catalog, start=1):
        print(i,"-", item)

    return catalog