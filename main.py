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
    print(f"\n[PESSOAS]")
    divisao = f"Divisão do renda mensal | Moradia {cor_amarelo}{percentuais[0]*100:.1f}%{reset} | Alimentação {cor_amarelo}{percentuais[1]*100:.1f}%{reset} | Transporte {cor_amarelo}{percentuais[2]*100:.1f}% {reset} | Saúde {cor_amarelo}{percentuais[3]*100:.1f}%{reset} | Educação {cor_amarelo}{percentuais[4]*100:.1f}%{reset} | Totalizando {cor_amarelo}{sum(percentuais)*100:.1f}%{reset} da renda mensal total."
    print(f"{cor_branco}{italico}{divisao}{reset}{reset}")
    print(f"{italico}Gráfico de Barras | Legenda: {italico}{cor_azul}Conforto{reset}{italico}, {cor_verde}Salário{reset}{italico}, {cor_roxo}Rendimentos{reset}{italico} | Cada traço = R$1000.00{reset}\n")

    #listas
    conforto_linhas = []
    rendimento_linhas = []

    for p in pessoas:
        conforto_barras = int(round((p.conforto / len(percentuais)) ))
        conforto_barras = min(conforto_barras, 10)
        conforto_linhas.append([cor_azul + "|" + reset] * conforto_barras)

        rendimento_patrimonial = p.patrimonio * 0.05
        salario = p.salario
        total_rendimento = salario + rendimento_patrimonial
        total_barras = min(int(total_rendimento // 1000), 10)

        barras_salario = min(int(salario // 1000), total_barras)
        barras_patrimonio = total_barras - barras_salario

        barras = [cor_roxo + "|" + reset] * barras_patrimonio + [cor_verde + "|" + reset] * barras_salario
        rendimento_linhas.append(barras)

    max_conforto = max(len(c) for c in conforto_linhas)
    for i in range(max_conforto):
        linha = ""
        for c in conforto_linhas:
            linha += c[i] if i < len(c) else " "
        print(linha)

    #Separador
    print(cor_branco + ("----") * 40 + reset)

    for nivel in reversed(range(10)):
        linha = ""
        for barras in rendimento_linhas:
            if nivel < len(barras):
                linha += barras[nivel]
            else:
                linha += " "
        print(linha)

def mostrar_vendas(vendas):
    if vendas >= 5:
        return cor_verde + ("$" * (vendas // 5)) + reset
    else:
        return ""
    
    
def print_empresas(empresas):
    print(f"\n{cor_branco}[EMPRESAS]{reset}")
    for empresa in empresas:
        preco = empresa.get_preco()
        lucro_mes = empresa.vendas * (preco - empresa.custo)
        
        cat = f"[{empresa.categoria}]"
        nome_prod = f"{empresa.nome}: {empresa.produto}"
        qual_marg = f"{cor_ciano}Q:{empresa.qualidade}{reset} Margem: {cor_amarelo}{empresa.margem:.1%}{reset}"
        custo_str = f"Custo:{cor_vermelho} R$ {empresa.custo:<8.2f}{reset}"
        preco_str = f"Preço:{cor_verde} R$ {preco:<8.2f}{reset}"
        lucro_str = f"Lucro T.:{cor_verde} R$ {empresa.lucro_total:<8.2f}{reset}"
        vendas_str = f"Vendas: {mostrar_vendas(empresa.vendas)}"
        
        print(f"{cat:<14}{nome_prod:<38}{qual_marg:<22}      {custo_str:<22}       {preco_str:<22}        {lucro_str:<25}       {vendas_str}{reset}")

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
