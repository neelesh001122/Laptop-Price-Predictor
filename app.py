import streamlit as st
import pickle
import numpy as np

# Model aur dataframe load karna
try:
    pipe = pickle.load(open('pipe.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
except Exception as e:
    st.error("Model files load karne mein dikkat hui. Please check karein ki pipe.pkl aur df.pkl present hain.")

st.title("💻 Laptop Price Predictor")
st.write("Apni pasand ki configuration select karein aur laptop ka estimated price jaanein.")

st.divider()

# Layout ko organize karne ke liye columns ka use
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('Brand', df['Company'].unique())
    type = st.selectbox('Type', df['TypeName'].unique())
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64], index=3)
    weight = st.number_input('Weight of Laptop (in kg)', min_value=0.5, max_value=5.0, value=1.5, step=0.1)
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('IPS Display', ['No', 'Yes'])

with col2:
    # Screen Size ke liye standard options
    screen_size = st.selectbox('Screen Size (in inches)', [11.6, 12.5, 13.3, 14.0, 15.6, 16.0, 17.3], index=4)
    resolution = st.selectbox('Screen Resolution', [
        '1920x1080', '1366x768', '1600x900', '3840x2160', 
        '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
    ])
    cpu = st.selectbox('CPU Brand', df['Cpu Brand'].unique())
    hdd = st.selectbox('HDD Storage (in GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('SSD Storage (in GB)', [0, 8, 128, 256, 512, 1024], index=3)
    gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())
    os = st.selectbox('Operating System', df['os'].unique())

st.divider()

if st.button('Predict Price', use_container_width=True):
    try:
        # Binary encoding
        touchscreen_val = 1 if touchscreen == 'Yes' else 0
        ips_val = 1 if ips == 'Yes' else 0

        # Screen resolution splits
        X_Res = int(resolution.split('x')[0])
        Y_Res = int(resolution.split('x')[1])

        # PPI calculation with check
        if screen_size <= 0:
            st.warning("Screen size 0 se bada hona chahiye.")
        else:
            PPI = (((X_Res ** 2) + (Y_Res ** 2)) ** 0.5) / screen_size

            # Input feature array
            query = np.array([company, type, ram, weight, touchscreen_val, ips_val, PPI, cpu, hdd, ssd, gpu, os])
            query = query.reshape(1, 12)

            # Prediction
            predicted_log_price = pipe.predict(query)[0]
            predicted_price = int(np.exp(predicted_log_price))

            st.success(f"### Estimated Price: ₹ {predicted_price:,}")

    except Exception as err:
        st.error(f"Prediction karne mein error aaya: {err}")
