# Imports
import streamlit as st
import random
import time
import requests


# Streamlit Page Configuration
st.set_page_config(page_title='Idea Bank', page_icon='💸', layout='centered')

# Web UI
col0, col1, col2 = st.columns([1.5,1.5,4.5], vertical_alignment='center')
with col0:
    st.write()
with col1:
    st.image('icons/atm.png', width=500)
with col2:
    st.title('IDEA BANK')


cola, colb = st.columns([1,55])
with cola:
    st.write()
with colb:
    st.markdown('### 💸 A Bank Full Of **Profitable** Ideas For Every **Hustler** 🤑.')

st.write('')

def money_generater():
    return random.randint(1, 2000)

st.subheader("Quick Cash Generator")
if st.button("Generate Money"):
    st.write("Your Money Is On The way...")
    time.sleep(4)
    amount = money_generater()
    st.success(f"You made ${amount}!")



def fetch_side_hustle():
    try:
        response = requests.get(
            "https://fastapi-api.vercel.app/side_hustles"
        )
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return "Freelancing"

    except:
        return "Something went wrong!"
    
st.write('')

st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.info(idea)


def fetch_money_quote():
    try:
        response = requests.get(
            "https://fastapi-api.vercel.app/money_quotes"
        )
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return "Money is the root of all evil!"
    except:
        return "Something went wrong!"

st.write('')

st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.warning(quote)