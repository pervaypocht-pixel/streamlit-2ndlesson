import streamlit as st
import random
st.set_page_config(page_title="mango", 
                   page_icon="4463971.png",
                   layout="wide")
st.title("welcome")
tab1,tab2,tab3,tab4=st.tabs(["Main","Second","links","minigame"])
with tab1:
    st.header("Main")
    st.write("This is the main tab.")
    col1,col2=st.columns([1,2])
    with col1:
        st.image("images.jpg", caption="ilovemangoes",width=300)
    with col2:
        st.subheader("Mangoes are delicious fruits that are loved by many people around the world. They come in various varieties and are known for their sweet and juicy flavor.")
        st.write("Mangoes are not only tasty but also packed with nutrients, making them a healthy choice for a snack or dessert.")
        st.write("In addition to being enjoyed fresh, mangoes can be used in a variety of recipes, including smoothies, salads, and desserts.")
        st.write("Overall, mangoes are a versatile and delightful fruit that can be enjoyed in many different ways.")
        with st.container():
            st.success("Mangoes are a great source of vitamins and minerals, including vitamin C, vitamin A, and potassium.")
            st.warning("However, some people may be allergic to mangoes, so it's important to be cautious if you have a known allergy.")
            st.markdown("For more information about mangoes, you can visit the [Mango Board](https://www.mango.org/) website.")
            st.markdown("You can also check out the [Mango Recipes](https://www.allrecipes.com/recipes/16792/fruits-and-vegetables/fruits/mango/) page for delicious ways to enjoy mangoes.")
with tab2:
    st.header("tut nechego net")
with tab3:
    st.title("Корисні посилання")
    st.write("Ось список корисних сайтів для навчання та програмування:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(" Програмування")

        st.markdown("[Python](https://www.python.org/)")
        st.markdown("[W3Schools](https://www.w3schools.com/python/)")
        st.markdown("[Streamlit](https://streamlit.io/)")

    with col2:
        st.subheader("Інші ресурси")

        st.markdown("[GitHub](https://github.com/)")
        st.markdown("[freeCodeCamp](https://www.freecodecamp.org/)")
        st.markdown("[GeeksforGeeks](https://www.geeksforgeeks.org/)")
with tab4:
    st.title("Вгадай число!")
    st.write("Я загадав число від 1 до 100. Спробуй вгадати!")
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)

    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    if "game_over" not in st.session_state:
        st.session_state.game_over = False
    guess = st.number_input(
        "Введіть число від 1 до 100:",
        min_value=1,
        max_value=100,
        step=1
    )
    if st.button("Перевірити", disabled=st.session_state.game_over):
        st.session_state.attempts += 1

        if guess < st.session_state.secret_number:
            st.info("Загадане число більше!")

        elif guess > st.session_state.secret_number:
            st.info("Загадане число менше!")

        else:
            st.success("Вітаємо! Ви вгадали!")
            st.balloons()
            st.session_state.game_over = True
    st.write(f"Кількість спроб: {st.session_state.attempts}")
    if st.button(" Зіграти знову"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()