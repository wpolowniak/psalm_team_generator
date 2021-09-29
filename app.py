import streamlit as st
from functions import community_members, copy_to_clipboard, split_teams
import pandas as pd

st.title("Psalm Team Generator")

# get number of teams as input
num_teams = st.sidebar.slider('How many teams?', 1, 6, 3)

generate_button = st.sidebar.button('Generate Teams')
if generate_button:
    teams = split_teams(community_members, num_teams)
    st.write(teams)

    if st.button('Copy Teams to Clipboard'):
        teams.to_clipboard(index=False)


