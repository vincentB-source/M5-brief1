import streamlit as st
import requests
from loguru import logger
import json

# URL
API_URL = "http://backend:9000/"

st.header("Calcul de carré")

# Fonction pour tester une phrase
def calcul_carre(nombre):
    try:
        response = requests.post(f"{API_URL}/calcul/", json={"nombre": nombre})
        return response.json()
    # traitement de la réponse
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de connexion à l'API : {e}")
        logger.error(f"Erreur de connexion à l'API : {e}")
    except Exception as e :
        st.error(f"Une erreur est survenue: {e}")
        logger.error(f"Une erreur est survenue: {e}")


with st.form("calcul_form"):
    nombre = st.number_input("Donnez votre nombre !. Exemple : 12")
    submitted = st.form_submit_button("Calculer")
    if submitted:
        result = calcul_carre(nombre)
        st.write(result)
