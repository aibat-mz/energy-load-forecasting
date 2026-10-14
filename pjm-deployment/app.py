import streamlit as st
import pandas as pd
from xgboost import XGBRegressor

st.set_page_config(page_title="PJM Load Forecast", layout="centered")

@st.cache_resource
def load_model():
    model = XGBRegressor()
    model.load_model("xgboost_model.bin")
    return model

model = load_model()

st.title("PJM Energy Load Forecast (24h ahead)")
st.write("Интерактивное приложение для прогноза электрической нагрузки на **24 часа вперёд**.")

st.subheader("Введите признаки")

col1, col2 = st.columns(2)

with col1:
    hour = st.slider("Hour (0–23)", 0, 23, 12, 1)
    dayofweek = st.selectbox(
        "Day of Week",
        options=list(range(7)),
        format_func=lambda x: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][x]
    )
    month = st.selectbox("Month (1–12)", list(range(1, 13)), index=6)

with col2:
    lag_24 = st.number_input("Load 24 hours ago (MW)", value=30000.0, step=100.0)
    lag_48 = st.number_input("Load 48 hours ago (MW)", value=29500.0, step=100.0)
    lag_144 = st.number_input("Load 144 hours ago (MW)", value=29200.0, step=100.0)
    lag_168 = st.number_input("Load 168 hours ago (MW)", value=29000.0, step=100.0)

if st.button("Predict"):
    X = pd.DataFrame([{
    "hour": hour,
    "dayofweek": dayofweek,
    "month": month,
    "lag_24": lag_24,
    "lag_48": lag_48,
    "lag_144": lag_144,
    "lag_168": lag_168
}])

    pred = float(model.predict(X)[0])

    st.success(f"Forecasted load (t+24): **{pred:,.0f} MW**")
    st.write("Input used:")
    st.dataframe(X)
