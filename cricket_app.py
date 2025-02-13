
import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Cricket Analysis Hub",
    page_icon="🏏",
    layout="wide"
)

# Title and description
st.title("🏏 Cricket Analysis Hub")
st.markdown("Welcome to the Cricket Analysis Hub! Explore cricket statistics and get match predictions.")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Match Predictor", "Player Stats", "Team Analysis"])

if page == "Match Predictor":
    st.header("Match Outcome Predictor")
    
    col1, col2 = st.columns(2)
    
    with col1:
        team1 = st.text_input("Enter Team 1 name")
        team1_ranking = st.slider("Team 1 ICC Ranking", 1, 12, 1)
        team1_form = st.slider("Team 1 Recent Form (0-100)", 0, 100, 50)
    
    with col2:
        team2 = st.text_input("Enter Team 2 name")
        team2_ranking = st.slider("Team 2 ICC Ranking", 1, 12, 2)
        team2_form = st.slider("Team 2 Recent Form (0-100)", 0, 100, 50)
    
    venue = st.selectbox("Select Match Venue Type", ["Home (Team 1)", "Away (Team 2)", "Neutral"])
    format = st.selectbox("Select Match Format", ["T20I", "ODI", "Test"])
    
    if st.button("Predict Match Outcome"):
        # Simple prediction model based on ranking and form
        team1_score = (13 - team1_ranking) * 0.6 + team1_form * 0.4
        team2_score = (13 - team2_ranking) * 0.6 + team2_form * 0.4
        
        # Adjust for venue advantage
        if venue == "Home (Team 1)":
            team1_score *= 1.1
        elif venue == "Away (Team 2)":
            team2_score *= 1.1
        
        # Calculate win probabilities
        total_score = team1_score + team2_score
        team1_prob = (team1_score / total_score) * 100
        team2_prob = (team2_score / total_score) * 100
        
        st.subheader("Match Prediction")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(f"{team1} Win Probability", f"{team1_prob:.1f}%")
        with col2:
            st.metric(f"{team2} Win Probability", f"{team2_prob:.1f}%")
        
        st.info("This is a simplified prediction model based on team rankings and form. Many other factors can influence the actual match outcome.")

elif page == "Player Stats":
    st.header("Player Statistics Generator")
    
    player_name = st.text_input("Enter Player Name")
    player_role = st.selectbox("Select Player Role", ["Batsman", "Bowler", "All-rounder"])
    matches = st.number_input("Number of Matches Played", min_value=0, value=50)
    
    if st.button("Generate Stats"):
        if player_role == "Batsman":
            avg = np.random.normal(35, 5)
            sr = np.random.normal(130, 10)
            
            st.subheader(f"Generated Stats for {player_name}")
            st.metric("Batting Average", f"{avg:.2f}")
            st.metric("Strike Rate", f"{sr:.2f}")
            
        elif player_role == "Bowler":
            avg = np.random.normal(25, 3)
            econ = np.random.normal(7.5, 0.5)
            
            st.subheader(f"Generated Stats for {player_name}")
            st.metric("Bowling Average", f"{avg:.2f}")
            st.metric("Economy Rate", f"{econ:.2f}")
            
        else:  # All-rounder
            bat_avg = np.random.normal(30, 5)
            bowl_avg = np.random.normal(28, 3)
            
            st.subheader(f"Generated Stats for {player_name}")
            st.metric("Batting Average", f"{bat_avg:.2f}")
            st.metric("Bowling Average", f"{bowl_avg:.2f}")

else:  # Team Analysis
    st.header("Team Performance Analysis")
    
    team_name = st.text_input("Enter Team Name")
    format = st.selectbox("Select Format", ["T20I", "ODI", "Test"])
    
    if st.button("Analyze Team"):
        # Generate random performance metrics
        win_rate = np.random.normal(55, 10)
        avg_score = np.random.normal(160 if format == "T20I" else 280 if format == "ODI" else 350, 20)
        
        st.subheader(f"{team_name} Performance Analysis")
        st.metric("Win Rate", f"{win_rate:.1f}%")
        st.metric("Average Score", f"{avg_score:.0f}")
        
        # Generate random form chart
        st.subheader("Recent Form")
        chart_data = pd.DataFrame(
            np.random.normal(win_rate, 10, size=(10, 1)),
            columns=['Performance']
        )
        st.line_chart(chart_data)

st.sidebar.markdown("---")
st.sidebar.markdown("Created with ❤️ by Cricket Analysis Hub")
