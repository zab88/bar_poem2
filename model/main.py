# -*- coding: utf-8 -*-
import pymysql
from PoemModel import PoemModel
import collections
import operator

AllPoems = []

#read poems
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='sample', charset='utf8')
curDB = conn.cursor()

# curDB.execute("SELECT * FROM words WHERE html LIKE '%2 variant%' LIMIT 100") #35, 68
#curDB.execute("SELECT * FROM poem WHERE is_draft=0 LIMIT 20")
curDB.execute("SELECT * FROM poem WHERE is_draft=0")
i = 0
for r in curDB.fetchall():
    #print(r[2])
    #print(r[2])
    new_poem = PoemModel(r[2].encode('utf-8'), r[1].encode('utf-8'))
    AllPoems.append(new_poem)

#searchin for homonyms and undefined words
file = open('../out/homonyms5.html', 'w+')
for poem in AllPoems:
    file.write("<p style='font-weight:bold'>"+poem.original_title+"<p>")
    homonym_html, all_homonyms = poem.get_poem_homonyms()
    file.write( str(homonym_html) )
    # continue
    # print('=======!=====================')
    # print(poem.original_title)
    # for gg in poem.lines:
    #     print(gg.line_original)

    # for line in poem.lines:
    #     print(line.line_original)

file.close()

ff = open('../out/list.txt', 'w+')
sorted_homonyms = sorted(all_homonyms.iteritems(), key=operator.itemgetter(1))
sorted_homonyms.reverse()
for el in sorted_homonyms:
    ff.write( str(el[0].encode('utf-8')) + ' ' + str(el[1]) + "\n" )
    # print(el[0])
    # print(el[1])
ff.close()
