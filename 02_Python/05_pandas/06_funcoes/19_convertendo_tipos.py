# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

df = pd.read_html(url)

uf = df[1]

print(uf.dtypes)

def str_to_flaot(num:str)->float:
    return float(
            num.replace(" ", "").
            replace(",",".").
            replace("\xa0","")
        )

def str_to_int(num:str)->int:
    return int(
            num.replace(" ", "").
            replace("\xa0","")
        )

def str_to_porcentagem(num:str)->float:
    return float(
            num.replace(",",".").
            replace("%","").
            replace("\xa0","")
        )/100

def str_to_pormilhar(num:str)->float:
    return float(
            num.replace(",",".").
            replace("‰","").
            replace("\xa0","")
        )/1000

def str_from_idade_to_float(num:str)->float:
    return float(
            num.replace(" ", "").
            replace(",",".").
            replace("anos", "").
            replace("\xa0","")
        )

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_flaot)

uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_int)

uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_int)

uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_flaot)

uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(str_to_porcentagem)

uf["Mortalidade infantil (2016)"] = uf["Mortalidade infantil (2016)"].apply(str_to_pormilhar)

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(str_from_idade_to_float)

uf.dtypes

# %%
uf

# %%
def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    else:
        return "Escrevi alguma coisa errada"
    
uf["REGIAO"] = uf["Unidade federativa"].apply(uf_to_regiao)

uf

# %%
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (2016)"] < 15 and
            linha["IDH (2010)"] > 700)

uf.apply(classifica_bom, axis=1) # axis=1 quer dizer que esta aplicando na linha

# %%
uf.apply(lambda x: print(x), axis=0)
# %%
uf.apply(lambda x: print(x), axis=1)