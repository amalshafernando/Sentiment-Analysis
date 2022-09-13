import sys
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt 

st.title("Sentiment Analysis of tweets about US airlines")
st.sidebar.title("Sentiment Analysis of tweets about US airlines")
#markdown is used to decide text down
st.markdown("This application is a streamlit app used to analyze the sentiments  of the tweets ")
st.sidebar.markdown("This application is a streamlit app used to analyze the sentiments  of the tweets:")


DATA_URL = ("tweets.csv")
@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    #converting the data type to date time
    data['tweet_created']=pd.to_datetime(data['tweet_created'])
    return data

data = load_data()  

st.sidebar.subheader('Show random tweet')
random_tweet = st.sidebar.radio('Sentiment Type', ('positive', 'negative', 'neutral'))
st.sidebar.markdown(data.)21:41