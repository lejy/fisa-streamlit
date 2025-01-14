import streamlit as st

# 검색창 생성
search = st.text_input("검색하실 애니메이션을 입력하세요.")
ani_list = ['짱구는못말려', '몬스터', '릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 검색 조건에 따라 이미지 출력
if search in ani_list[0]:
    st.image(img_list[0])
elif search in ani_list[1]:
    st.image(img_list[1])
elif search in ani_list[2]:
    st.image(img_list[2])
