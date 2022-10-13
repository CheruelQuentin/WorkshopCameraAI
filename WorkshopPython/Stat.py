from FirebaseQuentin.connect import getEmotion
import pandas as pd
import time

def count(file):
    #('angry', 'disgust', 'retard', 'happy', 'sad', 'surprise', 'neutral')

    fic = open(file, "r")
    content = fic.readlines()
            
    print("angry :", content.count("angry\n"))
    print("disgust :", content.count("disgust\n"))
    print("fear :", content.count("fear\n"))
    print("happy :", content.count("happy\n"))
    print("sad :", content.count("sad\n"))
    print("surprise :", content.count("surprise\n"))
    print("neutral :", content.count("neutral\n"))
    fic.close()

def stat(filename):
    fich = open(filename, "r")
    cont = fich.readlines()
    print("Pourcentage de personne happy : ", round(cont.count("happy\n")/len(cont),1)*100,"%")
    print("Pourcentage de personne disgust : ", round(cont.count("disgust\n")/len(cont),1)*100,"%")
    print("Pourcentage de personne fear : ", round(cont.count("fear\n")/len(cont),1)*100,"%")
    print("Pourcentage de personne angry : ", round(cont.count("angry\n")/len(cont),1)*100,"%")
    print("Pourcentage de personne sad : ", round(cont.count("sad\n")/len(cont),1)*100,"%")
    print("Pourcentage de personne surprise : ", round(cont.count("surprise\n")/len(cont),1)*100,"%")
    print("Pourcentage de personne neutral : ", round(cont.count("neutral\n")/len(cont),1)*100,"%")
    fich.close()

def StatFirebase():
    lst = []
    lstEmo = []
    lst = getEmotion()
    for item in lst:
        lstEmo.append(item["emotion"])

    print("Pourcentage de personne happy : ", round(lstEmo.count("happy")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne disgust : ", round(lstEmo.count("disgust")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne fear : ", round(lstEmo.count("fear")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne angry : ", round(lstEmo.count("angry")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne sad : ", round(lstEmo.count("sad")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne surprise : ", round(lstEmo.count("surprise")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne neutral : ", round(lstEmo.count("neutral")/len(lstEmo),1)*100,"%")

def StatFirebaseDay(day):
    lst = []
    lstEmo = []
    lst = getEmotion()
    for item in lst:
        if str(item["jours"])[0:10] == day:
            lstEmo.append(item["emotion"])

    print("Pourcentage de personne happy : ", round(lstEmo.count("happy")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne disgust : ", round(lstEmo.count("disgust")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne fear : ", round(lstEmo.count("fear")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne angry : ", round(lstEmo.count("angry")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne sad : ", round(lstEmo.count("sad")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne surprise : ", round(lstEmo.count("surprise")/len(lstEmo),1)*100,"%")
    print("Pourcentage de personne neutral : ", round(lstEmo.count("neutral")/len(lstEmo),1)*100,"%")

def StatFirebaseTime(day="", hours=""):
    lst = []
    lstEmo = []
    lst = getEmotion()
    for item in lst:
        if day != "" and hours != "":
            if str(item["jours"])[0:10] == day and str(item["jours"])[11:13] == hours:
                lstEmo.append(item["emotion"])
    
        if day != "" and hours == "":
            if str(item["jours"])[0:10] == day:
                lstEmo.append(item["emotion"])
        if day == "" and hours != "":
            if str(item["jours"])[11:13] == hours:
                lstEmo.append(item["emotion"])

    if not(lstEmo):
        print("Pas de stat pour ces paramètres ou pas de paramètres saisis")
    else:
        print("Pourcentage de personne happy : ", round(lstEmo.count("happy")/len(lstEmo),2)*100,"%")
        print("Pourcentage de personne disgust : ", round(lstEmo.count("disgust")/len(lstEmo),2)*100,"%")
        print("Pourcentage de personne fear : ", round(lstEmo.count("fear")/len(lstEmo),2)*100,"%")
        print("Pourcentage de personne angry : ", round(lstEmo.count("angry")/len(lstEmo),2)*100,"%")
        print("Pourcentage de personne sad : ", round(lstEmo.count("sad")/len(lstEmo),2)*100,"%")
        print("Pourcentage de personne surprise : ", round(lstEmo.count("surprise")/len(lstEmo),2)*100,"%")
        print("Pourcentage de personne neutral : ", round(lstEmo.count("neutral")/len(lstEmo),2)*100,"%")

def StatPandas():
    lst = []
    lst = getEmotion()
    df = pd.DataFrame.from_dict(lst, orient='columns')
    print(str(df.jours)[17:19])
    df["Day"] = str(df.jours)[6:16]
    df["H"] = str(df.jours)[17:19]
    df["H-m"] = str(df.jours)[17:22]
    df["H-m-s"] = str(df.jours)[17:25]
    df = df.drop(columns=['jours'])
    print(df)

#StatFirebaseTime("2022-10-13","14")


#StatPandas()

#stat("EmotionStat.txt")

