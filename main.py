import streamlit as st
import pandas as pd

# Load the CSV data
file_path = '신체검사 결과(1).csv'
data = pd.read_csv(file_path, encoding='cp949')

# Streamlit app
st.title("신체검사 결과 조회")

# User input
name = st.text_input("이름을 입력하세요:")
gender = st.selectbox("성별을 선택하세요:", ["남성", "여성"])

if st.button("결과 확인"):
    # Check if the entered name and gender match any record in the data
    match = data[(data['이름'] == name) & (data['성별'] == gender)]
    
    if not match.empty:
        st.success("정보를 바르게 입력했습니다.")
        height = match.iloc[0]['키']
        weight = match.iloc[0]['체중']
        st.write(f"키: {height} cm")
        st.write(f"체중: {weight} kg")
    else:
        st.error("정보가 일치하지 않습니다. 다시 입력하세요.")
