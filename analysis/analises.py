import pandas as pd

def analise():
    codigo = "sqlite:///database/imb.db"

    try:
        df_movies = pd.read_sql("SELECT * FROM movies",codigo)
        df_series = pd.read_sql("SELECT * FROM series",codigo)

        print("Dataframe carregado com sucesso!\n")

        df_sorted = df_movies.sort_values(by="rating", ascending=False)
        print("Filmes ordenados por Nota: \n")
        print(df_sorted.head(),"\n")
        # Honestamente, O proprio imdb já mostra filtrado por nota, logo esses filtros meio que são irrevelante


        df_filtered = df_sorted[df_sorted["rating"] > 9.0]
        #os unicos maiores que 9,0 são 7 no total, mas como pediu uns 5 ent ta ai

        print("Filmes com nota maior que 9.0: \n")
        print(df_filtered.head(),"\n")

        try:
            df_movies.to_csv("database/movies.csv", index=False)
            df_series.to_csv("database/series.csv", index=False)
            print("CSV exportado com sucesso!")

        except Exception as e:
            print("Erro ao salvar CSV", e)

        try:
            df_movies.to_json("database/movies.json", orient="records", indent=4)
            df_series.to_json("database/series.json", orient="records", indent=4)
        except Exception as e:
            print("Erro ao salvar JSON", e)

    except Exception as e:
        print("Erro: ", e)

