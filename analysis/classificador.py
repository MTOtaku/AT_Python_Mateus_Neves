import pandas as pd

codigo = "sqlite:///database/imb.db"

def classificar_nota(nota):
    if nota >= 9.0:
        return "Obra-prima"
    elif nota >= 8.0:
        return "Excelente"
    elif nota >= 7.0:
        return "Bom"
    else:
        return "Mediano"


def classificar():
    try:
        df_movies = pd.read_sql("SELECT * FROM movies", codigo)

        df_sorted = df_movies.sort_values(by="rating", ascending=False)

        df_sorted["categoria"] = df_sorted["rating"].apply(classificar_nota)

        print(df_sorted[["title", "rating", "categoria"]].head(10))

    except Exception as e:
        print("Erro:", e)


def resumo_por_categoria():
    try:
        df_movies = pd.read_sql("SELECT * FROM movies", codigo)

        df_movies["categoria"] = df_movies["rating"].apply(classificar_nota)

        resumo = df_movies.pivot_table(
            index="categoria",
            columns="year",
            values="title",
            aggfunc="count",
            fill_value=0
        )

        print("\nResumo de filmes por categoria e ano:\n")
        print(resumo)

    except Exception as e:
        print("Erro:", e)