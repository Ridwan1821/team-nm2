"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
import numpy as np
import pandas as pd
import pickle
import PIL
from PIL import Image

# Vectorizer
# news_vectorizer = open("resources/tfidfvect.pkl","rb")
# tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
# raw = pd.read_csv("resources/train.csv")

# The main function where we will build the actual app
def main():
        """Tweet Classifier App with Streamlit """
        img = Image.open('conroy.png')
        st.image(img, caption=None)
	# Creates a main title and subheader on your page -
	# these are static across all pages
        #st.title("Tweet Classifer")
        st.title('CONROY Tweet Classifer')
        st.subheader("Climate Change Tweet Classification")

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()

	# Creating sidebar with selection box -
	# you can create multiple pages this way
option1 = ["test_1", "test_2", "test_3"]
#selection1 = st.sidebar.selectbox("Choose tweet data", option1)
selection1 = st.selectbox("Choose tweet data", option1)
option2 = ["Logistic Regression", "Decision Tree Classifier"]
#selection2 = st.sidebar.selectbox("Choose model", option2)
selection2 = st.selectbox("Choose model", option2)

if selection1 == "test_1" and selection2 == "Logistic Regression":
        raw = pd.read_csv("resources/test_1.csv")
        tweet_cv = joblib.load(open("resources/Logistic_regression.pkl","rb"))
        st.info("Prediction with "+str(selection2)+" Model")
        st.markdown("Logistic regression is a Machine Learning model that models the probability of an event taking place by having the log-odds for the event as a linear combination of one or more independent variables. \nLogistic Regression is used in the medical field, social sciences and many other fields.")
elif selection1 == "test_1" and selection2 == "Decision Tree Classifier":
        raw = pd.read_csv("resources/test_1.csv")
        tweet_cv = joblib.load(open("resources/Decision_tree_classifier.pkl","rb"))
        st.info("Prediction with "+str(selection2)+" Model")
        st.markdown("Decision tree classifier is a Machine Learning model that is used to draw conclusions about a set of observations. This model is among the most popular machine leaarning algorithms given its intelligibility and simplicity.")
elif selection1 == "test_2" and selection2 == "Logistic Regression":
        raw = pd.read_csv("resources/test_2.csv")
        tweet_cv = joblib.load(open("resources/Logistic_regression.pkl","rb"))
        st.info("Prediction with "+str(selection2)+" Model")
        st.markdown("Logistic regression is a Machine Learning model that models the probability of an event taking place by having the log-odds for the event as a linear combination of one or more independent variables. \nLogistic Regression is used in the medical field, social sciences and many other fields.")
elif selection1 == "test_2" and selection2 == "Decision Tree Classifier":
        raw = pd.read_csv("resources/test_2.csv")
        tweet_cv = joblib.load(open("resources/Decision_tree_classifier.pkl","rb"))
        st.info("Prediction with "+str(selection2)+" Model")
        st.markdown("Decision tree classifier is a Machine Learning model that is used to draw conclusions about a set of observations. This model is among the most popular machine leaarning algorithms given its intelligibility and simplicity.")
elif selection1 == "test_3" and selection2 == "Logistic Regression":
        raw = pd.read_csv("resources/test_3.csv")
        tweet_cv = joblib.load(open("resources/Logistic_regression.pkl","rb"))
        st.info("Prediction with "+str(selection2)+" Model")
        st.markdown("Logistic regression is a Machine Learning model that models the probability of an event taking place by having the log-odds for the event as a linear combination of one or more independent variables. \nLogistic Regression is used in the medical field, social sciences and many other fields.")
elif selection1 == "test_3" and selection2 == "Decision Tree Classifier":
        raw = pd.read_csv("resources/test_3.csv")
        tweet_cv = joblib.load(open("resources/Decision_tree_classifier.pkl","rb"))
        st.info("Prediction with "+str(selection2)+" Model")
        st.markdown("Decision tree classifier is a Machine Learning model that is used to draw conclusions about a set of observations. This model is among the most popular machine leaarning algorithms given its intelligibility and simplicity.")

	# Building out the "Information" page
#if selection2 == "Logistic Regression":
#        tweet_cv = joblib.load(open("resources/Logistic_regression.pkl","rb"))
#elif selection2 == "Vect":
#        tweet_cv = joblib.load(open("resources/vect.pkl","rb"))
		#st.info("General Information")
		# You can read a markdown file from supporting resources folder
		#st.markdown("Some information here")

		#st.subheader("Raw Twitter data and label")
		#if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			#st.write(raw[['sentiment', 'message']]) # will write the df to the page

	# Building out the predication page
#st.info("Prediction with "+str(selection2)+" Model")
		# Creating a text box for user input
#if selection2 == "Logistic Regression":
        #st.markdown("Logistic regression is an ML model that...")
#elif selection2 == "Vect":
#        st.markdown("Vect regression is an ML model that...")
#tweet_text = st.text_area("Click on Classify to apply your model")
tweet_text = st.markdown("Click on Classify to apply your model")
if st.button("Classify"):
                        # Transforming user input with vectorizer
                        #vect_text = tweet_cv.transform([tweet_text]).toarray()
                        # Load your .pkl file with the model of your choice + make predictions
                        # Try loading in multiple models to give the user a choice
                        #predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
        predictor = tweet_cv
        prediction = predictor.predict(raw)

                        # When model has successfully run, will print prediction
                        # You can use a dictionary or similar structure to make this output
                        # more human interpretable.
                        #st.success("Text Categorized as: {}".format(prediction))
        st.success(str(selection2)+" successfully applied on "+str(selection1))
