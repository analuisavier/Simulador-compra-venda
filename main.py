from dados_iniciais import *
from simulador import simular_mercado
import os

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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_pessoas(pessoas):
    print(f"{cor_roxo}[PESSOAS]{reset}")
    divisao = f"Divisão do rend. mensal: | Moradia {percentuais[0]*100:.1f}% | Alimentação {percentuais[1]*100:.1f}% | Transporte {percentuais[2]*100:.1f}% | Saúde {percentuais[3]*100:.1f}% | Educação {percentuais[4]*100:.1f}% | Totalizando {sum(percentuais)*100:.1f}% do rend. mensal total."
    print(f"{cor_branco}{divisao}{reset}")
    
    # Lógica para o gráfico de barras
    print(f"Gráfico de Barras | Legenda: {cor_ciano}Conforto{reset}, {cor_amarelo}Salário{reset}, {cor_verde}Rendimentos{reset}")
    
    max_valor = 0
    for p in pessoas:
        max_atual = max(p.conforto, p.salario, p.rendimento_mensal)
        if max_atual > max_valor:
            max_valor = max_atual
    
    escala = 80 / max_valor if max_valor > 0 else 0

    for i, p in enumerate(pessoas):
        bar_conforto = int(p.conforto * escala)
        bar_salario = int(p.salario * escala)
        bar_rendimento = int(p.rendimento_mensal * escala)
        
        print(f"{cor_ciano}{'|' * bar_conforto}{reset}")
        print(f"{cor_amarelo}{'|' * bar_salario}{reset}")
def print_empresas(empresas):
    print(f"\n{cor_roxo}[EMPRESAS]{reset}")
    for empresa in empresas:
        preco = empresa.get_preco()
        lucro_mes = empresa.vendas * (preco - empresa.custo)
        
        cat = f"[{empresa.categoria}]"
        nome_prod = f"{empresa.nome}: {empresa.produto}"
        qual_marg = f"(Q:{empresa.qualidade} Margem: {empresa.margem:.1%})"
        custo_str = f"Custo: R$ {empresa.custo:<8.2f}"
        preco_str = f"Preço: R$ {preco:<8.2f}"
        lucro_str = f"Lucro T.: R$ {empresa.lucro_total:<8.2f}"
        vendas_str = f"Vendas: {empresa.vendas}"
        
        print(f"{cor_ciano}{cat:<14}{reset}{cor_branco}{nome_prod:<38}{qual_marg:<22}{custo_str:<22}{preco_str:<22}{lucro_str:<25}{vendas_str}{reset}")

def main():
    populacao_pessoas()
    populacao_empresas()
    
    meses_simulados = 0
    
    simular = True
    while simular:
        clear()
        print(f"{cor_branco}[SIMULADOR DE RELAÇÕES DE MERCADO]{reset}")
        if meses_simulados > 0:
            print(f"Simulação após {meses_simulados} meses.")

        print_pessoas(pessoas)
        print_empresas(empresas)

        resposta = input(f"\n{cor_branco}Digite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: {reset}")
        
        if resposta.isdigit():
            meses = int(resposta)
            for _ in range(meses):
                simular_mercado(pessoas, empresas, categorias, percentuais)
            meses_simulados += meses
        elif resposta == "":
            simular_mercado(pessoas, empresas, categorias, percentuais)
            meses_simulados += 1
        elif resposta == "sair":
            simular = False

if __name__ == "__main__":
    main()
