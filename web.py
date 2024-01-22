import streamlit as st
from functions import get_compliment_line, get_oracle_line, get_epitet_line, get_color_line, get_animal_line, get_action_line

compliment_file = "compliment.txt"
oracle_file = "oracle.txt"
color_file = "color.txt"
animal_file = "animal.txt"
epitet_file = "epitet.txt"
action_file = "action.txt"

import locale
try:
    locale.setlocale(locale.LC_TIME, 'uk_UA.utf8')  # або 'uk_UA.utf-8'
except locale.Error as e:
    print(f"Не вдалося встановити локаль: {e}")

st.markdown("<h1 style='text-align: center; font-family: Helvetica, sans-serif; font-weight: 900;'>Привіт!</h1>",
            unsafe_allow_html=True)
st.markdown("<h2 style='border-radius: 50px; text-align: center; font-family: Helvetica, sans-serif; font-weight: 400; margin: 20px'>Який чудовий день сьогодні!</h2>",
            unsafe_allow_html=True)


#st.text_input(label="Як тебе звати?", placeholder="Напиши сюди своє прекрасне ім'я!", key="name")

# Розміщення кнопок в один ряд з використанням стовпців
col1, col2, col3 = st.columns(3)

button_comp_clicked = col1.button("**Комплімент дня для тебе!**")

button_oracle_clicked = col2.button("**Передбачення для тебе!**")

button_animal_clicked = col3.button("**Твоя тотемна тварина на сьогодні!**")



if button_comp_clicked:
    #name = st.session_state["name"]
    #user = name.capitalize()
    try:
        compliment = get_compliment_line(compliment_file)
        st.markdown(
            f'<div style="background-color:#FFB996; color:black; padding:20px; margin:20px;'
            f'border-radius: 50px; font-weight: bold;">{compliment}</div>',
            unsafe_allow_html=True
        )

    except ValueError:
        st.warning(f"Сонечко, ти щось не те робиш ;)")


if button_oracle_clicked:
    try:
        oracle = get_oracle_line(oracle_file)
        st.markdown(
            f'<div style="border-radius: 50px; background-color:#FDFFAB; color:black; padding:20px; margin:20px; font-weight: bold; ">{oracle}</div>',
            unsafe_allow_html=True
        )

    except ValueError:
        st.warning(f"Сонечко, ти щось не те робиш ;)")


if button_animal_clicked:
    try:
        epitet = get_epitet_line(epitet_file)
        color = get_color_line(color_file)
        animal = get_animal_line(animal_file)
        action = get_action_line(action_file)
        st.markdown(
            f'<div style="border-radius: 50px; background-color:#756AB6; color:white; padding:20px; margin:20px; font-weight: bold;">{epitet}{color}{animal}, який {action}</div>',
            unsafe_allow_html=True
        )

    except ValueError:
        st.warning(f"Сонечко, ти щось не те робиш ;)")


st.markdown("<h4 style='text-align: center; font-family: Helvetica, sans-serif; font-size: 16px; font-weight: lighter; margin-top: 200px;'>Версія 1.0.1</h4>",
            unsafe_allow_html=True)

