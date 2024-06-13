#!/usr/bin/env python3
# coding:utf-8
import translate


en_ru = translate.Translator(to_lang='ru', from_lang='en')
ru_en = translate.Translator(to_lang='English', from_lang='Russian')

line = 'Кукушка купила капюшон'
for word in line.split():
    print(ru_en.translate(word))
