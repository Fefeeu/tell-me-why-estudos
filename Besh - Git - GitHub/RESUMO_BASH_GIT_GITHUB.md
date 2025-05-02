# Comandos BESH

pwd    	-> mostra o diretorio atual

ls         -> mostra todos os arquivos no diretorio atual

cd “”   	-> entra no diretorio referido

# Comandos BESH

### ---------- O BASICO --------

git init .						    -> cria novo repositório git;
git status                     		-> mostra o status da branch atual;
git add nome arquivo            	-> manda arquivo para stage;
git commit -m "minha mensagem"     	-> consolida o checkpoint "commit";
git log                           	-> exibe histórico de commits;
git reset                        	-> retorna para unstage;
git reset idCommit             		-> retorna para pós-commit;


### ---------- BRANCHs ----------

git branch 					-> mostra todas as branchs do projeto
git branch -M nome_da_branch		-> Renomeia a branch que está
git checkout nome_da_branch			-> troca de branch
git checkout -b nome_da_branch		-> cria uma nova branch e troca para ela


### ---------- GITHUB -----------

git push origin nome_branch 		-> envia para a branch remota no GitHub, origin = é o repositorio do git(o link)
git pull

-> A BOA PRATICA DO GIT, E COMO FUINCIONA O CICLO DE TRABALHAR COM O GIT HUB É:
-> 1) cria uma nova branch local
-> 2) envia no final o push da DA BRANCH NOVA!!!
-> 3) faz o pull request 
-> 4) da confirm no pull request, para dar marge com a main
-> 5) da pull da nova main
