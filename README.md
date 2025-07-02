# Config env 

## env virtuel
python -m venv .venv
source .venv/bin/activate

## install package
pip freeze > requirements.txt
pip install -r requirements.txt

# lancement Module

## comparaison des anciens/nouveaux modeles
python main.py

## lancement MLFLOW et sauvegarde MLFLOW
mlflow ui
python main-mlflow.py

## lancer l'api
uvicorn backend/main:app --host 127.0.0.1 --port 9000 --reload

## lancer streamlit (formulaire de prédiction)
streamlit run app.py   

# DOCKER 
## build image 
docker build -t my-python-app . --no-cache

## lancer docker
docker run -p 8000:8000 my-python-app