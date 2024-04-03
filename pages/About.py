import streamlit as st
import numpy as np

def show_about_page():
    st.title('About')
    st.write('Welcome to the About Page!')
    
    st.header('Text Extraction from Image')
    st.write('This project involves extracting text from images using Optical Character Recognition (OCR) techniques. Users can upload an image containing text, and the app will extract the text from the image and display it below.')
    st.write('Example: [Image Text Extraction App](https://github.com/example)')
    
    st.header('Paragraph or Sentence Maker')
    st.write('This module generates meaningful text from a given set of random words. Users can input random words or phrases, and the app will construct sentences or paragraphs based on those inputs.')
    st.write('Example: [Sentence Maker App](https://github.com/example)')
    
    st.header('Text Analysis')
    st.write('The text analysis module provides various analysis tools for paragraphs or texts. It includes generating word clouds, analyzing word frequencies, and visualizing data through graphs.')
    
   

if __name__ == '__main__':
    show_about_page()

