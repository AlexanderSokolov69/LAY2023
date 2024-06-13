#!/usr/bin/env python3
# coding:utf-8
def template(template, data):
    letters = 'aeouiy'
    newdata= []
    i = 0
    for sim in template:
        if sim == '0':
            newdata = [w for w in data if len(w) > i and w[i] in letters]
        elif sim == '1':
            newdata = [w for w in data if len(w) > i and w[i] not in letters]
        elif sim == '?':
            newdata = [w for w in data if len(w) > i]
        elif sim == '*':
            newdata = [w for w in data if len(w) >= len(template) - 1]
            i = -(len(template) - i)
        data = newdata.copy()
        i += 1
    if data:
        return data[0]
    else:
        return ''


print(template('????*?11?11?', ['agenda', 'performance', 'ease', 'quietness', 'courtroom', 'grade', 'handbag', 'loneliness', 'bet', 'wake', 'point', 'elaborate', 'as', 'meal', 'suburban', 'boil', 'point', 'unpunished']))
