import pickle
import json

def desirialize_from_pickle():
    with open("c:\group.pickle",'rb') as f:
        result=pickle.load(f)
        return result

def desirialize_from_json():
    with open("c:\group.json",'r', encoding='utf-8') as f:
        result=json.load(f)
        return result

print(desirialize_from_pickle())
print(desirialize_from_json())


