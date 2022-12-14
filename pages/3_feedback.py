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
        st.markdown("(1) On a scale of 0-10, how satisfied are you with the conroy classifier?")
        st.text_area("Enter reply to question 1","Type Here")
        st.markdown("(2) Was the platform easy to use?")
        st.text_area("Enter reply to question 2","Type Here")
        st.markdown("(3) Does the sentiments provided by this classifier reflect what you have in mind?")
        st.text_area("Enter reply to question 3","Type Here")
        st.markdown("(4) What improvement(s) would you like to see on this platform?")
        st.text_area("Enter reply to question 4","Type Here")
        st.markdown("(5) On a scale of 0-10, how well would you refer this platform to a friend?")
        st.text_area("Enter reply to question 5","Type Here")
        st.markdown("")
        st.markdown("Thank you for using this app. Be assured your reviews are going to lead to improvements on the app.")

if __name__ == '__main__':
	main()

if st.button("Submit Review"):
        st.success("Your review has been submitted. Thank you.")
