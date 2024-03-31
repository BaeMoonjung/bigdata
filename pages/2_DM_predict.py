import streamlit as st
import joblib
import numpy as np

model = joblib.load('dm_model.pkl')
scaler = joblib.load('dm_scaler.pkl')

st.title("당뇨 예측 모델")

height = st.number_input('키를 입력하세요(cm).')
weight = st.number_input('몸무게를 입력하시오(kg)')
smoke = st.number_input('흡연 여부를 입력하세요. 비흡연이면 0, 흡연자이면 1을 입력하세요.')
sex = st.number_input('성별을 입력하세요. 여자면 0, 남자면 1을 입력하세요.')
age = st.number_input('나이를 입력하시오.')
exercise = st.number_input('지난 30일 이내에 직업 이외에 숨치 찰 정도의 운동을 규칙적으로 하였습니까? 하지 않았으면 0, 하였으면 1을 입력 하세요.')

bmi = 0

if height != 0:
    bmi = weight/(height/100)**2

if 18 <= age < 25:
    age_calc = 1
elif 25 <= age < 30:
    age_calc = 2
elif 30 <= age < 35:
    age_calc = 3
elif 35 <= age < 40:
    age_calc = 4
elif 40 <= age < 45:
    age_calc = 5
elif 45 <= age < 50:
    age_calc = 6
elif 50 <= age < 55:
    age_calc = 7
elif 55 <= age < 60:
    age_calc = 8
elif 60 <= age < 65:
    age_calc = 9
elif 65 <= age < 70:
    age_calc = 10
elif 70 <= age < 75:
    age_calc = 11
elif 75 <= age < 80:
    age_calc = 12
elif 80 <= age:
    age_calc = 13
else:
    age_calc = 1

my_array = np.array([bmi, smoke, sex, age_calc, exercise])
my_array = my_array.reshape(-1, 5)

my_scaled_array = scaler.transform(my_array)

my_result = model.predict(my_scaled_array)

if my_result == 0:
    final_result = '정상일 가능성이 높습니다.'
elif my_result == 1:
    final_result = '당뇨 전단계 가능성이 있습니다. 병원에서 검사를 받아보시길 바랍니다.'
elif my_result == 2:
    final_result = '당뇨 가능성이 있습니다. 병원에서 검사를 받아 보시길 바랍니다.'

result = st.button('결과보기')
if result:
    st.write(final_result)