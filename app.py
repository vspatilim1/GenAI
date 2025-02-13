
import streamlit as st
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import pandas as pd

# Page config
st.set_page_config(
    page_title="CricketGPT - Cricket Analysis with AI",
    page_icon="🏏",
    layout="wide"
)

# Title
st.title("🏏 CricketGPT - Cricket Analysis with AI")

# Sidebar for API key
with st.sidebar:
    openai_api_key = st.text_input("Enter OpenAI API Key", type="password")
    st.markdown("---")
    st.markdown("""
    ## Features
    - Player Analysis
    - Match Prediction
    - Commentary Generation
    - Strategy Advisor
    """)

# Initialize ChatOpenAI
if openai_api_key:
    llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
else:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Player Analysis", 
    "Match Prediction", 
    "Commentary Generator",
    "Strategy Advisor"
])

# Player Analysis Tab
with tab1:
    st.header("Player Analysis")
    player_name = st.text_input("Enter player name:")
    if st.button("Analyze Player") and player_name:
        with st.spinner("Analyzing player..."):
            response = llm([
                SystemMessage(content="You are a cricket expert analyst. Provide detailed analysis of the player."),
                HumanMessage(content=f"Provide a detailed analysis of {player_name} including their playing style, strengths, weaknesses, and career highlights.")
            ])
            st.write(response.content)

# Match Prediction Tab
with tab2:
    st.header("Match Prediction")
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.text_input("Team 1:")
    with col2:
        team2 = st.text_input("Team 2:")
    
    venue = st.text_input("Venue:")
    
    if st.button("Predict Match") and team1 and team2:
        with st.spinner("Analyzing match factors..."):
            response = llm([
                SystemMessage(content="You are a cricket match predictor. Analyze teams and provide match prediction."),
                HumanMessage(content=f"Predict the match between {team1} vs {team2} at {venue}. Consider team form, head-to-head record, and venue conditions.")
            ])
            st.write(response.content)

# Commentary Generator Tab
with tab3:
    st.header("Commentary Generator")
    match_situation = st.text_area("Describe the match situation:")
    commentary_style = st.selectbox(
        "Select commentary style:",
        ["Traditional", "Exciting", "Technical", "Humorous"]
    )
    
    if st.button("Generate Commentary") and match_situation:
        with st.spinner("Generating commentary..."):
            response = llm([
                SystemMessage(content=f"You are a cricket commentator with a {commentary_style.lower()} style."),
                HumanMessage(content=f"Generate commentary for this situation: {match_situation}")
            ])
            st.write(response.content)

# Strategy Advisor Tab
with tab4:
    st.header("Strategy Advisor")
    scenario = st.text_area("Describe the match scenario:")
    target_audience = st.selectbox(
        "Advice for:",
        ["Captain", "Batsman", "Bowler", "Team Management"]
    )
    
    if st.button("Get Strategy Advice") and scenario:
        with st.spinner("Generating strategic advice..."):
            response = llm([
                SystemMessage(content=f"You are a cricket strategy expert providing advice for a {target_audience.lower()}."),
                HumanMessage(content=f"Provide strategic advice for this scenario: {scenario}")
            ])
            st.write(response.content)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and OpenAI")
