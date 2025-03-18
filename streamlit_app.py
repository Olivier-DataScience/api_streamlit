import streamlit as st
import requests
import json

# Titre de l'application
st.title("Prédiction de remboursement de crédit 💰")

# Création des champs de saisie pour les 48 features
CNT_CHILDREN = st.number_input("CNT_CHILDREN", value=0)
CNT_FAM_MEMBERS = st.number_input("CNT_FAM_MEMBERS", value=3)
CODE_GENDER_F = st.selectbox("CODE_GENDER_F (Femme)", [0, 1])
CODE_GENDER_M = st.selectbox("CODE_GENDER_M (Homme)", [0, 1])
FLAG_OWN_CAR_Y = st.selectbox("FLAG_OWN_CAR_Y (Voiture)", [0, 1])
FLAG_OWN_CAR_N = st.selectbox("FLAG_OWN_CAR_N (Pas de voiture)", [0, 1])
FLAG_OWN_REALTY_Y = st.selectbox("FLAG_OWN_REALTY_Y (Propriétaire)", [0, 1])
FLAG_OWN_REALTY_N = st.selectbox("FLAG_OWN_REALTY_N (Locataire)", [0, 1])
NAME_FAMILY_STATUS_Married = st.selectbox("NAME_FAMILY_STATUS_Married (Marié)", [0, 1])
NAME_FAMILY_STATUS_Single_not_married = st.selectbox("NAME_FAMILY_STATUS_Single_not_married (Célibataire)", [0, 1])
NAME_FAMILY_STATUS_Widow = st.selectbox("NAME_FAMILY_STATUS_Widow (Veuf)", [0, 1])
AMT_INCOME_TOTAL = st.number_input("AMT_INCOME_TOTAL (Revenu total)", value=50000)
AMT_CREDIT = st.number_input("AMT_CREDIT (Crédit total)", value=100000)
AMT_ANNUITY = st.number_input("AMT_ANNUITY (Remboursement annuel)", value=25000)
AMT_GOODS_PRICE = st.number_input("AMT_GOODS_PRICE (Prix des biens)", value=200000)
INCOME_CREDIT_PERC = st.number_input("INCOME_CREDIT_PERC (Ratio revenu/crédit)", value=0.5)
ANNUITY_INCOME_PERC = st.number_input("ANNUITY_INCOME_PERC (Ratio remboursement/revenu)", value=0.2)
PAYMENT_RATE = st.number_input("PAYMENT_RATE (Taux de paiement)", value=0.1)
DAYS_BIRTH = st.number_input("DAYS_BIRTH (Âge en jours)", value=-10000)
DAYS_EMPLOYED = st.number_input("DAYS_EMPLOYED (Ancienneté en jours)", value=-5000)
DAYS_EMPLOYED_PERC = st.number_input("DAYS_EMPLOYED_PERC (Ancienneté relative)", value=0.5)
DAYS_REGISTRATION = st.number_input("DAYS_REGISTRATION (Jours depuis l'enregistrement)", value=-2000)
DAYS_ID_PUBLISH = st.number_input("DAYS_ID_PUBLISH (Jours depuis la publication de l'ID)", value=-1000)
NAME_EDUCATION_TYPE_Higher_education = st.selectbox("NAME_EDUCATION_TYPE_Higher_education (Éducation supérieure)", [0, 1])
NAME_EDUCATION_TYPE_Secondary_secondary_special = st.selectbox("NAME_EDUCATION_TYPE_Secondary_secondary_special (Éducation secondaire)", [0, 1])
NAME_EDUCATION_TYPE_Lower_secondary = st.selectbox("NAME_EDUCATION_TYPE_Lower_secondary (Éducation inférieure)", [0, 1])
OCCUPATION_TYPE_Accountants = st.selectbox("OCCUPATION_TYPE_Accountants (Comptable)", [0, 1])
OCCUPATION_TYPE_Core_staff = st.selectbox("OCCUPATION_TYPE_Core_staff (Personnel clé)", [0, 1])
OCCUPATION_TYPE_Laborers = st.selectbox("OCCUPATION_TYPE_Laborers (Travailleurs)", [0, 1])
OCCUPATION_TYPE_Managers = st.selectbox("OCCUPATION_TYPE_Managers (Managers)", [0, 1])
OCCUPATION_TYPE_Sales_staff = st.selectbox("OCCUPATION_TYPE_Sales_staff (Vendeurs)", [0, 1])
EXT_SOURCE_2 = st.number_input("EXT_SOURCE_2 (Source externe 2)", value=0.5)
EXT_SOURCE_3 = st.number_input("EXT_SOURCE_3 (Source externe 3)", value=0.6)
AMT_REQ_CREDIT_BUREAU_YEAR = st.number_input("AMT_REQ_CREDIT_BUREAU_YEAR (Demande de crédit par an)", value=1)
AMT_REQ_CREDIT_BUREAU_MON = st.number_input("AMT_REQ_CREDIT_BUREAU_MON (Demande de crédit par mois)", value=0)
AMT_REQ_CREDIT_BUREAU_QRT = st.number_input("AMT_REQ_CREDIT_BUREAU_QRT (Demande de crédit par trimestre)", value=0)
OBS_30_CNT_SOCIAL_CIRCLE = st.number_input("OBS_30_CNT_SOCIAL_CIRCLE (Circles sociaux 30 jours)", value=3)
DEF_30_CNT_SOCIAL_CIRCLE = st.number_input("DEF_30_CNT_SOCIAL_CIRCLE (Défauts sociaux 30 jours)", value=0)
OBS_60_CNT_SOCIAL_CIRCLE = st.number_input("OBS_60_CNT_SOCIAL_CIRCLE (Circles sociaux 60 jours)", value=5)
DEF_60_CNT_SOCIAL_CIRCLE = st.number_input("DEF_60_CNT_SOCIAL_CIRCLE (Défauts sociaux 60 jours)", value=0)
REGION_POPULATION_RELATIVE = st.number_input("REGION_POPULATION_RELATIVE (Population relative par région)", value=0.02)
REGION_RATING_CLIENT = st.number_input("REGION_RATING_CLIENT (Note région)", value=2)
REGION_RATING_CLIENT_W_CITY = st.number_input("REGION_RATING_CLIENT_W_CITY (Note région avec ville)", value=3)
DAYS_LAST_PHONE_CHANGE = st.number_input("DAYS_LAST_PHONE_CHANGE (Dernier changement de téléphone)", value=-1000)
FLAG_PHONE = st.selectbox("FLAG_PHONE (A un téléphone)", [0, 1])
FLAG_EMAIL = st.selectbox("FLAG_EMAIL (A un email)", [0, 1])
FLAG_EMP_PHONE = st.selectbox("FLAG_EMP_PHONE (A un téléphone professionnel)", [0, 1])
FLAG_WORK_PHONE = st.selectbox("FLAG_WORK_PHONE (A un téléphone professionnel)", [0, 1])

