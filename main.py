import streamlit as st
import pandas as pd

# Load the CSV data
file_path = '신체검사 결과(1).csv'  # Ensure your file is in the same directory as this script
data = pd.read_csv(file_path, encoding='cp949')

st.title("신체검사 결과 조회")

# User input
name = st.text_input("이름을 입력하세요:")
gender = st.selectbox("성별을 선택하세요:", ["남성", "여성"])
password = st.text_input("비밀번호를 입력하세요:", type="password")

if st.button("결과 확인"):
    # Check if the entered name, gender, and password match any record in the data
    match = data[(data['이름'] == name) & (data['성별'] == gender) & (data['비밀번호'] == password)]
    
    if not match.empty:
        st.success("정보를 바르게 입력했습니다.")
        height = match.iloc[0]['키']
        weight = match.iloc[0]['체중']
        st.write(f"키: {height} cm")
        st.write(f"체중: {weight} kg")
    else:
        st.error("정보가 일치하지 않습니다. 다시 입력하세요.")
