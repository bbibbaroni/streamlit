import streamlit as st

st.title("Number nmd Name")
text = '''
---
'''
blank = '''

'''

st.markdown(text)
st.markdown(blank)
st.markdown(blank)
st.markdown(blank)

Number = st.number_input("학번", value=None, placeholder="Type your number...")
st.write("당신의 학번은", Number, "입니다")

st.session_state.number = Number

st.markdown(blank)
st.markdown(blank)
Name = st.text_input("이름", value=None, placeholder="Type your n name...")
st.write("당신의 이름 : ", Name)

st.session_state.name = Name

