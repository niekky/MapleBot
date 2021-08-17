import json

with open ("E:\HDNN\2021\TechRMIT\FoxBot\foxPython\EntitiesTagger\tagFolder\tagtrain.json","r",encoding="utf-8") as f:
    data=json.load(f)

dict={}
l=[]
count=0
for each in data["corpus"]["NERtag"]:
    for i in each:
        l.append(i)

for i in l:
    dict[i]=l.count(i)

for i in dict:
    print(i,dict[i])