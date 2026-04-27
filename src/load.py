import pandas as pd

def generate_report(df):
    resumo_produto = df.groupby('produto')['faturamento'].sum().reset_index()
    resumo_cidade = df.groupby('cidade')['faturamento'].sum().reset_index()

    with pd.ExcelWriter('output/reports/relatorio.xlsx') as writer:
        df.to_excel(writer, sheet_name='Dados', index=False)
        resumo_produto.to_excel(writer, sheet_name='Produtos', index=False)
        resumo_cidade.to_excel(writer, sheet_name='Cidades', index=False)