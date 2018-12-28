import json

PATH = "resource"
DICTIONARY_PATH = PATH+"/dictionary.json"
TRANSFER_PATH = PATH+"/transfermatrix.json"

def loadFile(path):
    with open(path) as file:
        dictionary = json.load(file)


def viterbi(transformation,dictionary,PinYin):
    return 0

dictionary = loadFile("resource/dictionary.json")
