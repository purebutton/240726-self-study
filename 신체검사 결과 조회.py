import streamlit as st
import pandas as pd

# Load the data
file_path = 'path_to_your_file/신체검사 결과(1).csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# Function to validate user input
def validate_user(name, gender):
    user_data = data[(data['이름'] == name) & (data['성별'] == gender)]
    if not user_data.empty:
        st.success('정보를 바르게 입력했습니다.')
        st.write(user_data[['키', '체중']])
    else:
        st.error('정보가 일치하지 않습니다. 다시 입력하세요.')

# Streamlit app layout
st.title('신체검사 결과 확인')
name = st.text_input('이름을 입력하세요:')
gender = st.selectbox('성별을 선택하세요:', options=['남', '여'])

if st.button('확인'):
    validate_user(name, gender)

