# -*- coding: utf-8 -*-
import nltk
import string
from WordModel import WordModel
stopwords = nltk.corpus.stopwords.words('russian')
# stopwords.extend([u'ТАК'.encode('utf-8'), u'ЧТО'.encode('utf-8'), u'ВОТ'.encode('utf-8'), u'ЭТО'.encode('utf-8'), u'КАК'.encode('utf-8')])
# stopwords.extend([u'БЫТЬ'.encode('utf-8'), u'a'.encode('utf-8')])
stopwords.extend(['а'])


class LineModel():
    line_original = ''
    #words = []

    def __init__(self, line_original):
        self.line_original = line_original
        self.words = []
        self.__init_words__()

    def __init_words__(self):
        #tokenization
        global stopwords
        tokens = nltk.word_tokenize( self.line_original.decode('utf-8').lower().encode('utf-8') )
        tokens = [i for i in tokens if ( i not in string.punctuation )]
        tokens = [i for i in tokens if ( i not in stopwords )]
        for w in tokens:
            new_word_model = WordModel(w)
            #print(new_word_model.word_original)
            self.words.append(new_word_model)

    def getHighlightingHomonyms(self):
        homonym_exists = False
        #print(self.line_original)
        new_line = str(self.line_original)
        for w in self.words:
            if w.isHomonim:
                #print(w.word_original)
                homonym_exists = True
                new_line = self.highlight_words(new_line, w)
        if homonym_exists is True:
            return new_line
        else:
            return None


    def highlight_words(self, line, word):
        #print(line, word)
        line = line.decode('utf-8')
        word_to_replace = u"<a target='_blank' href='http://starling.rinet.ru/cgi-bin/morph.cgi?word=["+word.word_lat+u"]'>"+\
                          word.word_original+u"</a>"
        #word_to_replace = word_to_replace.encode('utf-8')
        #print(line, word_to_replace)
        line = line.replace(word.word_original, word_to_replace )

        line = line.encode('utf-8')
        return line

        # indexes = [i for i in range(len(line)) if line.startswith(word, i)]
        # length = len(word)
        # for id in indexes:
        #     new_line = ''
