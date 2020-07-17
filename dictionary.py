import json 
import difflib
from difflib import get_close_matches
data = json.load(open("dictdata.json"))

def translate(word):
    newWord = word.lower()
    if newWord in data:
        newMeaning =data[newWord]
        return newMeaning
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(newWord, data.keys())) > 0:
        spellCheck = get_close_matches(newWord, data, n=3, cutoff = 0.8)
        ans = input("Did you mean %s? Enter Y for YES and N for NO: " %spellCheck[0])
        if ans == "Y":
            return data[spellCheck[0]]
        elif ans == "N": 
            return "Word not found. Please check the word you have entered."
        else :
            return "We didn't understand your entry. "
    else: 
        return "Word not found. Please check the word you have entered."

newInput = input("Enter the word: ")
newOutput = translate(newInput)

if type(newOutput) == list:
    for i in newOutput:
        print(i)
else: 
    print(newOutput)
