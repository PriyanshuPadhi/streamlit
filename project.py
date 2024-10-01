import streamlit as st
import pandas as pd
import os
 
# File to store user details
USER_DATA_FILE = 'user_data.csv'
 
# Function to load user data from CSV
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        return pd.read_csv(USER_DATA_FILE)
    else:
        return pd.DataFrame(columns=['Username', 'Password', 'Mobile', 'DOB'])
 
# Function to save new user data into the CSV
def save_user_data(username, password, mobile, dob):
    new_user = pd.DataFrame({
        'Username': [username],
        'Password': [password],
        'Mobile': [mobile],
        'DOB': [dob]
    })
    new_user.to_csv(USER_DATA_FILE, mode='a', header=not os.path.exists(USER_DATA_FILE), index=False)
 
# Load user data
users_df = load_user_data()
 
# Sidebar for action selection
st.sidebar.title("User Actions")
action = st.sidebar.radio("Select Action", ("Login", "Sign Up"))
 
if action == "Sign Up":
    st.header("Welcome! Sign Up")
 
    # Sign-up form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    mobile = st.text_input("Mobile Number")
    dob = st.date_input("Date of Birth")
   
    if st.button("Submit"):
        # Check if username already exists
        if username in users_df['Username'].values:
            st.error("Username already exists! Please choose another username.")
        else:
            # Append new user data
            save_user_data(username, password, mobile, dob)
            st.success("You have signed up successfully!")
 
elif action == "Login":
    st.header("Login Page")
   
    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
   
    if st.button("Login"):
        # Check if username exists
        if username not in users_df['Username'].values:
            st.error("Username does not exist!")
        else:
            # Validate password
            stored_password = users_df[users_df['Username'] == username]['Password'].values[0]
            if password == stored_password:
                st.success(f"Welcome back, {username}!")
            else:
                st.error("Incorrect password!")