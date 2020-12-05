#!/usr/bin/env bash

echo " Criando ambiente virtual >>>>>"
python -m venv venv

echo ""
echo "<<<<< Ativando ambiente virtual >>>>>"
source venv/bin/activate

echo ""
echo "<<<<< Atualizando o pip >>>>>"
pip install --upgrade pip

echo ""
echo "<<<<< Instalando pacotes do requirements.txt >>>>>"
python -m pip install -r requirements.txt
