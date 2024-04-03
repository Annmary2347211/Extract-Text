import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter

# Function to plot word frequency as a bar chart
def plot_word_frequency_bar(text):
    words = text.split()
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_words = [word[0] for word in sorted_word_counts[:10]]
    top_word_counts = [word[1] for word in sorted_word_counts[:10]]

    plt.figure(figsize=(10, 6))
    plt.bar(top_words, top_word_counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Most Frequent Words')
    st.pyplot()

# Function to plot word frequency as a pie chart
def plot_word_frequency_pie(text):
    words = text.split()
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_words = [word[0] for word in sorted_word_counts[:10]]
    top_word_counts = [word[1] for word in sorted_word_counts[:10]]

    plt.figure(figsize=(8, 8))
    plt.pie(top_word_counts, labels=top_words, autopct='%1.1f%%', startangle=140)
    plt.title('Top 10 Most Frequent Words')
    st.pyplot()

# Function to plot text length distribution as a histogram
def plot_text_length_distribution_hist(text):
    text_lengths = [len(word) for word in text.split()]
    
    plt.figure(figsize=(10, 6))
    plt.hist(text_lengths, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Text Length')
    plt.ylabel('Frequency')
    plt.title('Text Length Distribution (Histogram)')
    st.pyplot()

# Function to plot text length distribution as a box plot
def plot_text_length_distribution_box(text):
    text_lengths = [len(word) for word in text.split()]
    
    plt.figure(figsize=(10, 6))
    plt.boxplot(text_lengths, vert=False)
    plt.xlabel('Text Length')
    plt.title('Text Length Distribution (Box Plot)')
    st.pyplot()

# Streamlit UI
st.title('Text Analysis and Visualization')

# Text input
text = st.text_area('Enter your text here')

# Dropdown menu for selecting analysis type
analysis_type = st.selectbox('Select Analysis Type', ['Word Frequency', 'Text Length Distribution'])

# Dropdown menu for selecting graph type
if analysis_type == 'Word Frequency':
    graph_type = st.selectbox('Select Graph Type', ['Bar Chart', 'Pie Chart'])
elif analysis_type == 'Text Length Distribution':
    graph_type = st.selectbox('Select Graph Type', ['Histogram', 'Box Plot'])

# Plotting based on analysis type and graph type selection
if text:
    if analysis_type == 'Word Frequency':
        if graph_type == 'Bar Chart':
            plot_word_frequency_bar(text)
        elif graph_type == 'Pie Chart':
            plot_word_frequency_pie(text)
    elif analysis_type == 'Text Length Distribution':
        if graph_type == 'Histogram':
            plot_text_length_distribution_hist(text)
        elif graph_type == 'Box Plot':
            plot_text_length_distribution_box(text)
else:
    st.write('Please enter some text to analyze.')
