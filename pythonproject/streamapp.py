import streamlit as st
st.title("my first streamlit App")
name=st.text_input("enter name")
if name: st.write(f"Hello,{name}")
num=st.slider("pick number",0,100)
col1,col2 =st.columns(2)
with col1:
    st.write("left side")
with col2:
    st.write("right side")
clicked=st.button("calculator")
agree=st.checkbox("I agree to the terms")
fruit=st.selectbox("Favorite fruits",["Apple","Banana","Mango"])
col1,col2=st.columns(2)
with col1:st.write("left side")