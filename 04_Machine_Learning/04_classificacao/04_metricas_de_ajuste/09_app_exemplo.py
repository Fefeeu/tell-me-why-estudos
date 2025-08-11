# RODAR NO TERMINAL <streamlit run .../app.py>

# ta dando alguma coisa errada https://www.youtube.com/watch?v=KjI3xyZEj-w
# %%
import streamlit as st
import pandas as pd

st.markdown("# Descubra a Felicidade")


tempo_atuacao = ['Não atuo', 'De 0 a 6 meses', 'De 6 meses a 1 ano', 
        'De 1 ano a 2 anos', 'de 2 anos a 4 anos', 'Mais de 4 anos']

senioridade = ['Sênior', 'Iniciante', 'Júnior', 'Pleno', 'Gerência',
       'Coordenação', 'Especialista', 'Diretoria', 'C-Level']

redes_sociais = ['LinkedIn', 'Twitch', 'YouTube', 'Instagram', 'Amigos',
       'Twitter / X', 'Outra rede social']

uf = ['MG', 'SC', 'SP', 'CE', 'PE', 'RJ', 'AM', 'PR', 'BA', 'PA', 'MT',
       'RS', 'DF', 'RN', 'ES', 'PB', 'GO', 'MA']
uf.sort()



idade = st.number_input("Sua Idade", min_value=18, max_value=100)

col1, col2, col3 = st.columns(3)

with col1:
    video_games = st.radio("Curte Video Game?", ["Sim", "Não"])
    futebol = st.radio("Curte futebel?", ["Sim", "Não"])
        
    como_conheceu = st.selectbox('Como conheceu o Téo Me Why?', redes_sociais)
    quantos_cursos = st.selectbox('Quantos cursos acompanhou do Téo Me Why?', ['0', '1', '2', '3', 'Mais que 3'])

with col2:
    livro = st.radio("Curte livro?", ["Sim", "Não"])
    tabuleiro = st.radio("Curte Jogos de Tabuleiro?", ["Sim", "Não"])
    
    uf_mora = st.selectbox('Estado que mora atualmente', uf)
    formacao = st.selectbox('Área de Formação', ['Exatas', 'Biológicas', 'Humanas'])

with col3:
    f1 = st.radio("Curte F1?", ["Sim", "Não"])
    MMA = st.radio("Curte MMA?", ["Sim", "Não"])
    
    tempo_na_area = st.selectbox('Tempo que atua na área de dados', tempo_atuacao)
    cadeira = st.selectbox('Posição da cadeira (senioridade)', senioridade)
    

data = {'Como conheceu o Téo Me Why?': como_conheceu,
    'Quantos cursos acompanhou do Téo Me Why?': quantos_cursos,
    'Curte games?': video_games,
    'Curte futebol?': futebol,
    'Curte livros?': livro,
    'Curte jogos de tabuleiro?': tabuleiro,
    'Curte jogos de fórmula 1?': f1,
    'Curte jogos de MMA?': MMA,
    'Idade': idade,
    'Estado que mora atualmente': uf_mora,
    'Área de Formação': formacao,
    'Tempo que atua na área de dados': tempo_na_area,
    'Posição da cadeira (senioridade)': cadeira,
}

df = pd.DataFrame([data])
df = df.replace({"Sim":1, "Não":0})

df_template = pd.DataFrame(columns=['Como conheceu o Téo Me Why?_Amigos',
       'Como conheceu o Téo Me Why?_Instagram',
       'Como conheceu o Téo Me Why?_LinkedIn',
       'Como conheceu o Téo Me Why?_Outra rede social',
       'Como conheceu o Téo Me Why?_Twitch',
       'Como conheceu o Téo Me Why?_Twitter / X',
       'Como conheceu o Téo Me Why?_YouTube',
       'Quantos cursos acompanhou do Téo Me Why?_0',
       'Quantos cursos acompanhou do Téo Me Why?_1',
       'Quantos cursos acompanhou do Téo Me Why?_2',
       'Quantos cursos acompanhou do Téo Me Why?_3',
       'Quantos cursos acompanhou do Téo Me Why?_Mais que 3',
       'Estado que mora atualmente_AM', 'Estado que mora atualmente_BA',
       'Estado que mora atualmente_CE', 'Estado que mora atualmente_DF',
       'Estado que mora atualmente_ES', 'Estado que mora atualmente_GO',
       'Estado que mora atualmente_MA', 'Estado que mora atualmente_MG',
       'Estado que mora atualmente_MT', 'Estado que mora atualmente_PA',
       'Estado que mora atualmente_PB', 'Estado que mora atualmente_PE',
       'Estado que mora atualmente_PR', 'Estado que mora atualmente_RJ',
       'Estado que mora atualmente_RN', 'Estado que mora atualmente_RS',
       'Estado que mora atualmente_SC', 'Estado que mora atualmente_SP',
       'Área de Formação_Biológicas', 'Área de Formação_Exatas',
       'Área de Formação_Humanas',
       'Tempo que atua na área de dados_De 0 a 6 meses',
       'Tempo que atua na área de dados_De 1 ano a 2 anos',
       'Tempo que atua na área de dados_De 6 meses a 1 ano',
       'Tempo que atua na área de dados_Mais de 4 anos',
       'Tempo que atua na área de dados_Não atuo',
       'Tempo que atua na área de dados_de 2 anos a 4 anos',
       'Posição da cadeira (senioridade)_C-Level',
       'Posição da cadeira (senioridade)_Coordenação',
       'Posição da cadeira (senioridade)_Diretoria',
       'Posição da cadeira (senioridade)_Especialista',
       'Posição da cadeira (senioridade)_Gerência',
       'Posição da cadeira (senioridade)_Iniciante',
       'Posição da cadeira (senioridade)_Júnior',
       'Posição da cadeira (senioridade)_Pleno',
       'Posição da cadeira (senioridade)_Sênior', 'Curte games?',
       'Curte futebol?', 'Curte livros?', 'Curte jogos de tabuleiro?',
       'Curte jogos de fórmula 1?', 'Curte jogos de MMA?', 'Idade'
       ])

dummy_vars = [
    'Como conheceu o Téo Me Why?',
    'Quantos cursos acompanhou do Téo Me Why?',
    'Estado que mora atualmente',
    'Área de Formação',
    'Tempo que atua na área de dados',
    'Posição da cadeira (senioridade)'
]

df = pd.get_dummies(df[dummy_vars]).astype(int)

df = pd.concat([df_template, df]).fillna(0)

#   O PROBLEMA ESTA AQUI
model = pd.read_pickle("C:/Users/felip/OneDrive/Desktop/teo_me_why/curso_teo_me_why/04_Machine_Learning/04_classificacao/04_metricas_de_ajuste/01_model_feliz.pkl")
#   O PROBLEMA ESTA AQUI

proba = model["model"].predict_proba(df[model['features']])[:,1][0]

st.data_editor(df)

st.markdown(proba)

if proba > 0.7:
    st.success(f"Voce é uma pessoa FELIZ! Probabilidade: {100*proba:.0f}%")
elif proba > 0.4:
    st.warning(f"Voce é uma pessoa MEDIAMENTE FELIZ! Probabilidade: {100*proba:.0f}%")
elif proba < 0.4:
    st.error(f"Voce é uma pessoa NADA FELIZ! Probabilidade: {100*proba:.0f}%")