import streamlit as st
from main import data

st.title("Countries API Data")

country_name = data["data"]["objects"][0]["names"]["common"]
flag_emoji = data["data"]["objects"][0]["flag"]["emoji"]
capital_city = data["data"]["objects"][0]["capitals"][0]['name']

st.write(f'you choose a country: {country_name} {flag_emoji}')
st.write(f'capital city of {country_name} is: {capital_city}')

st.json((data['data']['objects']))
st.write(len((data['data']['objects'])))

