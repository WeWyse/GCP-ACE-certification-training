import pandas as pd
from random import randrange, sample


def main(n):
    data = pd.read_csv("Evaluation_test.csv",sep=";") #Récupère les données
    score =0 #Le score final obtenu
    number =0 #le numéro de la question

    questions = sample(range(1, len(data)+1), n)

    for i, number in enumerate(questions):
 
        # number = randrange(len(data)) #Choisis une des question au hasard
        print("\nQuestion {}".format(i+1)," sur {}:".format(n))
        print("____________________________")
        print(data["Question"][number]) #Affiche la question
        print("____________________________")
        for x in ["A","B","C","D","E"]:
            if(str(data[x][number])!="nan"):
                print("{}.".format(x)," {}".format(data[x][number])) #Affiche les réponses
        reponse = input("\nEntrez votre réponse: ")
        if (reponse == data["result"][number]):
            print("\nCORRECT. \n{} ".format(data["explanation"][number]))
            score+=1
        else:
            print("\nINCORRECT. \nla bonne réponse est {}".format(data["result"][number]),"\n{}".format(data["explanation"][number]))


    print("\nFin de série !\nScore: {}".format(score),"/ {}".format(n))
if __name__ == '__main__':
    n = int(input("Combien de question souhaitez-vous ?: "))
    main(n)