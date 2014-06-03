# -*- coding: utf-8 -*-
import pymysql

f = open('pushkin/pushkin_aleksandr_polnoe_sobranie_stihotvoreniy.txt', 'r')
#all_text = f.read()
all_lines = f.readlines()
f.close()
# print(all_lines[14]);exit()

def make_poems(lines):
    made_poems = []

    current_poem_text = 'first!'
    current_poem_name = ''
    for l in lines:
        if l[0] == ' ' or l[0] == "\t":
            #deleting leading tabs
            l = l.replace("\t", "")
            current_poem_text += l

            # if current_poem_name[0:5] == "* * *":
            #     print(current_poem_name);exit()
            if current_poem_name[0:5] == "* * *":
                #print(l)
                current_poem_name = l
                current_poem_name = current_poem_name.replace("\n", '').strip()
                if current_poem_name[-1] in (",", ";", ".", "?", ":", "!"):
                    current_poem_name = list(current_poem_name)
                    current_poem_name[-1] = ''
                    current_poem_name = "".join(current_poem_name)
                    current_poem_name += "..."
                else:
                    current_poem_name += "..."
                #print(current_poem_name)
        elif l[0] == "\n":
            continue
        else:
            made_poems.append( {'name':current_poem_name, 'text':current_poem_text} )
            current_poem_name = l
            current_poem_name = current_poem_name.replace("\n", '')
            current_poem_text = ''
    return made_poems

made_poems = make_poems(all_lines)
# kmd = 200
# print(made_poems[kmd]['name'])
# print(made_poems[kmd]['text'])
# exit()


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='pushkin', charset='utf8')
curDB = conn.cursor()

# curDB.execute("SELECT * FROM words WHERE html LIKE '%2 variant%' LIMIT 100") #35, 68
curDB.execute("SELECT * FROM poems")
i = 0
for r in curDB.fetchall():
    for el in made_poems:
        if el['name'] == r[1].encode('utf-8'):
            # if el['name'][-3:] == "...":
            #     print(el['name'])
            #     print(el['text'])
            # print(el['name'])
            # print(el['text'])
            i += 1

            #ok, found, let's write to DB
            curDB.execute("""UPDATE `poems` SET `poem_text` = %s WHERE  `id` = %s """, (el['text'], str(r[0])))
            conn.commit()

print(i)
    # print(r[1])
    # pos = all_text.find( "\n"+r[1].encode('utf-8') )
    # if pos > 0:
    #     print(r[1])
    #     print(pos)
    #     print(i)
    #     i+=1
    #     #ok, first position found, let's find next position
    #     pos2 = all_text.find()