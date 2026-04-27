import pandas as pd
import os

def load_data(path):
    files = [f for f in os.listdir(path) if f.endswith('.csv')]

    if not files:
        raise Exception("Nenhum arquivo CSV encontrado")

    df_list = []

    for file in files:
        full_path = os.path.join(path, file)
        df = pd.read_csv(full_path)
        df_list.append(df)

    return pd.concat(df_list, ignore_index=True)
print("extract carregado")