import streamlit as st
import nltk

# Download NLTK resources
nltk.download('punkt')

# Function to generate a meaningful sentence using given words
def generate_sentence(words, corpus):
    # Tokenize the corpus into sentences
    sentences = nltk.sent_tokenize(corpus)

    # Find sentences that contain all of the given words
    matching_sentences = []
    for sentence in sentences:
        if all(word.lower() in sentence.lower() for word in words):
            matching_sentences.append(sentence)

    if matching_sentences:
        # Randomly select a sentence from the matching sentences
        selected_sentence = matching_sentences[0]  # For simplicity, just selecting the first matching sentence
        return selected_sentence
    else:
        return "No meaningful sentence found with the given words."

# Streamlit UI
st.title('Meaningful Sentence Generator')
st.write('Enter some random words separated by commas and click on "Generate" to create a meaningful sentence.')

input_words = st.text_input('Enter words (separated by commas)')
generate_button = st.button('Generate')

corpus = """Your corpus goes here, replace this with your actual text corpus."""

if generate_button:
    words = [word.strip() for word in input_words.split(',') if word.strip()]
    
    if words:
        sentence = generate_sentence(words, corpus)
        st.subheader('Generated Sentence:')
        st.write(sentence)
    else:
        st.write('Please enter some words.')
