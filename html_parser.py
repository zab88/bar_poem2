import pymysql
from bs4 import BeautifulSoup


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='sample', charset='utf8')
curDB = conn.cursor()
file = open('out/out.txt', 'w+')

# curDB.execute("SELECT * FROM words WHERE html LIKE '%2 variant%' LIMIT 100") #35, 68
curDB.execute("SELECT * FROM words WHERE html LIKE '%2 variant%'") #35, 68

res = 0
for r in curDB.fetchall():
    #print(r)
    #soup = BeautifulSoup(r[3])
    parts = r[3].split('variant')
    len_parts = len(parts)

    founded = {}
    for i in range(1, len_parts, 1):
        soup = BeautifulSoup(parts[i])

        #print(soup.prettify())
        #print '====================================='
        for td in soup.find_all('td'):
            found_accent = None
            if not td.string:
                continue
            no_accent = td.string.replace(u"'", u"")
            #print no_accent , r[1]
            if no_accent == r[1]:
                founded[i] = td.string
            #print(td.string)


    if len(founded) >= 2:
        first_item = founded.values()[0]
        for j, w in founded.items():
            if first_item != w:
                res += 1
                print w
                print first_item
                file.write(w.encode('utf-8') + ' ' + first_item.encode('utf-8') + "\n")
                break

curDB.close()
conn.close()
file.close()

#finally print res diff
print res