import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import datetime


cred = credentials.Certificate("d:\save\EPSI\I1\workshop\Firebase\workshopcameraai-firebase-adminsdk-4mw40-cd5d7dda33.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'users').document(u'SANSTITRE')
doc_ref.set({
    u'first': u'Tison',
    u'last': u'Romuald',
    u'born': 1992
})


def insertEmotion(emotion):
    doc_ref = db.collection(u'emotions').document()
    doc_ref.set({
        u'jours': datetime.datetime.now(),
        u'emotion': emotion,
    })
    print("Ok insert")

insertEmotion("happy")