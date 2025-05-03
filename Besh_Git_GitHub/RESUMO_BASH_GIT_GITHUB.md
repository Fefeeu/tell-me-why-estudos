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

git <nome_arquivo>           	    -> retira o arquivo do commit

git reset                        	-> retorna para unstage

git reset idCommit             		-> retorna para pós-commit

git diff <nome_arquivo>             -> mostra a diferença do estado atual do arquivo em relação ao commit anterior

MAIS EXEMPLOS DE git add

git add teste_*                     -> vai colocar todos os arquivos que possuem "teste_"

git add *.txt                       -> vai colocar todos os arquivos .txt 

git add *                           -> coloca todos os arquivos, basicamente a mesma coisa que o git add .


### ---------- BRANCHs ----------

git branch 					        -> mostra todas as branchs do projeto

git branch -M <nome_branch>		    -> Renomeia a branch que está para <nome_branch>

git checkout <nome_branch>			-> troca de branch

git checkout -b <nome_branch>		-> cria uma nova branch e troca para ela

git merge <nome_branch>             -> mesca todos os arquivos no ultimo commit da <nome_branch> para  branch que voce está, trazendo junto com todo o historio dos commits

git branch -D <nome_branch>         -> deleta a <nome_branch>, porem para dar o comando nao pode estar na <nome_branch>

### ---------- FORK -------------

-> SEMPRE ANTES DE MEXER É BOM VER SE PRECISA ATUALIZAR O FORK, só abrir o fork que vai estar escrito quantos commits atrasados o seu fork esta

-> é importante que use o comando com a branch sendo: git push origin <nome_branch>

-> quando der o push, é preciso ir no SEU FORK e pedir um pull request

-> e dar o pull request o repositorio que foi "forkado"


### ---------- GITHUB -----------

git push origin <nome_branch> 		-> envia para a <nome_branch> remota no GitHub, origin = é o repositorio do git(o link)

git pull origin <nome_branch>       -> puxa todo a <nome_branch> do github, ou atualiza ele, main puxa a branch main
  
-> A BOA PRATICA DO GIT, E COMO FUINCIONA O CICLO DE TRABALHAR COM O GIT HUB É:

-> 1) cria uma nova branch local

-> 2) envia no final o push da DA BRANCH NOVA!!!

-> 3) faz o pull request 

-> 4) da confirm no pull request, para dar marge com a main

-> 5) da pull da nova main

![](https://i.imgur.com/hDmJgsC.png)

