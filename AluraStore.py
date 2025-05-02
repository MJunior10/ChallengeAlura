import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados das lojas
def carregar_dados():
    urls = [
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
        "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"
    ]
    return [pd.read_csv(url) for url in urls]

# Função para calcular o faturamento por loja
def calcular_faturamento(lojas):
    return {f'Loja{i+1}': loja['Preço'].sum() for i, loja in enumerate(lojas)}

# Função para contar vendas por categoria
def vendas_por_categoria(lojas):
    return {f'Loja{i+1}': loja['Categoria do Produto'].value_counts() for i, loja in enumerate(lojas)}

# Função para calcular média de avaliações
def media_avaliacoes(lojas):
    return {f'Loja{i+1}': loja['Avaliação da compra'].mean().round(2) for i, loja in enumerate(lojas)}

# Função para encontrar os produtos mais e menos vendidos
def produtos_mais_menos_vendidos(lojas):
    mais = {}
    menos = {}
    for i, loja in enumerate(lojas):
        nome = f'Loja{i+1}'
        vendidos = loja['Produto'].value_counts()
        mais[nome] = vendidos.idxmax()
        menos[nome] = vendidos.idxmin()
    return mais, menos

# Função para calcular o frete médio
def calcular_frete_medio(lojas):
    return {f'Loja{i+1}': loja['Frete'].mean().round(2) for i, loja in enumerate(lojas)}

# Função para gerar gráfico de frete médio
def plotar_frete_medio(fretes):
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=list(fretes.keys()), y=list(fretes.values()), marker='o', linestyle='-', color='green')
    plt.title('Frete Médio por Loja')
    plt.ylabel('Frete Médio (R$)')
    plt.xlabel('Lojas')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Função para gerar gráfico de avaliações
def plotar_avaliacoes(avaliacoes):
    plt.figure(figsize=(6, 5))
    sns.barplot(x=list(avaliacoes.keys()), y=list(avaliacoes.values()), palette='pastel')
    plt.title('Média de Avaliação por Loja')
    plt.ylabel('Nota Média')
    plt.xlabel('Lojas')
    plt.ylim(0, 5)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Função para gerar gráfico de faturamento
def plotar_faturamento(faturamento):
    plt.figure(figsize=(8, 5))
    plt.bar(faturamento.keys(), faturamento.values(), color='seagreen')
    plt.title("Faturamento Total por Loja")
    plt.xlabel("Lojas")
    plt.ylabel("Faturamento (R$)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# Função principal para executar tudo
def main():
    lojas = carregar_dados()
    
    faturamento = calcular_faturamento(lojas)
    print("Faturamento por loja:")
    for loja, total in faturamento.items():
        print(f"{loja}: R$ {total:,.2f}")
    
    categorias = vendas_por_categoria(lojas)
    print("\nQuantidade de vendas por categoria em cada loja:")
    for loja, dados in categorias.items():
        print(f"\n{loja}:")
        print(dados)
    
    avaliacoes = media_avaliacoes(lojas)
    print("\nMédia das avaliações por loja:")
    for loja, media in avaliacoes.items():
        print(f"{loja}: {media}")
    
    mais_vendidos, menos_vendidos = produtos_mais_menos_vendidos(lojas)
    print("\nProdutos mais vendidos por loja:")
    for loja, produto in mais_vendidos.items():
        print(f"{loja}: {produto}")
    
    print("\nProdutos menos vendidos por loja:")
    for loja, produto in menos_vendidos.items():
        print(f"{loja}: {produto}")
    
    fretes = calcular_frete_medio(lojas)
    print("\nFrete médio por loja:")
    for loja, frete in fretes.items():
        print(f"{loja}: R$ {frete}")
    
    plotar_frete_medio(fretes)
    plotar_avaliacoes(avaliacoes)
    plotar_faturamento(faturamento)


main()
