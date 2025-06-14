from dados_iniciais import pessoas, empresas, categorias, percentuais

# Códigos de escape ANSI
cor_vermelho = "\033[31m"
cor_verde = "\033[32m" 
cor_azul = "\033[34m"
cor_amarelo = "\033[33m"
cor_roxo = "\033[35m"
cor_ciano = "\033[36m"
cor_branco = "\033[37m"
italico = "\033[3m"
reset = "\033[0m"

def main():
    print("[SIMULADOR DE MERCADO]")
    print(f"{len(pessoas)} pessoas cadastradas.")
    print(f"{len(empresas)} empresas cadastradas.")
    print("Categorias disponíveis:")
    for categoria in categorias:
        print(f"- {categoria}")

if __name__ == "__main__":
    main()
