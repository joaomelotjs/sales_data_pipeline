import pandas as pd

def transform_data(df):
    df = df.dropna()
    df['data'] = pd.to_datetime(df['data'])
    df['faturamento'] = df['preco'] * df['quantidade']
    return df