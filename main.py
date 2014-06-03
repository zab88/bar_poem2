# -*- coding: utf-8 -*-
import nltk
import string
import pymorphy
#from nltk.corpus import stopwords
#import os
import pymysql

morph = pymorphy.get_morph('K:\databases\BAR\pymorfy')

file = open('pushkin/pushkin_aleksandr_polnoe_sobranie_stihotvoreniy.txt', 'r')
text = file.read()
file.close()
text = text.decode('utf-8')

#tokenization
tokens = nltk.word_tokenize(text)
tokens = [i for i in tokens if ( i not in string.punctuation )]

#making dictionary
pushkin_dict = {}
for i in tokens:
    key = i.replace('.', '')
    key = key.replace(u"«", '')
    key = key.replace(u'»', '')
    key = key.replace(u'…', '')
    key = key.lower()
    pushkin_dict[key] = 0

#put all in mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='pushkin', charset='utf8')
curDB = conn.cursor()
for k, el in pushkin_dict.items():
    curDB.execute("""INSERT INTO `words` (`word`) VALUES (%s)""", (k))
    conn.commit()

curDB.close()
conn.close()
