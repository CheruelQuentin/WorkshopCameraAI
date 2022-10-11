
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
    print("Pourcentage de personne happy : ", round(cont.count("happy\n")/len(cont),3),"%")
    print("Pourcentage de personne disgust : ", round(cont.count("disgust\n")/len(cont),3),"%")
    print("Pourcentage de personne fear : ", round(cont.count("fear\n")/len(cont),3),"%")
    print("Pourcentage de personne angry : ", round(cont.count("angry\n")/len(cont),3),"%")
    print("Pourcentage de personne sad : ", round(cont.count("sad\n")/len(cont),3),"%")
    print("Pourcentage de personne surprise : ", round(cont.count("surprise\n")/len(cont),3),"%")
    print("Pourcentage de personne neutral : ", round(cont.count("neutral\n")/len(cont),3),"%")

stat("EmotionStat.txt")


