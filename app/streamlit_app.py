import streamlit as st
import pandas as pd
import numpy as np
import joblib 
import os

model_path = os.path.join('..','models','revenue_model.pkl')
model = joblib.load(model_path)

st.set_page_config(page_title="Movie Revenue Predictor🎬",layout="centered")

st.title("🎬 Movie Revenue Predictor")
st.markdown("Enter movie details to predict revenue (in log scale)")

budget = st.number_input("Budget (in $)", min_value=0,value=10000000)
popularity = st.slider("Popularity",0.0,100.0,50.0)
runtime = st.slider("Runtime (minutes)",30,300,120)
release_month = st.selectbox("Release Month",list(range(1,13)))
release_year = st.slider("Release year",1950,2025,2023)
genre_count = st.slider("Number of genres",1,5,2)

if st.button("Predict Revenue"):
    input_data = pd.DataFrame({
         'log_budget': [np.log1p(budget)],
                'popularity': [popularity],
                'runtime': [runtime],
                'release_month': [release_month],
                'release_year': [release_year],
                'genre_count': [genre_count]
    })
    prediction = model.predict(input_data)[0]
    predicted_revenue = np.expm1(prediction)
    
    st.success(f"💰 Predicted Revenue: **${predicted_revenue:,.2f}**")