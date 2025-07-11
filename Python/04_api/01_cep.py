# %%
import requests # para realizar requisicoes na web
import json     # para tratar json de listas/dicionarios para arquivos 
from tqdm import tqdm # serve para mostrar uma barra de carregamento

import pandas as pd

ceps_brasil_numeros = [
    # São Paulo - SP
    "01001000", 
    "01310100",  
    "01414001", 
    "04001000",  
    "05001000",  
    
    # Rio de Janeiro - RJ
    "20010000", 
    "22010000", 
    "22250040",  
    
    # Belo Horizonte - MG
    "30110000",  
    "30310110",  
    
    # Porto Alegre - RS
    "90010000", 
    "90450000", 
    
    # Salvador - BA
    "40010000", 
    "40140110",  
    
    # Recife - PE
    "50010000",  
    "51020000", 
    
    # Brasília - DF
    "70070100", 
    "70297400",  
    
    # Manaus - AM
    "69005040",  
    
    # Fortaleza - CE
    "60010000",  
    "60150000", 
]

dados = []

url = "https://viacep.com.br/ws/{cep}/json/"

for cep in tqdm(ceps_brasil_numeros):
    resposta = requests.get(url.format(cep=cep))
    if resposta.status_code == 200: # verifica se a request foi bem sucedida (codigo 200)
        dados.append(resposta.json())

# %%
dataset = pd.DataFrame(dados)   # coisa linda
dataset.to_csv("ceps.csv", sep=";")

# %%
with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4) # indent=4 é para identar corretamente
    # ensure_ascii=False para ignorar a tabela ascii