def simular_mercado(pessoas, empresas, categorias, percentuais):
    for empresa in empresas:
        simular_empresa(empresa)

    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)
