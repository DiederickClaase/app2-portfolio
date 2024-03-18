import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Diederick Claase')
    content = """This is where I need to write something about myself"""

    st.info(content)

content2 = """Below you can find some of my applications that I have built in Python. Please feel free to look around"""
st.write(content2)

