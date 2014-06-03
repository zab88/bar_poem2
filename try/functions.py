# -*- coding: utf-8 -*-
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def isAnimateNoun2(word):
    #globals(morph)
    parsed = morph.parse( word )

    noun_found = False

    #if not parsed, return False
    if len(parsed) == 0:
        return False, noun_found

    #let's check if word is Noun.
    #if we have multiple variations, let's take first
    for variant in parsed:
        if {'NOUN'} in variant.tag:
            if variant.tag.animacy is not None:
                noun_found = True
                if variant.tag.animacy == "anim": #inan, anim
                    return True, noun_found


    return False, noun_found

#print(isAnimateNoun2(u'динозавр'))

def isAnimateNoun(word):
    morph = pymorphy2.MorphAnalyzer()
    parsed = morph.parse( word )

    #if not parsed, return False
    if len(parsed) == 0:
        return False

    #let's check if word is Noun.
    #if we have multiple variations, let's take first
    noun_word = None
    for variant in parsed:
        # if {'NOUN'} in variant.tag:
        #     noun_word = variant
        #     break
        if variant.tag.animacy is not None and variant.tag.animacy == "anim": #inan, anim
            print variant.tag.animacy
            print(variant.word)
            print('!!!!')
            return True

    if noun_word is None:
        return False

    #checking forms
    #множественное число родительного и винительного падежа
    gent_case = noun_word.inflect({'plur', 'gent'})
    accs_case = noun_word.inflect({'plur', 'accs'})
    if gent_case is None or accs_case is None:
        return False

    if gent_case.word == accs_case.word:
        print(gent_case.word)
        return True
    else:
        return False

#print(isAnimateNoun2(u'динозавр'))