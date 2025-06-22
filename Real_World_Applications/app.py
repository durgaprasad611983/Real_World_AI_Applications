import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import yfinance as yf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import datetime
import os
import requests
from io import BytesIO
import mediapipe as mp
import cv2
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

#******************Class Files****************

from tabs.healthcare import HealthcareTab
from tabs.finance import FinanceTab
from tabs.retail import RetailTab
from tabs.humanresource import HumanResouceTab

#*********************************************

st.set_page_config(page_title="🏨 Real-World AI Applications Demo", layout="wide")

st.markdown("""
    <style>
    .title-box {
        background-color: #48CAE4;
        padding: 30px;
        border: 2px solid #6c757d;
        border-radius: 10px;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #000000;
        margin-bottom: 30px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        width: 100%;
        max-width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    .stRadio > div {
        flex-direction: row !important;
    }
    </style>
    <div class="title-box">
        🏨 Real-World AI Applications Demo (MLops Data Science Implementation)
    </div>
""", unsafe_allow_html=True)

# -------- Spacing between bounding box and menu --------
st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)

# -------- Option menu with appealing colors --------
selected = option_menu(
    menu_title=None,
    options=[
"Healthcare",
"Finance & Banking",
"Retail & E-commerce",
"Human Resource/Recruitment"
    ],
    icons=[
"heart-pulse", "cash-coin", "basket", "car-front-fill", "person-badge-fill"
    ],
    orientation="horizontal",
    default_index=0,
    styles={
"container": {
    "background-color": "#88E788",
    "padding": "10px",
    "border-radius": "10px",
    "box-shadow": "0px 2px 4px rgba(0,0,0,0.1)"
},
"nav-link": {
    "font-size": "14px",
    "font-weight": "500",
    "color": "#000000",
    "padding": "8px 14px",
},
"nav-link-selected": {
    "background-color": "#d0e7ff",
    "color": "#000",
    "font-weight": "bold",
}
    }
)

if selected == "Healthcare":
  section = st.radio(
      label="",
      options=["Cancer Detection", "Hospital Resource Allocation", "ICU Stay Forecasting"],
      index=0,
      horizontal=True

  )

  tab1 = HealthcareTab()

  if section == "Cancer Detection":
      tab1.Cancer_Detection()
  elif section == "Hospital Resource Allocation":
      tab1.Hospital_Resource_Allocation()
  elif section == "ICU Stay Forecasting":
      tab1.ICU_Stay_Forecasting()

elif selected == "Finance & Banking":
  section = st.radio(
      label="",
      options=["Credit Card Fraud Detection", "Risk Scoring", "Portfolio Optimization"],
      index=0,
      horizontal=True

  )

  tab2 = FinanceTab()

  if section == "Credit Card Fraud Detection":
      tab2.Credit_Card_Fraud_Detection()
  elif section == "Risk Scoring":
      tab2.Risk_Scoring()
  elif section == "Portfolio Optimization":
      tab2.Portfolio_Optimization()

elif selected == "Retail & E-commerce":
  section = st.radio(
      label="",
      options=["Personalized Product Recommendations", "Dynamic Pricing", "Visual AI"],
      index=0,
      horizontal=True

  )

  tab3 = RetailTab()

  if section == "Personalized Product Recommendations":
      tab3.Personalized_Product_Recommendations()
  elif section == "Dynamic Pricing":
      tab3.Dynamic_Pricing()
  elif section == "Visual AI":
      tab3.Visual_AI()

elif selected == "Human Resource/Recruitment":
  section = st.radio(
      label="",
      options=["Resume Matching", "Resume Parsing", "Productivity Monitoring"],
      index=0,
      horizontal=True

  )

  tab4 = HumanResouceTab()

  if section == "Resume Matching":
      tab4.Resume_Matching()
  elif section == "Resume Parsing":
      tab4.Resume_Parsing()
  elif section == "Productivity Monitoring":
      tab4.Productivity_Monitoring()      