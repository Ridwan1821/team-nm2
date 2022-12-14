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
        st.subheader("Information")
        st.markdown("Climate change refers to long term shifts in temparature and weather patterns. These shifts may be natural, but since the 1800s, human activities have been the main driver of climate change due to the burning of fossil fuel which produces heat-trapping gases. Other causes of climate change are (but not limited to) deforestation and waste plastic.")
        img12 = Image.open('img12.jpeg')
        img13 = img12.resize((200,200))
        img14 = Image.open('img14.jpeg')
        img15 = img14.resize((200,200))
        img16 = Image.open('img16.jpeg')
        img17 = img16.resize((200,200))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.image(img13, caption="Deforestation", use_column_width=False)
        with col2:
                st.image(img15, caption="Waste Plastic", use_column_width=False)
        with col3:
                st.image(img17, caption="Fossil Fuel", use_column_width=False)
        st.markdown("Conroy AI has developed several models that predict the sentiment of people towards climate change through their words. This platform allows users to write about climate change and get what their sentiment to climate change is.")
        st.subheader("How to use the app")
        st.markdown("Select a model and then enter a text that is about climate change on the text box. \nOnce you are done, click on Classify to apply the model on the text. \nThe sentiment of the text will be stated.")
if __name__ == '__main__':
	main()
