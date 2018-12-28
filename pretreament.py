from pypinyin import lazy_pinyin
import json

PATH = "resource"
DICTIONARY_PATH = PATH+"/dictionary.json"
TRANSFER_PATH = PATH+"/transfermatrix.json"
SENTENCE_PATH = PATH+"/sentences.txt"


def possibility(trans):
    for key in trans:
        sum = 0
        for t in trans[key]:
            sum+=trans[key][t]
        for t in trans[key]:
            trans[key][t]=trans[key][t]/sum


def addDictionary(dictionary,key,value):
    if key in dictionary:
        if value in dictionary[key]:
            dictionary[key][value]=dictionary[key][value]+1
        else:
            dictionary[key][value]=1
    else:
        dictionary[key]={value:1}


def getTransfer(path,dict_path,trans_path):
    dictionary = {}
    trans = {}
    with open(path,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            preword=None
            words = line.strip()
            if(line.isspace()):
                continue
            PinYin = lazy_pinyin(words,errors="ignore")
            every_word = list(words)
            for i in range(len(PinYin)):
                piny = PinYin[i]
                hanzi = every_word[i]
                addDictionary(dictionary,piny,hanzi)
                if preword!=None:
                    addDictionary(trans,preword,hanzi)
                preword = hanzi
    possibility(trans)
    possibility(dictionary)
    dict_file = open(dict_path,'w',encoding='utf-8')
    transfermatrix_file = open(trans_path,'w',encoding='utf-8')
    json.dump(dictionary,dict_file)
    json.dump(trans,transfermatrix_file)
    dict_file.close()
    transfermatrix_file.close()

if __name__ == "__main__":
    getTransfer(SENTENCE_PATH,DICTIONARY_PATH,TRANSFER_PATH)