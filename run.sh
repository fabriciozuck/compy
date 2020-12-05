#!/usr/bin/env bash

#Criando ambiente virtual
python -m venv venv

#Ativando ambiente virtual
source /venv/bin/activate

#Atualizando o pip
pip install --upgrade pip

#Instalando pacotes do requirements.txt
python -m pip install -r requirements.txt
