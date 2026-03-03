from sqlalchemy import create_engine
from pymongo import MongoClient
import pandas as pd

engine = create_engine("postgresql+psycopg2://admin:admin123@localhost:5432/imobiliaria")
df_proprietarios = pd.read_sql("SELECT * FROM proprietarios", engine)

client = MongoClient("mongodb://localhost:27017/")
db = client["imobiliaria"]

imoveis = list(db.imoveis.find())
df_imoveis = pd.DataFrame(imoveis)

df_imoveis.drop(columns=["_id"], inplace=True)

df_final = df_imoveis.merge(
    df_proprietarios,
    left_on="cpf_proprietario",
    right_on="cpf",
    how="left"
)

def limpar_cpf(cpf):
    return cpf.replace(".", "").replace("-", "")

df_proprietarios["cpf_limpo"] = df_proprietarios["cpf"].apply(limpar_cpf)
df_imoveis["cpf_limpo"] = df_imoveis["cpf_proprietario"].apply(limpar_cpf)

df_final = df_imoveis.merge(
    df_proprietarios,
    on="cpf_limpo",
    how="left"
)

print(df_final.head())