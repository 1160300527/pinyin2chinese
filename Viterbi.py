import sys
import json
import copy
import operator

PATH = "resource"
DICTIONARY_PATH = PATH+"/dictionary.json"
TRANSFER_PATH = PATH+"/transfermatrix.json"
DONT_EXIST=0

def loadFile(path):
    with open(path) as file:
        return json.load(file)

def dict_and_transfer(dictionary,transfer):
    return loadFile(dictionary),loadFile(transfer)


def viterbi(transfer,dictionary,pinyin,num):
    prestate = {}
    state = {}
    preKey = []
    #遍历每个拼音
    for word in pinyin:
        #若字典中存在该拼音，则进行处理
        if word in dictionary:
            state = {}
            #若为初始状态，则需要将其前驱状态设置为该状态
            if len(prestate)>0:
                keys = {}
                #利用viterbi算法，寻找概率每个当前状态对应的最大的路径
                for the_state in dictionary[word]:
                    possibility = 0
                    key = None
                    shoot = dictionary[word][the_state]
                    #确定概率最大的前驱状态（前一个汉字）
                    for pre in prestate:
                        #前驱状态节点必须在转移矩阵中，且prestate->this_state必须有对应概率
                        if not(pre in transfer and the_state in transfer[pre]):
                            continue
                        temp_pos = prestate[pre]*transfer[pre][the_state]*shoot
                        if(temp_pos>possibility):
                            key = pre
                            possibility = temp_pos
                    if key!=None:
                        keys[the_state] = key
                        state[the_state] = possibility
                    else:
                        rand = prestate.popitem()
                        keys[the_state] = rand[0]
                        state[the_state] = DONT_EXIST
                        prestate[rand[0]]=rand[1]
                preKey.append([keys])
                prestate = state
            else:
                prestate = dictionary[word]
                state = prestate
        else:
            print("该拼音不存在："+word)
            return
    sorted_possibility = sorted(state.items(),key = operator.itemgetter(1),reverse=True)
    if(num>len(sorted_possibility)):
        num=len(sorted_possibility)
    hanzi=[""]*num
    temp=[""]*num
    for i in range(num):
        hanzi[i]=sorted_possibility[i][0]
        temp[i]=hanzi[i]
    while len(preKey):
        wordstate = preKey.pop()
        for i in range(num):
            temp[i] = wordstate[0][temp[i]]
            hanzi[i] = temp[i]+hanzi[i]
    return hanzi
        


if __name__ == "__main__":
    dictionary,transfer_matrix=dict_and_transfer(DICTIONARY_PATH,TRANSFER_PATH)
    pinyin = "ha er bin gong ye da xue ji suan ji ke xue yu ji shu xue yuan"
    if len(sys.argv)>1:
        pinyin=sys.argv[1]
    print(pinyin)
    pinyin = pinyin.strip().split()
    print(viterbi(transfer_matrix,dictionary,pinyin,5))