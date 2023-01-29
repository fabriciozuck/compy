echo "<<<<< Criando ambiente virtual >>>>>"
python -m venv venv

echo "<<<<< Ativando ambiente virtual >>>>>"
source venv/bin/activate

echo "<<<<< Atualizando o pip >>>>>"
pip install --upgrade pip

echo "<<<<< Instalando pacotes do requirements.txt >>>>>"
pip install -r requirements.txt
