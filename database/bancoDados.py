from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

from models.baseMovie import Movie
from models.baseSeries import Series

database_url = "sqlite:///database/imb.db"

engine = create_engine(database_url, echo=False)

Base = declarative_base()

class MovieDB(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Float)



class SeriesDB(Base):
    __tablename__ = "Series"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    seasons = Column(Integer)
    episodes = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Essa parte toda e essa de baixo é do Exercicio 6

def adicionar_no_database(catalog):
    for item in catalog:

        if isinstance(item, Movie):
            existente = session.query(MovieDB).filter_by(
                title=item.title,
                year=item.year,
            ).first()

            if existente:
                print(f"os Seguinte filme não foi adicionado pois ja existe: {item.title}")
                continue

            movie_db = MovieDB(
                title=item.title,
                year=item.year,
                rating=item.rating
            )
            session.add(movie_db)

        elif isinstance(item, Series):
            existente = session.query(SeriesDB).filter_by(
                title=item.title,
                year=item.year
            ).first()

            if existente:
                print(f"A seguinte Serie não foi adicionada pois ja existe: {item.title}")
                continue

            series_db = SeriesDB(
                title=item.title,
                year=item.year,
                seasons=item.seasons,
                episodes=item.episodes
            )
            session.add(series_db)

    session.commit()
    print("Itens adicionado ao banco")




