import pandas as pd
from sqlalchemy import create_engine

def ler_dados_pandas():
    try:
        engine = create_engine('sqlite:///database/imb.db')

        df_movies = pd.read_sql("SELECT * FROM movies", engine)

        df_series = pd.read_sql("SELECT * FROM series", engine)

        print("\nFilmes :")
        print(df_movies.head())

        print("\nSeries :")
        print(df_series.head())

        return df_movies, df_series

    except Exception as e:
        print("Erro ao acessar o banco: ", e)

