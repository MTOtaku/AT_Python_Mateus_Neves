from database.bancoDados import *
from models.baseMovie import *
from models.baseSeries import Series
from scraping.scraper import *

config = load_config()
url = config["url"]
n_filmes = config["n_filmes"]


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

adicionar_no_database(catalog) # Isso aq so é o ex 6