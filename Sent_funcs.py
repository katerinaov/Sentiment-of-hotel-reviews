import pickle
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import tensorflow as tf

stop = set(stopwords.words('english'))
graph = tf.get_default_graph()


with open('tokenizer1.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

filename = 'Sentiment_model_1_1.pkl'
model = pickle.load(open(filename, 'rb'))

class SentimentObject():

    def __init__(self):
        pass

    def clean_one_review(self, texts):

        text_sample = texts.lower()
        text_sample = re.findall(r'(?:\w+)', text_sample, flags=re.UNICODE)
        text_sample = [i for i in text_sample if not i.isdigit()]
        print(text_sample)
        text_sample = ' '.join([i for i in text_sample if len(i) > 2 and i not in stop])

        return text_sample

    def tokenize_text(self, texts, MAX_NUM_WORDS=1000, MAX_SEQUENCE_LENGTH=100):

        sequences = tokenizer.texts_to_sequences([texts])
        print(sequences)
        word_index = tokenizer.word_index

        print('Found %s unique tokens.' % len(word_index))

        data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
        return data

