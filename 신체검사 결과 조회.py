import streamlit as st
import pandas as pd

# CSV 파일을 읽어옵니다
file_path = '신체검사 결과.csv'
data = pd.read_csv(file_path, encoding='cp949')

# 필요한 열만 선택합니다
data = data[['번호', '이름', '성별', '키(cm)', '체중(kg)', '우 시력', '좌 시력']]

# Streamlit 애플리케이션을 만듭니다
st.title('신체검사 결과 확인')

# 사용자 입력을 받습니다
input_number = st.number_input('번호를 입력하세요', min_value=1, max_value=len(data))
input_name = st.text_input('이름을 입력하세요')
input_gender = st.selectbox('성별을 선택하세요', ['남성', '여성'])

# 사용자 입력과 데이터 비교
matching_row = data[(data['번호'] == input_number) & 
                    (data['이름'] == input_name) & 
                    (data['성별'] == input_gender)]

if not matching_row.empty:
    st.success('정보를 바르게 입력했습니다.')
    row = matching_row.iloc[0]
    st.write(f"키: {row['키(cm)']} cm")
    st.write(f"체중: {row['체중(kg)']} kg")
    st.write(f"우 시력: {row['우 시력']}")
    st.write(f"좌 시력: {row['좌 시력']}")
else:
    st.error('정보가 일치하지 않습니다. 다시 입력하세요.')
