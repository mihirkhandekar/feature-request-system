import spacy
import string
import nltk
from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_md')
nltk.download('stopwords')
stopwords_list = stopwords.words('english')


def get_difference_score(sentence1, sentence2):
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


if __name__ == '__main__':
    print(get_difference_score('obama was the president', 'my name is not obama'))
