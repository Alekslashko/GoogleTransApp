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
    st.write(f'Познайте отговора')
    answer = st.text_input("Опитайте се да познаете отговора")
    if answer == translation:
        st.write(f'{translation} е правилно')
    else:
        st.write(f'Грешно')

