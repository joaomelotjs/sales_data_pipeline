# 📊 Sales Data Pipeline

Este pipeline simula o processamento de dados de vendas de uma empresa,
automatizando a ingestão, transformação e geração de insights para apoio à decisão.

---

## 🚀 Tecnologias utilizadas

- Python
- Pandas
- SQLite
- Matplotlib

---

## 📂 Estrutura do projeto

- `data/raw` → dados brutos (CSV)
- `src/` → scripts de ETL (extract, transform, load)
- `database/` → banco de dados SQLite
- `output/reports` → relatórios gerados
- `output/charts` → gráficos

---

## 📊 Resultados

### Faturamento por Produto
![Faturamento por Produto](output/charts/faturamento_produto.png)

### Faturamento por Cidade
![Faturamento por Cidade](output/charts/faturamento_cidade.png)

---

## 📌 Objetivo

Este projeto demonstra habilidades práticas em:

1. Extração de arquivos CSV
2. Transformação e limpeza dos dados
3. Armazenamento em banco SQLite
4. Geração de relatórios em Excel
5. Criação de visualizações gráficas

---

## ▶️ Como executar o projeto

1. Clone o repositório:

git clone https://github.com/joaomelotjs/sales_data_pipeline.git

2. Acesse a pasta do projeto:

cd sales_data_pipeline

3. Crie um ambiente virtual:

python -m venv venv

4. Ative o ambiente:

Windows:
venv\Scripts\activate

5. Instale as dependências:

pip install -r requirements.txt

6. Execute o pipeline:

python -m src.pipeline
