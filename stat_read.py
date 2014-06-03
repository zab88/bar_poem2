# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import pymysql

# file = open('pushkin/stat_01.html', 'r')
# html = file.read()
# file.close()

all_poems = []
poem = []
line_number = 0
counter = 0
for line in open('pushkin/stat_01.html', 'r'):
    line_number+=1
    if line_number > 4206 and line_number < 9130:
        ll = line.strip()
        ll = re.sub('<[^>]*>', '', ll)
        if ll == "": continue;
        #filling
        # if counter > 0 and ll == "":
        #     counter += 1
        # elif counter > 0:
        #     poem.append(ll)

        if counter > 0:
            poem.append(ll)

        if re.match("\d+\.", ll):
            #print(ll)
            counter = 6
            all_poems.append(poem)
            poem = []


        counter -= 1

all_poems.pop(0)
# print(len(all_poems))
# for el in all_poems[618]:
# for el in all_poems[414]:
#     print el
# print("------")
# for el in all_poems[415]:
#     print el
# exit()

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='pushkin', charset='utf8')
curDB = conn.cursor()
for k, el in enumerate(all_poems):
    #curDB.execute("""INSERT INTO `poems` (`word`) VALUES (%s)""", (k))
    curDB.execute("""INSERT INTO  `poems` (
        `id` ,
        `name` ,
        `year_start` ,
        `year_end` ,
        `strok` ,
        `razmer` ,
        `strofika`
        )
        VALUES (%s, %s, %s, 0, %s, %s, %s)""", (str(k+1), el[0], el[1], el[2], el[3], el[4]))
    conn.commit()

curDB.close()
conn.close()
