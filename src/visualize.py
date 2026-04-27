import matplotlib.pyplot as plt

def generate_charts(df):
    # Faturamento por produto
    df.groupby('produto')['faturamento'].sum().plot(kind='bar')
    plt.title('Faturamento por Produto')
    plt.savefig('output/charts/faturamento_produto.png')
    plt.clf()

    # Faturamento por cidade
    df.groupby('cidade')['faturamento'].sum().plot(kind='bar')
    plt.title('Faturamento por Cidade')
    plt.savefig('output/charts/faturamento_cidade.png')
    plt.clf()

    print("Gráficos gerados com sucesso!")