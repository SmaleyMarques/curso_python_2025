# %%
import requests
import json

# %%

url = "https://viacep.com.br/ws/{cep}/json/"

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
    "26535140",
]

dados = []

from tqdm import tqdm # Demonstra progresso no terminal

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

# %%

with open("data/ceps.json", "w", encoding="utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)