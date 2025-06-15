def simular_pessoa(pessoa, empresas, categorias, percentuais):
    # Zera o conforto do mês e calcula o rendimento
    pessoa.conforto = 0
    pessoa.rendimento_mensal = pessoa.salario + (pessoa.patrimonio * 0.05)
    pessoa.patrimonio += pessoa.salario

    # Itera sobre cada categoria de gasto
    for i, categoria in enumerate(categorias):
        orcamento_categoria = pessoa.rendimento_mensal * percentuais[i]
        
        empresas_da_categoria = [e for e in empresas if e.categoria == categoria and e.oferta > 0]
        if not empresas_da_categoria:
            continue

        # Tenta comprar o de maior qualidade dentro do orçamento
        compras_possiveis = [e for e in empresas_da_categoria if e.get_preco() <= orcamento_categoria]
        
        compra_realizada = None
        if compras_possiveis:
            # Maximiza o conforto
            compra_realizada = max(compras_possiveis, key=lambda e: e.qualidade)
        else:
            # Se não pode pagar com o rendimento, usa o patrimônio para o mais barato
            # para não ficar desamparado
            mais_barata = min(empresas_da_categoria, key=lambda e: e.get_preco())
            if pessoa.patrimonio >= mais_barata.get_preco():
                compra_realizada = mais_barata
        
        # Efetiva a compra
        if compra_realizada:
            preco = compra_realizada.get_preco()
            pessoa.patrimonio -= preco
            pessoa.conforto += compra_realizada.qualidade
            
            compra_realizada.oferta -= 1
            compra_realizada.vendas += 1
            compra_realizada.lucro_total += (preco - compra_realizada.custo)


def simular_empresa(empresa):
    # Ajusta estratégia com base nas vendas do mês
    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01  # Aumenta margem em 1%
    elif empresa.oferta >= 10:
        if empresa.reposicao > 1: # Evita reposição negativa
             empresa.reposicao -= 1
        empresa.margem -= 0.01  # Diminui margem em 1%
        if empresa.margem < 0: # Evita margem negativa
            empresa.margem = 0

def simular_mercado(pessoas, empresas, categorias, percentuais):
    # 1. Empresas repõem o estoque e zeram as vendas do mês
    for empresa in empresas:
        empresa.oferta += empresa.reposicao
        empresa.vendas = 0

    # 2. Pessoas recebem e gastam
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)

    # 3. Empresas ajustam suas estratégias para o próximo mês
    for empresa in empresas:
        simular_empresa(empresa)