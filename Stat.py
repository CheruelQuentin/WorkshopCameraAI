
def count(file):
    #('angry', 'disgust', 'retard', 'happy', 'sad', 'surprise', 'neutral')

    fic = open(file, "r")
    content = fic.readlines()
            
    print("angry :", content.count("angry\n"))
    print("disgust :", content.count("disgust\n"))
    print("retard :", content.count("retard\n"))
    print("happy :", content.count("happy\n"))
    print("sad :", content.count("sad\n"))
    print("surprise :", content.count("surprise\n"))
    print("neutral :", content.count("neutral\n"))
    fic.close()

