# -*- coding: utf-8 -*-
import pymorphy2

# new_lines = []
# file = open('nationality.txt', 'r')
# for line in file.readlines():
#     l = line.strip()
#     if l is '': continue
#     l = l.decode('utf-8').lower().encode('utf-8')
#     new_lines.append(l)
#     print(l)
# file.close()
#
# file = open('all_nationality.txt', 'w')
# for l in new_lines:
#     file.write(l + "\n")
# file.close()
# exit()

morph = pymorphy2.MorphAnalyzer()


generated_nationalities = []

file = open('all_nationality.txt', 'r')
for line in file.readlines():
    line = line.strip() #deleting unnecessary spaces
    if ' ' in line: continue
    parsed = morph.parse( line.decode('utf-8') )
    if len(parsed) == 0: continue
    parsed = parsed[0]
    res = parsed.inflect({'sing', 'nomn'})
    if res is None: continue #continue if can not generate form
    print(res.word)

    # generated_nationalities.append( line.encode('utf-8') +u', '+res.word.encode('utf-8'))
    generated_nationalities.append( line + ', ' + res.word.encode('utf-8') )
file.close()

#writing to file
file_generated = open('generated_nationalities.txt', 'w')
file_generated.write( "\n".join(generated_nationalities) )
file_generated.close()

exit()


morph = pymorphy2.MorphAnalyzer()
parsed = morph.parse(u'китайцы')[0]

# res2 = parsed.inflect({'femn sing'})
res2 = parsed.inflect({'sing', 'nomn'})
print(res2)
print(res2.word)
exit()

res = parsed.lexeme
for r in res:
    print(r.word)

