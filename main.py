import streamlit as st

# 1. SAYFA KONFIGURASYONU
st.set_page_config(
    page_title="Kaggle 20 Competitions Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SAYFA TANIMLAMALARI
home_page = st.Page("pages_config/home.py", title="Ana Sayfa ve Ozet", default=True)

tabular_pages = [
    st.Page("pages_config/comp_01_titanic.py", title="1. Titanic - Machine Learning"),
    st.Page("pages_config/comp_02_house_prices.py", title="2. House Prices - Regression"),
    st.Page("pages_config/comp_03_spaceship_titanic.py", title="3. Spaceship Titanic"),
    st.Page("pages_config/comp_04_water_potability.py", title="4. Water Potability"),
    st.Page("pages_config/comp_05_heart_disease.py", title="5. Heart Disease Prediction"),
    st.Page("pages_config/comp_06_credit_card_fraud.py", title="6. Credit Card Fraud"),
    st.Page("pages_config/comp_07_icr_age_related.py", title="7. ICR - Age-Related Conditions"),
]

nlp_pages = [
    st.Page("pages_config/comp_08_disaster_tweets.py", title="8. Disaster Tweets"),
    st.Page("pages_config/comp_09_rotten_tomatoes.py", title="9. Movie Review Sentiment"),
    st.Page("pages_config/comp_10_feedback_prize.py", title="10. Feedback Prize"),
    st.Page("pages_config/comp_11_commonlit.py", title="11. CommonLit Readability"),
    st.Page("pages_config/comp_12_detect_ai_text.py", title="12. Detect AI Generated Text"),
]

cv_pages = [
    st.Page("pages_config/comp_13_digit_recognizer.py", title="13. Digit Recognizer (MNIST)"),
    st.Page("pages_config/comp_14_aerial_cactus.py", title="14. Aerial Cactus Identification"),
    st.Page("pages_config/comp_15_petfinder_pawpularity.py", title="15. PetFinder Pawpularity"),
    st.Page("pages_config/comp_16_cassava_leaf.py", title="16. Cassava Leaf Disease"),
    st.Page("pages_config/comp_17_dog_breed.py", title="17. Dog Breed Identification"),
]

time_series_pages = [
    st.Page("pages_config/comp_18_store_sales.py", title="18. Store Sales Time Series"),
    st.Page("pages_config/comp_19_m5_forecasting.py", title="19. M5 Forecasting"),
    st.Page("pages_config/comp_20_ventilator_pressure.py", title="20. Ventilator Pressure"),
]

# 3. GEZINTI MENUSU HIYERARSISI
pg = st.navigation(
    {
        "Genel": [home_page],
        "Tablolu Veri (Tabular)": tabular_pages,
        "Dogal Dil Isleme (NLP)": nlp_pages,
        "Bilgisayarli Goru (CV)": cv_pages,
        "Zaman Serisi ve Sinyal": time_series_pages,
    }
)

# 4. YAN MENU
with st.sidebar:
    st.title("Kaggle Portfolio")
    st.caption("20 Kaggle Yarismasi ve Canli Tahminler")
    st.divider()

pg.run()