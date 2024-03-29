import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col2:
    st.image("images/photo4.png")

with col1:
    st.title('Diederick Claase')
    content = """This is where I need to write something about myself, so let me write something about myself.
    Wel, I am trying to learn how to write some Python Code, enrolled on Udemy for a Course and want to learn
    more about coding. Wish me LUCK!!"""
    st.info(content)

content2 = """Below you can find some of my applications that I have built in Python. Please feel free to look around"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")