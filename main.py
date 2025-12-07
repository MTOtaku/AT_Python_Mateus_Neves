from menus.menu import menu
from scraping.objetos_scraping import lista_obj
from database.bancoDados import adicionar_no_database
from database.codigoPandas import ler_dados_pandas
from analysis.analises import analise
from analysis.classificador import classificar, resumo_por_categoria

def main():

    catalog = None

    while True:
        opcao = menu()

        if opcao == "1":
            catalog = lista_obj()
            print("Catálogo criado com sucesso!")

        elif opcao == "2":
            if catalog is None:
                print("Você precisa criar o catálogo primeiro! (opção 1)")
            else:
                adicionar_no_database(catalog)

        elif opcao == "3":
            ler_dados_pandas()

        elif opcao == "4":
            analise()

        elif opcao == "5":
            classificar()

        elif opcao == "6":
            resumo_por_categoria()

        elif opcao == "0":
            print("Saindo... até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
