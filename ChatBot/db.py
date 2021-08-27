#TEST PLAYGROUND
from random import randint
def checker(sentence):
    #Set up
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore
    import random
    cred = credentials.Certificate("D:/a-Code/Ignite Niek/foxPython/ChatBot/android-firebase-1f1b8-firebase-adminsdk-wtlm2-7a0d32b4fc.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    #Example format
    def sentences(sub,item):
        sen1 = [f"Bạn đã thử {sub} {item} chưa?",
        f"Mình thấy {sub} {item} cũng được lắm nha!",
        f"Nhiều người thích {sub} {item} lắm đó!"]
        return sen1[random.randint(0,2)]
    #Things that db contains
    names = []
    docs = db.collection(u'bot').stream()
    for doc in docs:
        names.append(doc.id)
    #Check if the asked thing in list
    for word in sentence.split():
        if word in names:
            doc_ref = db.collection(u'bot').document(word)
            doc = doc_ref.get()
            if doc.exists:
                dictz = doc.to_dict()
                print(sentences(word,dictz["item"][randint(0,len(dictz["item"])-1)]))
                break
say = "bạn thích ăn món gì"
checker(say)
