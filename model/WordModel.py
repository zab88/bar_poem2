# -*- coding: utf-8 -*-
import pymorphy2
import pymysql
MorphEngine = pymorphy2.MorphAnalyzer()
HomonimArray = []

#read homonyms
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='sample', charset='utf8')
curDB = conn.cursor()

# curDB.execute("SELECT * FROM words WHERE html LIKE '%2 variant%' LIMIT 100") #35, 68
curDB.execute("SELECT * FROM words WHERE html LIKE '%2 variant:%'")
i = 0
for r in curDB.fetchall():
    HomonimArray.append(r)

class WordModel(object):
    word_original = ''
    isHomonim = False
    id_zaliznyak = 0
    is_debug = False
    word_lat = ''

    parsed = []

    def __init__(self, word_original):
        self.word_original = word_original.replace(",", "")
        self.word_original = self.word_original.replace(":", "")

        self.word_original = self.word_original.decode('utf-8')
        self.makeMorphAnalyse()

    def makeMorphAnalyse(self):
        global MorphEngine, HomonimArray
        self.parsed = MorphEngine.parse( self.word_original )
        if len(self.parsed) > 1:
            self.isHomonim = True
            #searh in starling
            self.searh_starling_rinet(self.word_original)
            #!!
            # if self.id_zaliznyak > -1:
            #     print(HomonimArray[self.id_zaliznyak][2])
            # else:
            #     print(self.word_original)
            #out
            if self.is_debug:
                print(self.word_original)
                for variant in self.parsed:
                    print(variant.normal_form)
                print('----------------------------------')

    def searh_starling_rinet(self, word):
        global HomonimArray
        res = -1
        for k, r in enumerate(HomonimArray):
            if r[1] == word:
                self.id_zaliznyak = k
                self.word_lat = r[2]
                res = k
        return res