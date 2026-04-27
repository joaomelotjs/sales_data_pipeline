from src.extract import load_data
from src.transform import transform_data
from src.load import save_to_db, generate_report
from src.visualize import generate_charts

def run_pipeline():
    print("🚀 Iniciando pipeline...")

    # Extract
    df = load_data('data/raw')

    # Transform
    df = transform_data(df)

    # Load
    save_to_db(df)

    # Report
    generate_report(df)

    # Visualização
    generate_charts(df)

    print("✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()