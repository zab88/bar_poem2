import pymysql
import pymorphy2
import nltk
import string

import functions

# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='pushkin', charset='utf8')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='sample', charset='utf8')
curDB = conn.cursor()

# curDB.execute("SELECT * FROM words WHERE html LIKE '%2 variant%' LIMIT 100") #35, 68
curDB.execute("SELECT * FROM poem WHERE is_draft = 0")

file = open('count_animacy.txt', 'w+')
for r in curDB.fetchall():
    animate_num = 0
    not_animate_num = 0

    text = r[1]
    tokens = nltk.word_tokenize(text)
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    for word in tokens:
        print(word)
        is_animate, is_noun = functions.isAnimateNoun2(word)
        if is_noun:
            if is_animate:
                animate_num += 1
            else:
                not_animate_num += 1

    # file.write(r[2].decode('utf-8')+' nouns:'+(animate_num) + '/' + (animate_num+not_animate_num) )
    file.write(r[2].encode('utf-8')+' nouns:'+str(animate_num).encode('utf-8') + '/' + str(animate_num+not_animate_num).encode('utf-8') )
    file.write("\n")
    #print(tokens[0])
    # exit()
file.close()
print(not_animate_num)
print(animate_num)