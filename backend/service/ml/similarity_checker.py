import string

import nltk
import spacy
from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_md')
nltk.download('stopwords')
stopwords_list = stopwords.words('english')


def get_difference_score(sentence1, sentence2):
    '''
    Function to get similarity scores between 2 sentences. Compares word2vec vectors of words in sentences.
    '''
    # Preprocessing
    punctuation_remover = str.maketrans(
        string.punctuation, ' '*len(string.punctuation))

    sentence1 = sentence1.translate(punctuation_remover)
    sentence1 = sentence1.lower().split()
    sentence1 = nlp(
        ' '.join([word for word in sentence1 if word not in stopwords_list]))

    sentence2 = sentence2.translate(punctuation_remover)
    sentence2 = sentence2.lower().split()
    sentence2 = nlp(
        ' '.join([word for word in sentence2 if word not in stopwords_list]))

    return sentence1.similarity(sentence2)
