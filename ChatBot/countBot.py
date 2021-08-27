import json
f = open('ChatBot\intentsVN.json', encoding="utf8")
data = json.load(f)
print(len(data["intents"]))