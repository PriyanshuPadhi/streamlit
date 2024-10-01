import streamlit as st
import pandas as pd
import json
import os

# File to store user details
USER_DATA_FILE = 'user_data.json'

# Function to load user data from JSON
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return pd.DataFrame(data)
                elif isinstance(data, dict):
                    # If it's a single dictionary, convert it to a DataFrame with one row
                    return pd.DataFrame([data])
                else:
                    # If the JSON structure is unexpected, return an empty DataFrame
                    return pd.DataFrame(columns=['Username', 'Password', 'Mobile', 'DOB'])
            except json.JSONDecodeError:
                # If JSON is malformed, return an empty DataFrame
                return pd.DataFrame(columns=['Username', 'Password', 'Mobile', 'DOB'])
    else:
        # If the file doesn't exist, return an empty DataFrame
        return pd.DataFrame(columns=['Username', 'Password', 'Mobile', 'DOB'])

# Function to save new user data into the JSON
def save_user_data(username, password, mobile, dob):
    new_user = {
        'Username': username,
        'Password': password,
        'Mobile': mobile,
        'DOB': str(dob)  # Convert date to string for JSON serialization
    }
    
    # Load existing users
    users_df = load_user_data()
    
    # Check if the DataFrame is empty
    if users_df.empty:
        users_df = pd.DataFrame([new_user])
    else:
        # Append the new user to the DataFrame
        users_df = pd.concat([users_df, pd.DataFrame([new_user])], ignore_index=True)
    
    # Save the updated DataFrame back to JSON
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users_df.to_dict(orient='records'), file, indent=4)

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

    # Set minimum and maximum birth years
    dob = st.date_input(
        "Date of Birth", 
        min_value=pd.Timestamp(1980, 1, 1), 
        max_value=pd.Timestamp(2024, 12, 31)
    )

    if st.button("Submit"):
        # Trim whitespace from username
        username = username.strip()
        
        # Basic validation
        if not username or not password or not mobile:
            st.error("Please fill in all fields.")
        elif username in users_df['Username'].values:
            st.error("Username already exists! Please choose another username.")
        else:
            # Append new user data
            save_user_data(username, password, mobile, dob)
            st.success("You have signed up successfully!")
            
            # Refresh the DataFrame
            users_df = load_user_data()

elif action == "Login":
    st.header("Login Page")
    
    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Trim whitespace from username
        username = username.strip()
        
        if username not in users_df['Username'].values:
            st.error("Username does not exist!")
        else:
            # Retrieve the stored password
            stored_password = users_df.loc[users_df['Username'] == username, 'Password'].values[0]
            if password == stored_password:
                st.success(f"Welcome back, {username}!")
            else:
                st.error("Incorrect password!")
