import streamlit as st

st.title("Quiz")

if 'number' in st.session_state: 
    st.markdown(st.session_state.number)
if 'name' in st.session_state: 
    st.markdown(st.session_state.name)



text = '''
---
'''

st.markdown(text)

genre = st.radio(
    "1 . 다음중 최정혁의 생일로 옳은 것은? (2점)",
    ["08/12", "04/19", "12/25", "08/29", "02/08"],
    index=None,
)
st.write("You selected:",genre)

score =+ 2 if genre == "08/29" else 0

st.markdown(text)

st.write('2 . 다음은 최정혁의 발언이다. 빈칸에 들어갈 말을 작성하시오. (4점)')

st.write('P가 철철의 반댓 말은? 인이 (ㅤㅤㅤㅤ) ㅋㅋㅋㅋ')
answer = st.text_input("",value=None, placeholder="Type your answer...")
st.write("당신의 답 : ",answer)
