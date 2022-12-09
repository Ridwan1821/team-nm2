# Streamlit dependencies
import streamlit as st
import joblib,os

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
        st.subheader("About Us")
        st.markdown("Conroy AI Solutions is a tech company that bring solutions to real life problems using data driven techniques. \nWe do Data Analytics, Predictive Analysis and Data Mining. \nOur team is made of qualified and experienced personnel that take pride in helping the society using Data.")
        st.subheader("How to use the app")
        st.markdown("Select a tweet data and a classification model of your choice from the selectboxes. \nOnce you are done, click on Classify to apply the model on the data. \nAwait your predicitions.")
if __name__ == '__main__':
	main()
