
##########Sentiment Analysis
 
#Data Import
import pandas as pd
from io import StringIO
import os
import random

ACTUAL_DIR = os.path.dirname(os.path.abspath(__file__))

input_data = pd.read_csv( ACTUAL_DIR + '\\Datasets\\User_Reviews\\User_movie_review.csv')


#Basic Details of the data
input_data.shape
input_data.columns
input_data.head(10)

#Frequency of sentiment col
input_data['class'].value_counts()

##########
#Creating Document Term Matrix

from sklearn.feature_extraction.text import CountVectorizer

"""
    Las siguientes variables se encargan de realizar la matriz de dtm, Document Term Matrix
    La cual, es la estructura de datos que se va a usar para los entrenamientos y testeos
"""
countvec1 = CountVectorizer()
dtm_v1 = pd.DataFrame(countvec1.fit_transform(input_data['text']).toarray(), columns=countvec1.get_feature_names(), index=None)
dtm_v1['class'] = input_data['class']
dtm_v1.head()

#############################################
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
#####Writing a Custom Tokenizer
stemmer = PorterStemmer()
def tokenize(text):
    text = stemmer.stem(text)               #stemming
    text = re.sub(r'\W+|\d+|_', ' ', text)    #removing numbers and punctuations and Underscores
    tokens = nltk.word_tokenize(text)       #tokenizing
    return tokens

countvec = CountVectorizer(min_df= 5, tokenizer=tokenize, stop_words=stopwords.words('english'))
dtm = pd.DataFrame(countvec.fit_transform(input_data['text']).toarray(), columns=countvec.get_feature_names(), index=None)
#Adding label Column
dtm['class'] = input_data['class']
dtm.head()  

test = countvec.get_feature_names()

###Building training and testing sets
df_train = dtm[:1900]
df_test = dtm[1900:]

################# Building Naive Bayes Model
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
X_train= df_train.drop(['class'], axis=1)
#Fitting model to our data
clf.fit(X_train, df_train['class'])

#Accuracy
X_test= df_test.drop(['class'], axis=1)
clf.score(X_test,df_test['class'])

#Prediction
#pred_sentiment=clf.predict(df_test.drop('class', axis=1))

##########
# Creating predict function - data is a string
def predict( data ):
    """
        predict: Toma los datos como una cadena y clasifica la polaridad.
        Positiva o Negativa.
    """
    df = pd.read_csv(StringIO( "class,text\n" + "_," + " " + data))
    countvec = CountVectorizer(min_df= 5, tokenizer=tokenize, stop_words=stopwords.words('english'), vocabulary=test)
    dtm = pd.DataFrame(countvec.fit_transform(df['text']).toarray(), columns=countvec.get_feature_names(), index=None)
    dtm['class'] = df['class']
    print( clf.predict_proba( dtm.drop('class', axis=1) ) )
    return clf.predict( dtm.drop('class', axis=1) )

def predict_proba( data ):
    """
        predict_proba: Toma los datos como una cadena y clasifica la polaridad.
        Sin embargo, devuelve los valores en forma de probabilidad por polaridad.
    """
    df = pd.read_csv(StringIO( "class,text\n" + "_," + " " + data))
    countvec = CountVectorizer(min_df= 5, tokenizer=tokenize, stop_words=stopwords.words('english'), vocabulary=test)
    dtm = pd.DataFrame(countvec.fit_transform(df['text']).toarray(), columns=countvec.get_feature_names(), index=None)
    dtm['class'] = df['class']
    return clf.predict_proba( dtm.drop('class', axis=1) )

def sa_measure( replies_file ):
    """
        sa_measure: Es la función que centraliza las demás, parsea los datos y mide
        la polaridad de las oraciones ingresadas.
    """
    # Sentences of the file.
    reps = list();
    sentiments = list()
    with open(replies_file, 'r') as file:
        for row in file.readlines():
            reps.append(row.strip("\n"))
    with open(replies_file.replace(".txt","_SA.txt"), 'w+') as resultFile:
        for reply in reps:
            val = predict_proba(reply)
            if val[0][0] > 0.7: 
                pred = 'Neg'; sentiments.append(1-val[0][0])
            elif val[0][1] > 0.7: 
                pred = 'Pos'; sentiments.append(val[0][1])
            else: 
                pred = 'Neut'
                if val[0][0] > val[0][1]:
                    sentiments.append(random.uniform(0.31,0.5))
                else:
                    sentiments.append(random.uniform(0.5,0.69))
            resultFile.write(reply + "," + pred + "\n")
    return sentiments
