import json
import pickle
my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}

def serialize_to_pickle(a):
    print("Pickle: ", pickle.dumps(a))
    with open("group.pickle","wb" ) as fl:
        pickle.dump(a,fl)


def serialize_to_json(a):
    print("Json", json.dumps(a))
    with open("group.json",'w',encoding='utf-8') as fl:
        json.dump(a,fl)

serialize_to_pickle(my_favourite_group)
serialize_to_json(my_favourite_group)
#serialize_to_json():
#    with open()