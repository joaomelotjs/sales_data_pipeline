import pandas as pd
import sqlite3
import os

def generate_report(df):
    resumo_produto = df.groupby('produto')['faturamento'].sum().reset_index()
    resumo_cidade = df.groupby('cidade')['faturamento'].sum().reset_index()

    os.makedirs('output/reports', exist_ok=True)

    with pd.ExcelWriter('output/reports/relatorio.xlsx') as writer:
        df.to_excel(writer, sheet_name='Dados', index=False)
        resumo_produto.to_excel(writer, sheet_name='Produtos', index=False)
        resumo_cidade.to_excel(writer, sheet_name='Cidades', index=False)

def save_to_db(df):
    os.makedirs('database', exist_ok=True)

    conn = sqlite3.connect('database/sales.db')
    df.to_sql('sales', conn, if_exists='replace', index=False)
    conn.close()

    print("Dados salvos no banco com sucesso!")