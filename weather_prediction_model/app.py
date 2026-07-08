# ==========================================================
# AI Weather Predictor
# Developed by UNISOLE AI Labs
# ==========================================================

import streamlit as st
import joblib
import pandas as pd

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="AI Weather Predictor",
    page_icon="🌦️",
    layout="centered"
)

# ==========================================================
# Load Trained Model
# ==========================================================

model = joblib.load("rain_model.pkl")

# ==========================================================
# Title
# ==========================================================

st.title("🌦️ AI Weather Predictor")

st.markdown(
    """
Predict **whether it will rain tomorrow** using a Machine Learning model.

This project is built using:

- 🐍 Python
- 📊 Pandas
- 🤖 Scikit-Learn
- 🎈 Streamlit
"""
)

st.divider()

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("About")

st.sidebar.info(
    """
This AI model predicts whether it will rain tomorrow based on:

- 🌡️ Maximum Temperature
- 💧 Humidity
- 💨 Wind Speed

Created by students using Machine Learning.
"""
)

# ==========================================================
# User Inputs
# ==========================================================

st.header("Enter Today's Weather")

temperature = st.slider(
    "🌡️ Maximum Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    value=25.0
)

humidity = st.slider(
    "💧 Humidity at 3 PM (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

wind = st.slider(
    "💨 Wind Speed (km/h)",
    min_value=0.0,
    max_value=100.0,
    value=15.0
)

st.divider()

# ==========================================================
# Show Entered Values
# ==========================================================

st.subheader("Today's Weather")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperature", f"{temperature:.1f}°C")

with col2:
    st.metric("💧 Humidity", f"{humidity:.1f}%")

with col3:
    st.metric("💨 Wind Speed", f"{wind:.1f} km/h")

st.divider()

# ==========================================================
# Prediction Button
# ==========================================================

if st.button("🔍 Predict Weather", use_container_width=True):

    # Prepare Input
    input_data = pd.DataFrame(
        {
            "MaxTemp": [temperature],
            "Humidity3pm": [humidity],
            "WindSpeed3pm": [wind]
        }
    )

    # Prediction
    prediction = model.predict(input_data)[0]

    # Prediction Probability
    probability = model.predict_proba(input_data)

    confidence = max(probability[0]) * 100

    st.subheader("AI Prediction")

    if prediction == "Yes":

        st.error("🌧️ Rain Expected Tomorrow")

        st.progress(confidence / 100)

        st.write(f"### Confidence : {confidence:.2f}%")

        st.info("☂️ Carry an Umbrella")

        st.info("🚗 Drive Carefully")

        st.info("🌾 Farmers should plan field activities accordingly.")

        st.balloons()

    else:

        st.success("☀️ No Rain Expected")

        st.progress(confidence / 100)

        st.write(f"### Confidence : {confidence:.2f}%")

        st.info("😎 Enjoy Outdoor Activities")

        st.info("🏏 Great Weather for Sports")

        st.info("🚶 Good Day for Travelling")

st.divider()

# ==========================================================
# How AI Works
# ==========================================================

with st.expander("🧠 How does this AI work?"):

    st.write("""
This AI follows five simple steps:

1️⃣ Collect historical weather data

2️⃣ Learn patterns from the data

3️⃣ Build a Machine Learning model

4️⃣ Compare today's weather with past patterns

5️⃣ Predict whether it may rain tomorrow

Remember:

**AI does not guess.**

It learns patterns from data.
""")

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.markdown(
"""
### 👨‍💻 Developed By

**UNISOLE AI Labs**

Empowering students with Artificial Intelligence and Machine Learning.

Made with ❤️ using Python, Scikit-Learn and Streamlit.
"""
)