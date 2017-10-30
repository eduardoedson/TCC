**************************************
SCP - Sistema de Controle de Pacientes
**************************************

Instalação de dependências
---------------------------------------------------------------
  ``sudo apt-get install python-pip python-dev python3-dev libpq-dev postgresql postgresql-contrib npm curl git vim pgadmin3``
  ``sudo curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -``
  ``sudo apt-get install -y nodejs``
  ``sudo apt-get install -y build-essential``
  ``sudo npm install -g bower``

  ``git clone https://EduardoEdson@bitbucket.org/EduardoEdson/tcc.git``

  Criar banco:
---------------------------------------
* Em outro terminal rode:
  ``sudo su - postgres``
  ``createdb prontuario``
  ``psql``
  ``CREATE USER root WITH PASSWORD 'root';``
  ``GRANT ALL PRIVILEGES ON DATABASE prontuario TO root;``
  ``\q``
  ``exit``

Instalação da virtualenv
------------------------
  ``sudo pip install virtualenvwrapper``
  ``sudo vim ~/.bashrc``
* No final do arquivo adicionar:
  ``export WORKON_HOME=$HOME/.virtualenvs``
  ``source /usr/local/bin/virtualenvwrapper.sh``
* Após fechar rodar:
  ``source ~/.bashrc``

Instalação das dependências do projeto:
---------------------------------------
* Criar uma virtualenv para instalar dependências do projeto:
  ``mkvirtualenv --python=/usr/bin/python3 scp``
* Instalar dependências:
  ``pip install -r requeriments.txt``
  ``./manage.py bower install``

Depedências do banco:
---------------------------------------
  ``./manage.py migrate``

Criar usuário administrador:
---------------------------------------
  ``./manage.py createsuperuser``

Rodando projeto:
---------------------------------------
* Rode:
  ``./manage.py runserver --insecure``
* Acesse no navegador:
  ``localhost:8000``
