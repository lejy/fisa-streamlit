import streamlit as st

st.title(f"{st.session_state.user1.name}님의 포트폴리오")
if st.session_state.get("user1"):
    st.write(f"현재 사용자: {st.session_state.user1.name}")
    st.write(f"현재 돈: {st.session_state.user1.money:,}원")
else:
    st.write("아직 사용자가 생성되지 않았습니다.")
