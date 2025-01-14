import streamlit as st
import pandas as pd
import numpy as np
# 스트림릿은 그냥 인풋 아웃풋만 담아준다.
# 실제코드는 다른 패키지, 내장 파이썬으로 작성해야함.

# User 클래스 정의
class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def plusmoney(self, a):
        self.money += a

    def minusmoney(self, a):
        self.money -= a


# Session State 초기화
if "user1" not in st.session_state:
    st.session_state.user1 = None  # 초기값은 None

# 사용자 입력
st.title("사용자 생성 및 저장")
user_name = st.text_input("이름", value="", key="name_input")
user_money = st.text_input("돈", value="0", key="money_input")

# 사용자 객체 생성 및 저장
if st.button("사용자 생성"):
    if st.session_state.user1:
        st.warning("이미 생성된 계정입니다.")  # 이미 계정이 있는 경우 경고 메시지 표시
    else:
        try:
            user_money = int(user_money)  # 숫자로 변환 시도
            st.session_state.user1 = User(user_name, user_money)  # 사용자 객체 저장
            st.success(f"사용자 {user_name}이 생성되었습니다! 돈: {user_money:,}원")
        except ValueError:
            st.error("돈은 숫자로 입력해주세요.")  # 숫자로 변환 실패 시 오류 메시지 표시
                

# 사용자 정보 표시
if st.session_state.user1:
    pass

    # df = pd.DataFrame(
    #     [
    #     {"command": "st.selectbox", "rating": 4, "is_widget": True},
    #     {"command": "st.balloons", "rating": 5, "is_widget": False},
    #     {"command": "st.time_input", "rating": 3, "is_widget": True},
    # ]
    # )

    # ani_list = ['짱구는못말려', '몬스터','릭앤모티']
    # img_list = ['https://i.imgur.com/t2ewhfH.png', 
    #             'https://i.imgur.com/ECROFMC.png', 
    #             'https://i.imgur.com/MDKQoDc.jpg']

    # data = './README.md'
    # url = 'https://naver.com'
    # def foo():
    #     print('abc')
    # def b():
    #     pass
    # slider_val = None

    # st.button("클릭 미")
    # st.download_button("Download file", data)
    # st.link_button("Go to gallery", url)
    # st.page_link("pages/app2.py", label="Home")
    # st.data_editor(df)
    # st.checkbox("I agree")
    # st.feedback("thumbs")
    # st.pills("Tags", ["Sports", "Politics"])
    # st.radio("Pick one", ["cats", "dogs"])
    # st.segmented_control("Filter", ["Open", "Closed"])
    # st.toggle("Enable")
    # st.selectbox("Pick one", ["cats", "dogs"])
    # st.multiselect("Buy", ["milk", "apples", "potatoes"])
    # st.slider("Pick a number", 0, 100)
    # st.select_slider("Pick a size", ["S", "M", "L"])
    # st.text_input("First name")
    # st.number_input("Pick a number", 0, 10)
    # st.text_area("Text to translate")
    # st.date_input("Your birthday")
    # st.time_input("Meeting time")
    # st.file_uploader("Upload a CSV")
    # st.audio_input("Record a voice message")
    # st.camera_input("Take a picture")
    # st.color_picker("Pick a color")

    # # Use widgets' returned values in variables:
    # for i in range(int(st.number_input("Num:"))):
    #     foo()
    # if st.sidebar.selectbox("I:",["f"]) == "f":
    #     b()

    # # my_slider_val2 = st.slidebar.slider("Quinn")
    # # st.slidebar.write(my_slider_val2)

    # my_slider_val = st.slider("Quinn Mallory", 1, 88)
    # st.write(my_slider_val)

