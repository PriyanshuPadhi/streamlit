import streamlit as st

st.title('Hello World')

#take input from user and display it
name = st.text_input('Enter your name')
st.write('Hello', name)

#demo of dropdown box in streamlit
option = st.selectbox('Which number do you like best?', [1,2,3,4,5])
st.write('You selected:', option)

#demo of radio button in streamlit
option = st.radio('Which number do you like best?', [1,2,3,4,5])
st.write('You selected:', option)

#demo of checkbox in streamlit
if st.checkbox('Show/Hide'):
    st.write('Showing or Hiding Widget')

#demo of slider in streamlit
age = st.slider('How old are you?', 0, 130, 25)
st.write('I am:', age, 'years old')

#demo of button in streamlit
if st.button('Say Hello'):
    st.write('Hello')

#demo of text area in streamlit
message = st.text_area('Enter your message')
st.write('You entered:', message)

#demo of date input in streamlit
import datetime
today = st.date_input('Today is', datetime.datetime.now())
st.write('Today is:', today)

#demo of time input in streamlit
time = st.time_input('The time is', datetime.time())
st.write('The time is:', time)

#current system time
st.write('Current time is:', datetime.datetime.now())

#demo of file uploader in streamlit & display the uploaded file may be a csv
import pandas as pd
uploaded_file = st.file_uploader('Choose a file', type = ['csv'])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

#demo of progress bar in streamlit
import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

#demo of sidebar in streamlit
st.sidebar.write('This is a sidebar')
st.sidebar.button('Press me') 

#demo of expander in streamlit
with st.expander('See more'):
    st.write('This is hidden by default')

#demo of columns in streamlit
col1, col2, col3 = st.columns(3)
col1.write('This is column 1')
col2.write('This is column 2')
col3.write('This is column 3')

#demo of plot in streamlit
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100)
fig, ax = plt.subplots()
ax.hist(x, bins = 20)
st.pyplot(fig)

#demo of image in streamlit
from PIL import Image
image = Image.open("/Users/priya/Downloads/Apache.jpeg")
st.image(image, caption = ' Hadoop Pig', use_column_width = True)

#demo of youtube video in streamlit
st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

#demo of video from local file
video_file = open('/Users/priya/Videos/Captures/Fortnite   2024-07-03 17-29-03.mp4')



