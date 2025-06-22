from pessoa import Pessoa
from empresa import Empresa

pessoas = []
empresas = []

categorias = ["Moradia", "Alimentação", "Transporte", "Saúde", "Educação"]

percentuais = [0.35, 0.25, 0.10, 0.10, 0.10]




def add_pessoas(num_pessoas, patrimonio, salario, variacao=0.0):
    for i in range(num_pessoas):
        pessoas.append(Pessoa(patrimonio + i * variacao, salario + i * variacao))



def populacao_pessoas():
    add_pessoas(5,  patrimonio=20000000, salario=0,      variacao=0)     
    add_pessoas(10, patrimonio=200000,   salario=100000, variacao=-5000) 
    add_pessoas(25, patrimonio=100000,   salario=30000,  variacao=-1000) 
    add_pessoas(50, patrimonio=10000,    salario=5000,   variacao=-50)   
    add_pessoas(70, patrimonio=10000,    salario=1518,   variacao=0)     

    

def populacao_empresas():
    empresas.append(Empresa("Moradia",     "    República A", "Aluguel, Várzea", 300.0,  qualidade=3))
    empresas.append(Empresa("Moradia",     "    República B", "Aluguel, Várzea", 300.0,  qualidade=3))
    empresas.append(Empresa("Moradia",     "CTI Imobiliária", "Aluguel, Centro", 1500.0, qualidade=7))
    empresas.append(Empresa("Moradia",     "Orla Smart Live", "Aluguel, Boa V.", 3000.0, qualidade=9))
    empresas.append(Empresa("Alimentação", "          CEASA", "Feira do Mês   ", 200.0,  qualidade=3))
    empresas.append(Empresa("Alimentação", "    Mix Matheus", "Feira do Mês   ", 900.0,  qualidade=5))
    empresas.append(Empresa("Alimentação", "  Pão de Açúcar", "Feira do Mês   ", 1500.0, qualidade=7))
    empresas.append(Empresa("Alimentação", "      Home Chef", "Chef em Casa   ", 6000.0, qualidade=9))
    empresas.append(Empresa("Transporte",  "  Grande Recife", "VEM  Ônibus    ", 150.0,  qualidade=3))
    empresas.append(Empresa("Transporte",  "           UBER", "Uber Moto      ", 200.0,  qualidade=4))
    empresas.append(Empresa("Transporte",  "             99", "99 Moto        ", 200.0,  qualidade=4))
    empresas.append(Empresa("Transporte",  "            BYD", "BYD Dolphin    ", 3000.0, qualidade=8))
    empresas.append(Empresa("Saúde",       "    Health Coop", "Plano de Saúde ", 200.0,  qualidade=2))
    empresas.append(Empresa("Saúde",       "        HapVida", "Plano de Saúde ", 650.0,  qualidade=5))
    empresas.append(Empresa("Saúde",       " Bradesco Saúde", "Plano de Saúde ", 800.0,  qualidade=5))
    empresas.append(Empresa("Saúde",       "     Sulamérica", "Plano de Saúde ", 850.0,  qualidade=5))
    empresas.append(Empresa("Educação",    "      Escolinha", "Mensalidade    ", 100.0,  qualidade=1))
    empresas.append(Empresa("Educação",    "     Mazzarello", "Mensalidade    ", 1200.0, qualidade=6))
    empresas.append(Empresa("Educação",    "      Arco Íris", "Mensalidade    ", 1800.0, qualidade=8))
    empresas.append(Empresa("Educação",    "Escola do Porto", "Mensalidade    ", 5000.0, qualidade=9))

