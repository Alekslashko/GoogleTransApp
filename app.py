import streamlit as st
from googletrans import Translator

# Заглавие
st.title('Приложение за превод на текст')

# Входен текст
text = st.text_input("Въведете текст за превод:")

# Избор на език
language = st.selectbox("Изберете език за превод", ["en", "fr", "de", "it", "es"])

# Превод
if text:
    translator = Translator()
    translation = translator.translate(text, dest=language)
    answer = st.text_input("Опитайте се да познаете отговора")
    if answer == translation.text:
        st.write(f'Правилно')
    else:
        st.write(f'Грешно')

