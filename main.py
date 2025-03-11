import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px



def stats(dataframe):
    st.header("Data Statistics")
    st.write(dataframe.describe())

def data_header(dataframe):
    st.header("Data Header")
    st.write(dataframe.head())

def plot(dataframe):
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)


def interactive_plot(dataframe):
    x_axis_val = st.selectbox("Select X-Axis value", options = dataframe.columns)
    y_axis_val = st.selectbox("Select Y-Axis value", options = dataframe.columns)
    col = st.color_picker('Select the color of the plot')
 

    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

st.title("Earthquake Data Explorer")
st.text("This is a web app to explore earthquake data.") 

st.sidebar.title("Navigation")
uploaded_file=st.sidebar.file_uploader("Upload Your CSV file here")

options = st.sidebar.radio('Pages', options=[
    'Home', 
    'Data Statistics', 
    'Data Header', 
    'Plot',
    'Interactive Plot'
    ])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
  
if options == "Data Statistics":
    stats(df)
elif options == "Data Header":
    data_header(df)
elif options == "Plot":
    plot(df) 
elif options == "Interactive Plot":
    interactive_plot(df) 