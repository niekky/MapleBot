import json

with open ("E:/MLCourse/foxBot/foxPython/tagFolder/tagData.json","r",encoding="utf-8") as f:
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