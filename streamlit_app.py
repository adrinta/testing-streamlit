import streamlit as st
import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com/python/demopage.htm')

#print the response text (the content of the requested file):
st.write(x.text)


st.title("Streamlit Dashboard Demo")

print("test")