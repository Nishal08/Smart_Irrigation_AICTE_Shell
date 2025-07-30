# 🌿 Smart Irrigation System

An AICTE Shell project Artificial Intelligence and Machine Learning to automate irrigation based on environmental sensor data.

## 📌 Overview

This Smart Irrigation System uses a trained machine learning model to decide whether to turn ON or OFF the water sprinklers based on inputs like soil moisture, temperature, and humidity. The goal is to conserve water and ensure optimal irrigation using real-time data.

## 🛠️ Tech Stack

- **Frontend:** Streamlit (custom styled with `style.css`)
- **Backend:** Python
- **Model:** Pre-trained `.pkl` file
- **Data:** Sample input from `irrigation_machine.csv`
- **UI Configuration:** `.streamlit/config.toml`

## 📁 Files in the Repo

- `app.py` – Main Streamlit web app
- `Farm_Irrigation_System.pkl` – Trained ML model
- `irrigation_machine.csv` – Sample sensor data
- `Irrigation_System.ipynb` – Jupyter notebook for model training & testing
- `style.css` – Custom styling for Streamlit app
- `.streamlit/config.toml` – Theme settings for Streamlit

## ▶️ How to Run

1. Clone the repository:

   git clone https://github.com/Nishal08/Smart_Irrigation_AICTE_Shell.git
   cd Smart_Irrigation_AICTE_Shell

2. Install dependencies:

   pip install -r requirements.txt
   

3. Run the app:

   streamlit run app.py

## 💡 Features

* Interactive sliders to simulate sensor input
* Real-time prediction of sprinkler status (ON/OFF)
* Reset functionality using Streamlit session state
* Visual feedback with intuitive icons and color-coded results

## 📷 Screenshots

<img width="2560" height="1368" alt="Screenshot 2025-07-30 145642" src="https://github.com/user-attachments/assets/6baf946d-e80a-4c41-bc36-181c6dfa5047" />

<img width="2560" height="1368" alt="image" src="https://github.com/user-attachments/assets/5de9de3a-3394-4b4c-87ca-de08f8c99b7f" />




---

Made with 💧 by [Nishal08](https://github.com/Nishal08)


