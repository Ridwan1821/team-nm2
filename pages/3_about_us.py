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
        img1 = img.resize((600,100))
        st.image(img1, caption=None, use_column_width=False)
	# Creates a main title and subheader on your page -
	# these are static across all pages
        #st.title("Tweet Classifer")
        #st.title('CONROY AI SOLUTIONS')
        st.subheader("About Us")
        st.markdown("Conroy AI Solutions is a tech company that bring solutions to real life problems using data driven techniques. \nWe do Data Analytics, Predictive Analysis and Data Mining. \nOur team is made of qualified and experienced personnels that take pride in helping the society using Data.")
        st.subheader("Meet the team")
        st.markdown("Conroy AI is made up of data professionals with similar mindset of changing the world positively through data.")
        img2 = Image.open('alaine.png')
        img3 = img2.resize((200,200))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img3, caption="CEO: Alaine Tobias", use_column_width=False)
        with col2:
                st.write("Alaine Tobias is a Data Scientist with over 10 years of professional experience. She has a B.Sc in Computer Science and a masters degree in Data Science.  \nOver the years, She has headed several teams of data professionals, solving real life issues in the process.")
        with col3:
                st.write("She hopes to help the world cope with climate change through this platform.")
        img4 = Image.open('beaver.png')
        img5 = img4.resize((200,150))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img5, caption="Lead Data Scientist: Keketso Muchichwa", use_column_width=False)
        with col2:
                st.write("Keketso Muchichwa is a Data Scientist with a deep foundation in Mathematics and Statistics. He has a B.Sc degree in Statistics and M.Sc in Collective Intelligence.  \n")
        with col3:
                st.write("")
        img6 = Image.open('eeman.png')
        img7 = img6.resize((200,200))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img7, caption="Data Scientist: Iman Fasasi", use_column_width=False)
        with col2:
                st.write("Iman Fasasi is a Data Scientist and an advocate of good Eco system. She has a B.Sc in Computer Science and she has acquired several data science cerfitications.  \nShe is being driven to achieve this project by her love for the Eco system")
        with col3:
                st.write("")
        img8 = Image.open('ridwan.png')
        img9 = img8.resize((200,200))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img9, caption="Data Engineer: Kolawole Ridwan", use_column_width=False)
        with col2:
                st.write("Kolawole Ridwan is a Data Engineer. He has a B.Sc in Computer Science and he has worked in several organizations as a data engineer. He takes pride in bridging the comunication gap between data professionals and non data savvy audiences using built applications.")
        with col3:
                st.write("")
        img10 = Image.open('temitope.png')
        img11 = img10.resize((200,200))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img11, caption="Marketing Lead: Temitope Olaitan", use_column_width=False)
        with col2:
                st.write("Temitope Olaitan is a Data Analyst and a Digital Marketer. He has a B.Sc in Mathematics and he has been a professional digital marketer for over 5 years.")
        with col3:
                st.write("")        
if __name__ == '__main__':
	main()
