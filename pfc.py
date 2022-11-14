#DEBUT

#On admet la fonction input() qui renvoit la valeur donner par le player
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe
from random import randint

#Définir une fonction pierreFeuilleCiseaux qui permet au joueur de faire son choix
def pierreFeuilleCiseaux():
    #Écrire les règles du jeu
    print("règles du jeu")
    #Créer un tableau game = ["pierre","feuille","ciseaux"]
    #Initialiser une variable cpuChoice à None
    cpuChoice = None
    #Initialiser une variable playerChoice à None
    playerChoice = None
    #Initialiser une variable scorePlayer à 0
    scorePlayer = 0
    #Initialiser une variable scoreCpu à 0
    scoreCpu = 0
    #---------------------------------------Initialiser une variable playAgain à 'y'
    #Tant que scorePlayer < 2 et scoreCpu < 2
    while scorePlayer < 2 and scoreCpu < 2:
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction random()
        cpuChoice = int(randint(0, 2))
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Que faites-vous ce tour ? ")
        playerChoice = float(input("0 pour pierre, 1 pour feuille ou 2 pour ciseaux: "))
        #Si playerChoice est égale à cpuChoice
        if playerChoice == cpuChoice:
            #Alors écrire "Egalité!"
            print("bah non, vous avez fait la même")
        #Sinon si playerChoice égale à 0
        elif playerChoice == 0:
            #Si cpuChoice égale à 2
            if cpuChoice == 2:
                #Alors écrire "Vous avez gagné!"
                print("gg mon reuf, il a joué les ciseaux ce boulet")
                #Incrémenter scorePlayer de 1
                scorePlayer = scorePlayer + 1
            #Sinon 
            else:
                #Alors, écrire "Vous avez Perdu!"
                print("raté du con")
                #Incrémenter scoreCpu de 1
                scoreCpu = scoreCpu + 1
        #Sinon si playerChoice égale à 1
        elif playerChoice == 1:
            #Si cpuChoice égale à 0
            if cpuChoice == 0:
                #Alors écrire "Vous avez gagné!"
                print("bien joué il a pas penser que tu jouerais la feuille")
                #Incrémenter scorePlayer de 1
                scorePlayer = scorePlayer + 1
            #Sinon 
            else:
                #Alors, écrire "Vous avez Perdu!"
                print("you lose pauv' merde")
                #Incrémenter scoreCpu à 1
                scoreCpu = scoreCpu + 1
        #Sinon si playerChoice égale à 2
        elif playerChoice == 2:
            #Si cpuChoice égale de 1
            if cpuChoice == 1:
                #Alors écrire "Vous avez gagné!"
                print("Alors là c'est bien joué, il avait pas vu venir le ciseau")
                #Incrémenter scorePlayer de 1
                scorePlayer = scorePlayer + 1
            #Sinon
            else:
                #Alors écrire "Vous avez Perdu!"
                print("tu pers face à un toaster, ta mère as honte de toi")
                #Incrémenter scoreCpu de 1
                scoreCpu = scoreCpu + 1
        #Sinon : playerChoice ne renvoi à aucun élément du tableau game
        else:
            #Alors écrire "Choix impossible!"
            print("t'as trois option et tu trouve le moyen de te foirer... débile")

    #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
    print(scorePlayer, "/", scoreCpu, ", bah voilà les scores, mouais pas ouf")

            #------------------------BONUS PEUT-ÊTRE FINI (à valider)------------------------
            #Tant que playAgain est différent 'y' ou 'n'
                #Assigner la résultante de l'appel d'input("Voulez vous rejouer (y/n) ? ") à la variable playAgain
                #Si playAgain différent de 'y' ou 'n'
                    #Alors afficher un message d'erreur

#Executer la fonction pierreFeuilleCiseaux
pierreFeuilleCiseaux()

#FIN






#DEBUT

#On admet la fonction input() qui renvoit la valeur donner par le player
#On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe

#Définir une fonction pierreFeuilleCiseaux qui permet au joueur de faire son choix
    #Écrire les règles du jeu
    #Initialiser une variable cpuChoice à None
    #Initialiser une variable playerChoice à None
    #Initialiser une variable scorePlayer à 0
    #Initialiser une variable scoreCpu à 0

    #

    #---------------------------------------Initialiser une variable playAgain à 'y'
    #Tant que scorePlayer < 2 et scoreCpu < 2
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction random()
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Que faites-vous ce tour ? ")
        #Si playerChoice est égale à cpuChoice
            #Alors écrire "Egalité!"
        #Sinon si playerChoice égale à 0
            #Si cpuChoice égale à 2
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon 
                #Alors, écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon si playerChoice égale à 1
            #Si cpuChoice égale à 0
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon 
                #Alors, écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu à 1
        #Sinon si playerChoice égale à 2
            #Si cpuChoice égale de 1
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon
                #Alors écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon : playerChoice ne renvoi à aucun élément du tableau game
            #Alors écrire "Choix impossible!"

    #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 

            #------------------------BONUS PEUT-ÊTRE FINI (à valider)------------------------
            #Tant que playAgain est différent 'y' ou 'n'
                #Assigner la résultante de l'appel d'input("Voulez vous rejouer (y/n) ? ") à la variable playAgain
                #Si playAgain différent de 'y' ou 'n'
                    #Alors afficher un message d'erreur

#Executer la fonction pierreFeuilleCiseaux

#FIN