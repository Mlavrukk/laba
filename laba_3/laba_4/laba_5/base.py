import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torchvision
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
from collections import Counter

from pymystem3 import Mystem

import nltk
from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords


#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.model_selection import train_test_split

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def Lemmatize(src: list):
    ''' Лемматизирует переданный датасет
    '''
    text_nomalized = ' '.join(src).lower() 

    m = Mystem()
    lemmas = m.lemmatize(text_nomalized)
    
    lemmas = [lemma for lemma in lemmas if not lemma == ' ' ]
    
    return lemmas

if __name__=='__main__':
    
    data = pd.read_csv('dataframe.csv')
    data = data.head(10)
    
    data.dropna(inplace=True)
    remove_non_alphabets = lambda x: re.sub(r'[^а-яА-Я]',' ',str(x))
    
    tokenize = lambda x: word_tokenize(x, language = "russian")
    
    ps = PorterStemmer()
    stem = lambda w: [ ps.stem(x) for x in w ]
    
    data['text_of_comment'] = data['text_of_comment'].apply(remove_non_alphabets)
    data['text_of_comment'] = data['text_of_comment'].apply(tokenize) # [ word_tokenize(row) for row in data['email']]
    data['text_of_comment'] = data['text_of_comment'].apply(stem)
    data['text_of_comment'] = data['text_of_comment'].apply(Lemmatize)
    data['text_of_comment'] = data['text_of_comment'].apply(lambda x: ' '.join(x))
    
    print(data.head())