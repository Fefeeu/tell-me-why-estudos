# Comandos BESH

CTRL + L    -> arruma o zoom do git bash

pwd                         -> mostra o caminho do diretorio atual

ls                          -> mostra todos os arquivos no diretorio atual

ls -s                       -> + arquivos ocultos

cd <nome_diretorio>         -> entra no diretorio referido

cd ..                       -> volta para o diretorio em que a pasta esta

mkdir <nome_pasta>          -> cria uma nova pasta

rm -rf <nome_pasta>         -> apaga a pasta CUIDADO COM ISSO SE FOR USADO NO C: VAI DELETAR TODOS OS ARQUIVOS DO PC

cat <nome_arquivo>          -> abre visualização do arquivo na bash

nano <nome_arquivo>         -> abre para editar o arquivo na bash, obs.: se usar o nome de um arquivo que nao existe, cria o arquivo

obs.: . significa a propria pasta atual

# Comandos BESH

### ---------- O BASICO --------

git init .						    -> cria novo repositório git

git status                     		-> mostra o status da branch atual

git add <nome_arquivo>            	-> manda arquivo para stage

git commit -m "minha mensagem"     	-> consolida o checkpoint "commit"

git log                           	-> exibe histórico de commits

git reset                        	-> retorna para unstage

git reset idCommit             		-> retorna para pós-commit

MAIS EXEMPLOS DE git add

git add teste_*                     -> vai colocar todos os arquivos que possuem "teste_"

git add *.txt                       -> vai colocar todos os arquivos .txt 

git add *                           -> coloca todos os arquivos, basicamente a mesma coisa que o git add .


### ---------- BRANCHs ----------

git branch 					-> mostra todas as branchs do projeto

git branch -M <nome_branch>		-> Renomeia a branch que está

git checkout <nome_branch>			-> troca de branch

git checkout -b <nome_branch>		-> cria uma nova branch e troca para ela


### ---------- GITHUB -----------

git push origin <nome_branch> 		-> envia para a branch remota no GitHub, origin = é o repositorio do git(o link)

git pull                            -> puxa todo o repositorio do github, ou atualiza ele
  
-> A BOA PRATICA DO GIT, E COMO FUINCIONA O CICLO DE TRABALHAR COM O GIT HUB É:

-> 1) cria uma nova branch local

-> 2) envia no final o push da DA BRANCH NOVA!!!

-> 3) faz o pull request 

-> 4) da confirm no pull request, para dar marge com a main

-> 5) da pull da nova main

![](https://i.imgur.com/hDmJgsC.png)

