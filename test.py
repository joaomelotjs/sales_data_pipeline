from src.extract import load_data
from src.transform import transform_data
from src.database import save_to_db
from src.load import generate_report
from src.visualize import create_charts

print("Rodando...")

df = load_data('data/raw')
df = transform_data(df)

save_to_db(df)
generate_report(df)
create_charts(df)

print(df.head())
print("Total de linhas:", len(df))