# Création du JSON pour l'API
input_data = {
    "CNT_CHILDREN": CNT_CHILDREN,
    "CNT_FAM_MEMBERS": CNT_FAM_MEMBERS,
    "CODE_GENDER_F": CODE_GENDER_F,
    "CODE_GENDER_M": CODE_GENDER_M,
    "FLAG_OWN_CAR_Y": FLAG_OWN_CAR_Y,
    "FLAG_OWN_CAR_N": FLAG_OWN_CAR_N,
    "FLAG_OWN_REALTY_Y": FLAG_OWN_REALTY_Y,
    "FLAG_OWN_REALTY_N": FLAG_OWN_REALTY_N,
    "NAME_FAMILY_STATUS_Married": NAME_FAMILY_STATUS_Married,
    "NAME_FAMILY_STATUS_Single_not_married": NAME_FAMILY_STATUS_Single_not_married,
    "NAME_FAMILY_STATUS_Widow": NAME_FAMILY_STATUS_Widow,
    "AMT_INCOME_TOTAL": AMT_INCOME_TOTAL,
    "AMT_CREDIT": AMT_CREDIT,
    "AMT_ANNUITY": AMT_ANNUITY,
    "AMT_GOODS_PRICE": AMT_GOODS_PRICE,
    "INCOME_CREDIT_PERC": INCOME_CREDIT_PERC,
    "ANNUITY_INCOME_PERC": ANNUITY_INCOME_PERC,
    "PAYMENT_RATE": PAYMENT_RATE,
    "DAYS_BIRTH": DAYS_BIRTH,
    "DAYS_EMPLOYED": DAYS_EMPLOYED,
    "DAYS_EMPLOYED_PERC": DAYS_EMPLOYED_PERC,
    "DAYS_REGISTRATION": DAYS_REGISTRATION,
    "DAYS_ID_PUBLISH": DAYS_ID_PUBLISH,
    "NAME_EDUCATION_TYPE_Higher_education": NAME_EDUCATION_TYPE_Higher_education,
    "NAME_EDUCATION_TYPE_Secondary_secondary_special": NAME_EDUCATION_TYPE_Secondary_secondary_special,
    "NAME_EDUCATION_TYPE_Lower_secondary": NAME_EDUCATION_TYPE_Lower_secondary,
    "OCCUPATION_TYPE_Accountants": OCCUPATION_TYPE_Accountants,
    "OCCUPATION_TYPE_Core_staff": OCCUPATION_TYPE_Core_staff,
    "OCCUPATION_TYPE_Laborers": OCCUPATION_TYPE_Laborers,
    "OCCUPATION_TYPE_Managers": OCCUPATION_TYPE_Managers,
    "OCCUPATION_TYPE_Sales_staff": OCCUPATION_TYPE_Sales_staff,
    "EXT_SOURCE_2": EXT_SOURCE_2,
    "EXT_SOURCE_3": EXT_SOURCE_3,
    "AMT_REQ_CREDIT_BUREAU_YEAR": AMT_REQ_CREDIT_BUREAU_YEAR,
    "AMT_REQ_CREDIT_BUREAU_MON": AMT_REQ_CREDIT_BUREAU_MON,
    "AMT_REQ_CREDIT_BUREAU_QRT": AMT_REQ_CREDIT_BUREAU_QRT,
    "OBS_30_CNT_SOCIAL_CIRCLE": OBS_30_CNT_SOCIAL_CIRCLE,
    "DEF_30_CNT_SOCIAL_CIRCLE": DEF_30_CNT_SOCIAL_CIRCLE,
    "OBS_60_CNT_SOCIAL_CIRCLE": OBS_60_CNT_SOCIAL_CIRCLE,
    "DEF_60_CNT_SOCIAL_CIRCLE": DEF_60_CNT_SOCIAL_CIRCLE,
    "REGION_POPULATION_RELATIVE": REGION_POPULATION_RELATIVE,
    "REGION_RATING_CLIENT": REGION_RATING_CLIENT,
    "REGION_RATING_CLIENT_W_CITY": REGION_RATING_CLIENT_W_CITY,
    "DAYS_LAST_PHONE_CHANGE": DAYS_LAST_PHONE_CHANGE,
    "FLAG_PHONE": FLAG_PHONE,
    "FLAG_EMAIL": FLAG_EMAIL,
    "FLAG_EMP_PHONE": FLAG_EMP_PHONE,
    "FLAG_WORK_PHONE": FLAG_WORK_PHONE
}

# Envoi de la requête POST à l'API FastAPI
url = "https://mon-api-fastapi-32b9272786a2.herokuapp.com/predict"
response = requests.post(url, json=input_data)

# Affichage du résultat
if response.status_code == 200:
    result = response.json()
    
    prediction = result['prediction']  # 0 ou 1
    probabilite = round(result['probabilité'], 4)

    if prediction == 1:
        st.error(f"Le client risque de ne PAS rembourser")
    else:
        st.success(f"Le client est susceptible de rembourser")
    
    st.info(f"Probabilité associée : {probabilite}")
else:
    st.error("Erreur lors de la requête à l'API")
 
