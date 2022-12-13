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
vectorizer = pickle.load(open("resources/vect.pkl","rb"))
#tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file
# Models
#log_reg = pickle.load(open("resources/logistic.pkl", 'rb'))
#ridge = pickle.load(open("resources/ridge.pkl", 'rb'))
#dec_tree = pickle.load(open("resources/dec_tree.pkl", 'rb'))

# Load your raw data
# raw = pd.read_csv("resources/train.csv")

# The main function where we will build the actual app
def main():
        """Tweet Classifier App with Streamlit """
        img = Image.open('conroy.png')
        st.image(img, caption=None, width=450)
	# Creates a main title and subheader on your page -
	# these are static across all pages
        #st.title("Tweet Classifer")
        #st.title('CONROY Tweet Classifer')
        st.subheader("Climate Change Tweet Classification")

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()

	# Creating sidebar with selection box -
	# you can create multiple pages this way
option = ["Logistic Regression", "Ridge Classifier", "Decision Tree Classifier"]
selection = st.selectbox("Choose model", option)

if selection == "Logistic Regression":
        pred = pickle.load(open("resources/logistic.pkl", 'rb'))
        st.info("Prediction with "+str(selection)+" Model")
        st.markdown("Logistic regression is a Machine Learning model that models the probability of an event taking place by having the log-odds for the event as a linear combination of one or more independent variables. \nLogistic Regression is used in the medical field, social sciences and many other fields.")
elif selection == "Ridge Classifier":
        pred = pickle.load(open("resources/ridge.pkl", 'rb'))
        st.info("Prediction with "+str(selection)+" Model")
        st.markdown("Ridge classification is a technique used to analyze linear discriminant models. It is a form of regularization that penalizes model coefficients to prevent overfitting.")
elif selection == "Decision Tree Classifier":
        pred = pickle.load(open("resources/dec_tree.pkl", 'rb'))
        st.info("Prediction with "+str(selection)+" Model")
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
tweet_text = st.text_area("Enter Text","Type Here")
tweet = [tweet_text]
tweet_msg = pd.DataFrame({'msg':tweet})
if st.button("Classify"):
                        # Transforming user input with vectorizer
                        #vect_text = tweet_cv.transform([tweet_text]).toarray()
                        # Load your .pkl file with the model of your choice + make predictions
                        # Try loading in multiple models to give the user a choice
                        #predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
        vect_text = vectorizer.transform(tweet_msg['msg'].values.astype(str))
        prediction = pred.predict(vect_text)

                        # When model has successfully run, will print prediction
                        # You can use a dictionary or similar structure to make this output
                        # more human interpretable.
                        #st.success("Text Categorized as: {}".format(prediction))
        if prediction == 2:
                sentiment = 'News category'
        elif prediction == 1:
                sentiment = 'Pro climate change'
        elif prediction == 0:
                sentiment = 'Neutral to climate change'
        elif prediction == -1:
                sentiment = 'Anti climate change'
        st.success("Text Categorized as: " + sentiment)
        #st.success("Text Categorized as: {}".format(prediction))
