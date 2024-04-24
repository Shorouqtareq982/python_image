import nltk 
from nltk.corpus import stopwords
from collections import Counter

\
nltk.download('punkt')
nltk.download('stopwords')


def process_text(file_path):

    stop_words = set(stopwords.words('english'))
    

    with open(file_path, 'r') as file:
        text = file.read()
    
 
    words = [word for word in nltk.word_tokenize(text.lower()) if word.isalpha() and word not in stop_words]
    
    
    word_freq = Counter(words)
    
    
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")


process_text('paragraphs.txt')