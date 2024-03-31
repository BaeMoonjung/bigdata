import streamlit as st
import pandas as pd
import random
from string import ascii_uppercase

st.set_page_config(
    page_title= "의료 빅테이터 분석",
    layout="wide",
)

alphabet_list = list(ascii_uppercase)

def convert_df(df):
    return df.to_csv().encode('cp949')

st.title("무작위 배정하기")

seed_n = st.number_input("임의의 숫자 9자리를 입력하세요:")
participant_n = st.number_input("시험 대상자 수를 입력하시오:")
group_n = st.number_input("시험 그룹 수를 입력하시오:")
paralle1 = st.number_input("직렬 투약인 경우 1, 병렬 투약인 경우 2를 입력하시오:")

# 무작위 배정 번호 생성

randomization_n=[]
randomization_group = []  

# 직렬인 경우 무작위 번호 생성

if paralle1 == 1:
    for i in range(int(participant_n)):
        s = "R" + str(1001+i)
        randomization_n.append(s)    

    # 시험군 수에 따른 그룹 설정    

    for i in range(int(group_n)):
        g = alphabet_list[i]
        randomization_group.append(g)

    randomization_group = randomization_group*int(participant_n/group_n)

    # 무작위 배정

    random.seed(seed_n)
    random.shuffle(randomization_group)

    df = pd.DataFrame({"무작위 번호":randomization_n, "투여군": randomization_group})

    result = st.button('결과보기')
    if result:
        st.write(df)

    df1 = convert_df(df)
    st.download_button(
        label="Download data as CSV",
        data=df1,
        file_name='large_df.csv',
        mime='text/csv',
    )

# 병렬인 경우 무작위 번호 생성       

if paralle1 == 2:
    for i in range(int(participant_n/2)):
        s = "R" + str(1001+i)
        randomization_n.append(s)
    for i in range(int(participant_n/2)):
        s = "R" + str(2001+i)
        randomization_n.append(s)

    # 시험군 수에 따른 그룹 설정          

    for i in range(int(group_n)):
        g = alphabet_list[i]
        randomization_group.append(g)

    randomization_group = randomization_group*int(participant_n/group_n)

    # 무작위 배정

    random.seed(seed_n)
    random.shuffle(randomization_group)

    df = pd.DataFrame({"무작위 번호":randomization_n, "투여군": randomization_group})

    result = st.button('결과보기')
    if result:
        st.write(df)

    df1 = convert_df(df)
    st.download_button(
        label="Download data as CSV",
        data=df1,
        file_name='randomization.csv',
        mime='text/csv',
    )