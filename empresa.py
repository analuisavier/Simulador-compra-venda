class Empresa:
    def __init__(self, categoria, nome, produto, custo, qualidade):
        self.categoria = categoria
        self.nome = nome
        self.produto = produto
        self.custo = float(custo)
        self.qualidade = int(qualidade)
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0
        self.lucro_total = 0.0
        self.meses_sem_venda = 0  

    def get_preco(self):
        return self.custo * (1 + self.margem)