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
        st.subheader("Exploratory Data Analysis - EDA")
        st.markdown("The data that was used to train our models is a tweet data that contain 15819 rows and 3 columns. The columns are sentiment, message and tweetid while the rows contain records having sentiment, message and tweetid.  \nAfter exploring this data, the following insights were uncovered:")
        img18 = Image.open('eda1.png')
        img19 = img18.resize((200,200))
        img20 = Image.open('eda2.png')
        img21 = img20.resize((200,200))
        img22 = Image.open('eda3.png')
        img23 = img22.resize((200,200))
        img24 = Image.open('eda4.png')
        img25 = img24.resize((200,200))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img19, caption="First five records", use_column_width=False)
        with col2:
                st.image(img21, caption="Sentiments", use_column_width=False)
        with col3:
                st.write("53.9% of the observations are pro climate change.  \n8.2% are anti climate change.  \n14.9% are neutral while 23% of the observations fall into the NEWS category.")
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img23, caption="Imbalanced data", use_column_width=False)
        with col2:
                st.image(img25, caption="Balanced data", use_column_width=False)
        with col3:
                st.write("Our data is imbalanced as some sentiments have way more observations than others.  \nThe data was balanced so that every sentiment category will have equal number of observations. This will help remove some bias from the model")
        st.markdown("The message column is the predictive feature of the data. As such, we removed stop words, urls and punctuations from the column. We then applied tokenization and lemmatization before we did data preprocessing.  \n The following images contain word clouds gotten from messages under each category of sentiments.")
        img26 = Image.open('pro.png')
        img27 = img26.resize((200,200))
        img28 = Image.open('anti.png')
        img29 = img29.resize((200,200))
        img30 = Image.open('neutral.png')
        img31 = img30.resize((200,200))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img27, caption="Pro climate change", use_column_width=False)
        with col2:
                st.image(img29, caption="Anti climate change", use_column_width=False)
        with col3:
                st.write(img31, caption="Neutral", use_column_width=False)

        #st.subheader("How to use the app")
        #st.markdown("Select a model and then enter a text that is about climate change on the text box. \nOnce you are done, click on Classify to apply the model on the text. \nThe sentiment of the text will be stated.")
if __name__ == '__main__':
	main()
