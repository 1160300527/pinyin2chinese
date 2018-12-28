import json
import copy

PATH = "resource"
DICTIONARY_PATH = PATH+"/dictionary.json"
TRANSFER_PATH = PATH+"/transfermatrix.json"

def loadFile(path):
    with open(path) as file:
        return json.load(file)


def viterbi(transfer,dictionary,PinYin):
    pinyin = PinYin.strip().split()
    prestate = {}
    state = {}
    preKey = []
    for word in pinyin:
        if word in dictionary:
            state = {}
            if len(prestate)>0:
                keys = {}
                for the_state in dictionary[word]:
                    possibility = 0
                    key = None
                    shoot = dictionary[word][the_state]
                    for pre in prestate:
                        if not(pre in transfer and the_state in transfer[pre]):
                            continue
                        temp_pos = prestate[pre]*shoot*transfer[pre][the_state]*shoot
                        if(temp_pos>possibility):
                            key = pre
                            possibility = temp_pos
                    if key!=None:
                        keys[the_state] = key
                        state[the_state] = possibility
                preKey.append([keys])
                prestate = state
            else:
                prestate = dictionary[word]
        else:
            print("该拼音不存在："+word)
            break
    hanzi = ""
    temp = ""
    possibility = 0
    for final_state in state:
        if state[final_state]>possibility:
            possibility = state[final_state]
            temp = final_state
    hanzi=temp
    while len(preKey):
        temp = preKey.pop()[0][temp]
        hanzi = temp+hanzi
    return hanzi
        


if __name__ == "__main__":
    dictionary = loadFile(DICTIONARY_PATH)
    transfer_matrix = loadFile(TRANSFER_PATH)
    print(viterbi(transfer_matrix,dictionary,"cong qian you ge ren"))