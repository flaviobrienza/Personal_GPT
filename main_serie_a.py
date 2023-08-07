import streamlit as st 
from players_openai import get_answer 

st.title('Your Fantasy Football Advisor by Flavio Brienza') 
st.subheader('''This is the first attempt made to create a fantasy football advisor. By providing players' name and surname it will be possibile to obtain some general information about his 2022/2023 season. So far general and shooting stats are included.''')

question = st.text_input('Question:') 

if question:
    answer = get_answer(question) 
    st.text('Answer:')
    st.write(answer)