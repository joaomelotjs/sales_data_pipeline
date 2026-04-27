import matplotlib.pyplot as plt

def create_charts(df):
    # faturamento por produto
    produto = df.groupby('produto')['faturamento'].sum()

    plt.figure()
    produto.sort_values().plot(kind='barh')
    plt.title('Faturamento por Produto')
    plt.xlabel('Faturamento')
    plt.tight_layout()
    plt.savefig('output/charts/faturamento_produto.png')
    plt.close()

    # faturamento por cidade
    cidade = df.groupby('cidade')['faturamento'].sum()

    plt.figure()
    cidade.sort_values().plot(kind='barh')
    plt.title('Faturamento por Cidade')
    plt.xlabel('Faturamento')
    plt.tight_layout()
    plt.savefig('output/charts/faturamento_cidade.png')
    plt.close()