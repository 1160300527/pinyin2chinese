from pypinyin import lazy_pinyin
import json

dict = {}
with open('sentences.txt',encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        words = line.strip()
        if(line.isspace()):
            continue
        PinYin = lazy_pinyin(words,errors="ignore")
        every_word = list(words)
        for word in words:
            print(word)
        print(len(PinYin))
        print(every_word)
        break
