import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import datetime


cred = credentials.Certificate(r"C:\Users\loicr\Desktop\EPSI\I1\workshop_Quentin\WorkshopPython\FirebaseQuentin\workshopcameraai-firebase-adminsdk-4mw40-cd5d7dda33.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def insertEmotion(emotion):
    doc_ref = db.collection(u'emotions').document()
    doc_ref.set({
        u'jours': datetime.datetime.now(),
        u'emotion': emotion,
    })
    print("Ok insert")

def getEmotion():
    list = []
    docs = db.collection(u'emotions').stream()
    for doc in docs:
        #print(f'{doc.to_dict()}')
        list.append(doc.to_dict())
    return list
        