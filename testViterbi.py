from pypinyin import lazy_pinyin
from Viterbi import viterbi,dict_and_transfer
import sys

PATH = "resource"
TEST_PATH = PATH+"/test.txt"
DICTIONARY_PATH = PATH+"/dictionary.json"
TRANSFER_PATH = PATH+"/transfermatrix.json"

def getTest(path):
    with open(path,encoding="utf-8") as file:
        return file.readlines()

def generate_pinyin(lines):
    pinyin = []
    for line in lines:
        line = line.strip()
        pinyin.append(lazy_pinyin(line,errors="ignore"))
    return pinyin

def pinyin2hanzi(transfer,dictionary,pinyin,num):
    hanzi = []
    for py in piniyin:
        hz = viterbi(transfer,dictionary,py,num)
        hanzi.append(hz)
    return hanzi

def compare(real_hanzi,hanzi,num):
    sum = 0
    right = 0
    for i in range(len(real_hanzi)):
        line = real_hanzi[i].strip()
        hz = hanzi[i]
        sum+=len(line)
        max_right=0
        for j in range(len(hz)):
            temp_right = 0
            viterbi_hanzi = hz[j]
            for k in range(len(line)):
                if(line[k]==viterbi_hanzi[k]):
                    temp_right+=1
            if(temp_right>max_right):
                max_right=temp_right
        right+=max_right
    print(right/sum)

if __name__ == "__main__":
    if len(sys.argv)<2:
        path = TEST_PATH
    else:
        path = sys.argv[1]
    num = 4
    if len(sys.argv)>2:
        num=sys.argv[2]
    lines = getTest(path)
    dictionary,transfer = dict_and_transfer(DICTIONARY_PATH,TRANSFER_PATH)
    piniyin=generate_pinyin(lines)
    viterbi_hanzi = pinyin2hanzi(transfer,dictionary,piniyin,num)
    with open(PATH+"/test_result.txt","w",encoding="utf-8") as file:
        for line in viterbi_hanzi:
            file.write(line[0]+"\n")
    compare(lines,viterbi_hanzi,num)