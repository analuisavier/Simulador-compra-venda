def simular_pessoa(pessoa, empresas, categorias, percentuais):
    pessoa.conforto = 0
    pessoa.rendimento_mensal = pessoa.salario + (pessoa.patrimonio * 0.05)
    
    gastos_do_mes = 0

    for i, categoria in enumerate(categorias):
        orcamento_categoria = pessoa.rendimento_mensal * percentuais[i]
        
        empresas_da_categoria = [e for e in empresas if e.categoria == categoria and e.oferta > 0]
        if not empresas_da_categoria:
            continue

        compras_possiveis = [e for e in empresas_da_categoria if e.get_preco() <= orcamento_categoria]
        
        compra_realizada = None
        usou_patrimonio_emergencia = False

        if compras_possiveis:
            compra_realizada = max(compras_possiveis, key=lambda e: e.qualidade )
        else:
            mais_barata = min(empresas_da_categoria, key=lambda e: e.get_preco())
            if pessoa.patrimonio >= mais_barata.get_preco():
                compra_realizada = mais_barata
                usou_patrimonio_emergencia = True
        
        if compra_realizada:
            preco = compra_realizada.get_preco()
            
            if usou_patrimonio_emergencia:
                #Sai direto do patrimônio
                pessoa.patrimonio -= preco
            else:
                #Gasto do mês
                gastos_do_mes += preco
            
            pessoa.conforto += compra_realizada.qualidade
            
            compra_realizada.oferta -= 1
            compra_realizada.vendas += 1
            compra_realizada.lucro_total += (preco - compra_realizada.custo)
    
    # No final do mês, o que sobrou do rendimento vira poupança e aumenta o patrimônio
    poupanca = pessoa.rendimento_mensal - gastos_do_mes
    pessoa.patrimonio += poupanca

def simular_empresa(empresa):
    # Se não vendeu nada no mês, aumenta a margem para tentar compensar
    if empresa.vendas == 0:
        empresa.margem += 0.01
    # Se a oferta acabou, aumenta reposição
    if empresa.oferta == 0:
        empresa.reposicao += 1
    # Se a oferta está alta E houve vendas, reduz reposição e margem
    elif empresa.oferta >= 10 and empresa.vendas > 0:
        empresa.reposicao -= 1
        empresa.margem -= 0.01
        if empresa.margem < 0.0:
            empresa.margem = 0

def simular_mercado(pessoas, empresas, categorias, percentuais):
    # 0 Empresas ajustam suas estratégias antes de repor estoque
    for empresa in empresas:
        simular_empresa(empresa)
    # 1 Empresas repõem estoque e zeram as vendas do mês
    for empresa in empresas:
        empresa.oferta += empresa.reposicao
        empresa.vendas = 0
    # 2 Pessoas recebem e gastam
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)