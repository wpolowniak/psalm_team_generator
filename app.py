import streamlit as st
from functions import community_members, copy_to_clipboard, split_teams, to_excel
import pandas as pd

st.title("Psalm Team Generator")

# get number of teams as input
num_teams = st.sidebar.slider('How many teams?', 1, 6, 3)

generate_button = st.sidebar.button('Generate Teams')
if generate_button:
    teams = split_teams(community_members, num_teams)
    st.write(teams)

    # st.button('Copy Teams to Clipboard', on_click=copy_to_clipboard(teams))
    df= to_excel(teams)
    st.download_button(label="Download",data=df,file_name='teams.xlsx')