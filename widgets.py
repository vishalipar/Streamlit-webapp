import streamlit as st 
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:" ,0,100,25)

st.write(f"Your age is {age}.")

options = ['Python', 'Java', 'C++', 'Javascript']
choices = st.selectbox("Choose your favourite Language: ", options)
st.write(f"Your favourite language is {choices}")

if name:
    st.write(f"Hello , {name}")
    
data = {
    "Name":["Vishal","Ram", "Sham","Vedant"],
    "Age":[21,24,43,22],
    "City":["Nandgaon", "Nashik","Yeola","Manmad"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)