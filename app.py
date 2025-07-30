import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  # Replace with your model file

# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.title("Smart Sprinkler System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# Session state initialization
if "sensor_values" not in st.session_state:
    st.session_state.sensor_values = [0.5] * 20  # Default value

# Reset button
if st.button("🔄 Reset All Sensors"):
    st.session_state.sensor_values = [0.5] * 20

# Collect sensor inputs
sensor_values = []
for i in range(20):
    val = st.slider(
        f"Sensor {i}",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.sensor_values[i],
        step=0.01,
        key=f"sensor_{i}"
    )
    sensor_values.append(val)

# Update state
st.session_state.sensor_values = sensor_values

# Predict button
if st.button("🚀 Predict Sprinklers"):
    with st.spinner("Predicting sprinkler status..."):
        input_array = np.array(sensor_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    for i, status in enumerate(prediction):
        st.markdown(
            f"<div class='prediction'>💧 Sprinkler {i} (parcel_{i}): <strong>{'ON ✅' if status == 1 else 'OFF ❌'}</strong></div>",
            unsafe_allow_html=True
        )

