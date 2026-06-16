import streamlit as st
from main import country_request

st.title("Countries API Data")

st.text_input("Enter a country name", key="country_name")

if st.button("Get Country Data"):
    country_name = st.session_state.country_name
    data = country_request(country_name)

    if isinstance(data, str):
        st.write(data)
    else:

        country_name = data["data"]["objects"][0]["names"]["common"]
        flag_emoji = data["data"]["objects"][0]["flag"]["emoji"]
        capital_city = data["data"]["objects"][0]["capitals"][0]['name']

        st.write(f'you choose a country: {country_name} {flag_emoji}')
        st.write(f'capital city of {country_name} is: {capital_city}')

        st.write((data))
        st.write(len((data['data']['objects'])))

