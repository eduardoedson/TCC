Manual de Instalação
====================

Introdução
----------
Este manual foi feito para a instalação do sistema Prontuário Único UCB feito como projeto final do curso de Ciência da Computação. Essa instalação foi testada usando um sistema operacional Linux, mais especificamente <a href="https://www.ubuntu.com/desktop/1710">Ubuntu 17.10</a>, podendo ocorrer divergências em outras distribuições e sistemas operacionais.

Instalação das dependências do sistema
--------------------------------------
Abra um terminal com o comando `Ctrl+Alt+T` e cole os seguintes comandos:
```
sudo apt-get install -y python-pip python-dev python3-dev libpq-dev postgresql postgresql-contrib npm curl git vim pgadmin3
sudo curl -sL https://deb.nodesource.com/setup_7.x
sudo apt-get install -y nodejs build-essential
sudo npm install -g bower
```
Após concluir todas essas instalações, as dependências do sistema operacional foram atendidas.

Baixar o projeto
----------------
O projeto se encontra disponível no GitHub, então para poder baixá-lo é necessário rodar o seguinte comando no terminal:
```
git clone htpps://github.com/eduardoedson/TCC.git
```

Criar Banco de Dados
--------------------
Primeiro é necessário entrar no terminal do postgresql:
```
sudo su - postgres
createdb prontuario
psql
CREATE USER root WITH PASSWORD 'root';
GRANT ALL PRIVILEGES ON DATABASE prontuario TO root;
\q
exit
```

Instalar Virtualenv
-------------------
A virtualenv será usada para instalar as dependências do projeto sem prejudicar as instalações do sistema operacional ou de outros projetos.
```
sudo pip install virtualenvwrapper
```
Agora é preciso abrir o arquivo `bashrc`
```
sudo vim ~/.bashrc
```
e adicionar as seguinter linhas no final do arquivo:
```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
agora para fechar o arquivo é necessário pressionar `ESC` e digitar `:wq` <br />
depois é necessário recarregar o arquivo digitando:
```
source ~/.bashrc
```
Para criar um virtualenv será necessário o seguinte comando:
```
mkvirtualenv --python=/usr/bin/python3 prontuario
```

Dependências do Projeto
-----------------------
Dentro da virtualenv, é necessário ir até a pasta do projeto:
```
cd /TCC/django_project
```
Agora serão instaladas as dependências do projeto:
```
pip install -r requeriments.txt
./mana ge.py bower install
./manage.py migrate
```

Rodar o Sistema
---------------

Para rodar o sistema basta usar o seguinte comando:
```
./manage.py runserver
```

Acessando o Sistema
-------------------
```
http://localhost:8000
```
