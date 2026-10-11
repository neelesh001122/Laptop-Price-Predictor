import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Laptop Price Predictor Pro",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Professional UI
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .stButton>button {
            width: 100%;
            background: linear-gradient(135deg, #1f77b4 0%, #2ca02c 100%);
            color: white;
            font-size: 18px;
            font-weight: bold;
            height: 3em;
            border-radius: 10px;
            border: none;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #135d8e 0%, #228b22 100%);
            color: #ffffff;
        }
        h1 {
            color: #ffffff;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
        }
    </style>
""", unsafe_allow_html=True)

# Load Model and Data
@st.cache_resource
def load_data():
    pipe = pickle.load(open('pipe.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
    return pipe, df

try:
    pipe, df = load_data()
except Exception as e:
    st.error(f"Error loading model files: {e}")

# App Header
st.markdown("<h1 style='text-align: center;'>💻 Professional Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a3a3a3; font-size: 16px;'>Configure your desired laptop specifications below to instantly estimate market price with high precision.</p>", unsafe_allow_html=True)
st.divider()

# Symmetric 3-Column Layout
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("### ⚙️ General Specs")
    company = st.selectbox('Brand', sorted(df['Company'].unique()))
    
    # Dynamic OS filtering based on brand
    if company == 'Apple':
        os_options = [o for o in df['os'].unique() if 'mac' in o.lower() or 'ios' in o.lower()]
        if not os_options:
            os_options = ['macOS']
        os = st.selectbox('Operating System', os_options)
    else:
        os_options = [o for o in df['os'].unique() if 'mac' not in o.lower() and 'ios' not in o.lower()]
        os = st.selectbox('Operating System', os_options)
        
    type = st.selectbox('Laptop Type', sorted(df['TypeName'].unique()))
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64], index=3)

with col2:
    st.markdown("### 🖥️ Display & Build")
    screen_size = st.selectbox('Screen Size (in inches)', [11.6, 12.5, 13.3, 14.0, 15.6, 16.0, 17.3], index=4)
    resolution = st.selectbox('Screen Resolution', [
        '1920x1080', '1366x768', '1600x900', '3840x2160', 
        '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
    ])
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('IPS Display', ['No', 'Yes'])
    weight = st.selectbox('Weight (in kg)', [1.0, 1.2, 1.3, 1.4, 1.5, 1.8, 2.0, 2.2, 2.5, 3.0], index=4)

with col3:
    st.markdown("### ⚡ Performance & Storage")
    cpu = st.selectbox('CPU Brand', sorted(df['Cpu Brand'].unique()))
    gpu = st.selectbox('GPU Brand', sorted(df['Gpu brand'].unique()))
    ssd = st.selectbox('SSD Storage (in GB)', [0, 8, 128, 256, 512, 1024], index=3)
    hdd = st.selectbox('HDD Storage (in GB)', [0, 128, 256, 512, 1024, 2048])

st.divider()

# Centered Predict Button
col_space1, col_btn, col_space2 = st.columns([1, 2, 1])
with col_btn:
    predict_clicked = st.button('Predict Laptop Price')

if predict_clicked:
    try:
        touchscreen_val = 1 if touchscreen == 'Yes' else 0
        ips_val = 1 if ips == 'Yes' else 0

        X_Res = int(resolution.split('x')[0])
        Y_Res = int(resolution.split('x')[1])

        if screen_size <= 0:
            st.error("Screen size must be greater than 0.")
        else:
            PPI = (((X_Res ** 2) + (Y_Res ** 2)) ** 0.5) / screen_size

            # Match exact column order and names used during training
            query_df = pd.DataFrame([[company, type, ram, weight, touchscreen_val, ips_val, PPI, cpu, hdd, ssd, gpu, os]],
                                    columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'PPI', 'Cpu Brand', 'HDD', 'SSD', 'Gpu brand', 'os'])

            predicted_log_price = pipe.predict(query_df)[0]
            predicted_price = int(np.exp(predicted_log_price))

            st.success(f"### 🎉 Estimated Market Price: ₹ {predicted_price:,}")

    except Exception as err:
        st.error(f"An error occurred during prediction: {err}")