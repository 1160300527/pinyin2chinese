from pypinyin import lazy_pinyin
import json

PATH = "resource"
DICTIONARY_PATH = PATH+"/dictionary.json"
TRANSFER_PATH = PATH+"/transfermatrix.json"
SENTENCE_PATH = PATH+"/sentences.txt"

def getTransfer(path,dict_path,trans_path):
    dict = {}
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
                if piny in dict:
                    dict[piny].append(hanzi)
                else:
                    dict[piny]=[hanzi]
                if preword!=None:
                    if preword in trans:
                        if hanzi in trans[preword]:
                            trans[preword][hanzi]=trans[preword][hanzi]+1
                        else:
                            trans[preword][hanzi]=1
                    else:
                        trans[preword]={hanzi:1}
                preword = hanzi
    for key in trans:
        for t in trans[key]:
            trans[key][t]=trans[key][t]/len(trans[key])
    dict_file = open(dict_path,'w',encoding='utf-8')
    transfermatrix_file = open(trans_path,'w',encoding='utf-8')
    json.dump(dict,dict_file)
    json.dump(trans,transfermatrix_file)
    dict_file.close()
    transfermatrix_file.close()

getTransfer(SENTENCE_PATH,DICTIONARY_PATH,TRANSFER_PATH)