import streamlit as st
import random
import base64
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✂️")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.title("Rock, Paper, Scissors")

if 'max_points' not in st.session_state:
    st.session_state.max_points = 5

max_points = st.number_input("Maximum Points to Win:", min_value=1, value=st.session_state.max_points)
st.session_state.max_points = max_points

if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0

col1, col2, col3 = st.columns(3)

with col1:
    with stylable_container(
        key="rock_button",
        css_styles=f"""
            button {{
                background-image: url("data:image/png;base64,{get_base64_of_bin_file('rock.png')}");
                background-size: cover;
                background-repeat: no-repeat;
                height: 200px;
                width: 200px;
            }}
            """,
    ):
        if st.button("Rock", key="rock"):
            user_choice = "rock"
            computer_choice = random.choice(["rock", "paper", "scissors"])
            st.session_state.user_choice = user_choice
            st.session_state.computer_choice = computer_choice

with col2:
    with stylable_container(
        key="paper_button",
        css_styles=f"""
            button {{
                background-image: url("data:image/png;base64,{get_base64_of_bin_file('paper.png')}");
                background-size: cover;
                background-repeat: no-repeat;
                height: 200px;
                width: 200px;
            }}
            """,
    ):
        if st.button("Paper", key="paper"):
            user_choice = "paper"
            computer_choice = random.choice(["rock", "paper", "scissors"])
            st.session_state.user_choice = user_choice
            st.session_state.computer_choice = computer_choice

with col3:
    with stylable_container(
        key="scissors_button",
        css_styles=f"""
            button {{
                background-image: url("data:image/png;base64,{get_base64_of_bin_file('scissors.png')}");
                background-size: cover;
                background-repeat: no-repeat;
                height: 200px;
                width: 200px;
            }}
            """,
    ):
        if st.button("Scissors", key="scissors"):
            user_choice = "scissors"
            computer_choice = random.choice(["rock", "paper", "scissors"])
            st.session_state.user_choice = user_choice
            st.session_state.computer_choice = computer_choice

if 'user_choice' in st.session_state:
    st.write(f"You chose **{st.session_state.user_choice}**, computer chose **{st.session_state.computer_choice}**.")

    if st.session_state.user_choice == st.session_state.computer_choice:
        st.info("It's a tie!")
    elif (st.session_state.user_choice == "rock" and st.session_state.computer_choice == "scissors") or \
            (st.session_state.user_choice == "paper" and st.session_state.computer_choice == "rock") or \
            (st.session_state.user_choice == "scissors" and st.session_state.computer_choice == "paper"):
        st.success("You win this round!")
        st.session_state.user_score += 1
    else:
        st.error("Computer wins this round!")
        st.session_state.computer_score += 1
    
    # Clear choices for next round
    if 'user_choice' in st.session_state:
        del st.session_state.user_choice
    if 'computer_choice' in st.session_state:
        del st.session_state.computer_choice

if st.session_state.user_score >= st.session_state.max_points:
    st.balloons()
    st.success("You won the game!")
    if st.button("New Game"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0

elif st.session_state.computer_score >= st.session_state.max_points:
    st.error("Computer won the game!")
    if st.button("New Game"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0

st.write(f"## Score: You {st.session_state.user_score} - {st.session_state.computer_score} Computer")
