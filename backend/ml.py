from utils import getRandomString, clean_text, word_stemmer, word_pos_tagger, word_lemmatizer

import pandas as pd
import re
import pickle
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def prepare():
	nltk.download('stopwords')
	nltk.download('punkt')
	nltk.download('wordnet')
	nltk.download('omw-1.4')

def text_classify(message):
    p_negative = pickle.load(open("p_negative", "rb"))
    p_positive = pickle.load(open("p_positive", "rb"))
    parameters_negative = pickle.load(open("parameters_negative", "rb"))
    parameters_positive = pickle.load(open("parameters_positive", "rb"))
    
    message = message.lower()
    message = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", message)
    # remove numbers
    message = re.sub(r"\d+", "", message)

    # remove stop words
    message = ' '.join([word for word in message.split() if word not in (stopwords.words('english'))])

    # tokenization
    message = word_tokenize(message)

    # stemming
    message = word_stemmer(message)

    # lemmatization
    message = word_lemmatizer(message)

    p_negative_message = p_negative
    p_positive_message = p_positive

    for word in message:
        if word in parameters_negative:
            p_negative_message *= parameters_negative[word]

        if word in parameters_positive:
            p_positive_message *= parameters_positive[word]

    if p_positive_message > p_negative_message:
        return 1
    elif p_negative_message > p_positive_message:
        return -1
    else:
        return 0