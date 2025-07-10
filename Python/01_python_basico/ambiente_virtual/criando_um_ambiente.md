# CRIANDO UM AMBIENTE VIRTUAL NO CONDA

Ambientes virtuais servem para cumprir dependencias de projetos, sem entrar em conflito com outros projetos

```
conda create --name <nome do ambiete> python=3.
```
Obs.: no final o "3." eh somente a vercao do python (nesse caso eh a vercao mais recente do python3), na qual pode ser subistituido por qualquer vercao (Ex.: 3.12.3)

```
conda info --envs
```
Lista os ambientes criados

```
pip install -r requirements.txt
```
Esse comando instala todos os requerimentos que estao listados naquele arquivo