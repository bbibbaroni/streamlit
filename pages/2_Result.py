import streamlit as st

st.title("Result")

text = '''
---
'''

st.markdown(text)

if 'number' in st.session_state: 
    st.write("학번 : ",st.session_state.number)
if 'name' in st.session_state: 
    st.write("이름 : ", st.session_state.name)

if 'name' in st.session_state: 
    st.write(st.session_state.name,"님의 최종결과는", "점 입니다.")

st