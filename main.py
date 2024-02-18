import streamlit as st
import plotly.express as px
import pandas as pd


st.title('In search for Happiness')
data_x=st.selectbox('Select the data for X-axis',("gdp","happiness","generosity"))
data_y=st.selectbox('Select the data for Y-axis',("gdp","happiness","generosity"))
st.subheader(f"{data_x} and {data_y}")

def get_data(x,y):
    data=pd.read_csv('happy.csv')
    return data[f'{x}'],data[f'{y}']


figure = px.scatter(x=get_data(data_x,data_y)[0],y=get_data(data_x,data_y)[1],labels = {"X":f"{data_x}","Y":f'{data_y}'})
st.plotly_chart(figure,theme="streamlit", use_container_width=True)
