# Streamlit dependencies
import streamlit as st

# Data dependencies
import numpy as np
import pandas as pd
import PIL
from PIL import Image

def main():
        """Tweet Classifier App with Streamlit """
        img = Image.open('conroy.png')
        st.image(img, caption=None)
	# Creates a main title and subheader on your page -
	# these are static across all pages
        #st.title("Tweet Classifer")
        #st.title('CONROY AI SOLUTIONS')
        st.subheader("Customer Feedback")
        st.text_input("Enter your email address","")
        #st.markdown("(1) On a scale of 0-10, how satisfied are you with the conroy classifier?")
        option = [0,1,2,3,4,5,6,7,8,9,10]
        selection = st.selectbox("(1) On a scale of 0-10, how satisfied are you with the conroy classifier?", option)
        #st.text_input("","Type Here")
        #st.markdown("(2) Was the platform easy to use?")
        st.text_input("(2) Was the platform easy to use?","")
        #st.markdown("(3) Does the sentiments provided by this classifier reflect what you have in mind?")
        st.text_input("(3) Does the sentiments provided by this classifier reflect what you have in mind?","")
        #st.markdown("(4) What improvement(s) would you like to see on this platform?")
        st.text_input("(4) What improvement(s) would you like to see on this platform?","")
        #st.markdown("(5) Would you refer this platform to a friend?")
        st.text_input("(5) Would you refer this platform to a friend?","")
        st.markdown("")
        st.markdown("Thank you for using this app.")

if __name__ == '__main__':
	main()

if st.button("Submit Review"):
        st.success("Your review has been submitted. Thank you.")
