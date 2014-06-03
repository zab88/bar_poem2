# -*- coding: utf-8 -*-
from LineModel import LineModel

class PoemModel(object):
    original_title = ''
    original_text = ''

    lines = []

    def __init__(self, original_title, original_text, years=[]):
        self.original_title = original_title
        self.original_text = original_text
        self.__init_lines__()
        # for line in self.lines:
        #     print(line.line_original)
        # exit()

    #splits text into lines
    def __init_lines__(self):
        lines = self.original_text.split("\n")
        for line in lines:
            new_line = LineModel(line)#.strip()
            self.lines.append(new_line)
            #print(self.lines[len(self.lines)-1].line_original)

    def get_poem_homonyms(self):
        out_html = ''
        for l in self.lines:
            #print(l.line_original)
            homonym_line = l.getHighlightingHomonyms()
            if homonym_line is not None:
                #print(homonym_line)
                # out_html += l + "<br />"
                return homonym_line
        return None