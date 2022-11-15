# #DEBUT

# #On admet la fonction input() qui renvoit la valeur donner par le player
# #On admet la fonction random() qui renvoi une valeur aléatoire comprise entre 0 et 2 existe
from random import randint

# #Définir une fonction pierreFeuilleCiseaux qui permet au joueur de faire son choix
# def pierreFeuilleCiseaux():
#     #Écrire les règles du jeu
#     print("règles du jeu")
#     #Créer un tableau game = ["pierre","feuille","ciseaux"]
#     #Initialiser une variable cpuChoice à None
#     cpuChoice = None
#     #Initialiser une variable playerChoice à None
#     playerChoice = None
#     #Initialiser une variable scorePlayer à 0
#     scorePlayer = 0
#     #Initialiser une variable scoreCpu à 0
#     scoreCpu = 0
#     #---------------------------------------Initialiser une variable playAgain à 'y'
#     #Tant que scorePlayer < 2 et scoreCpu < 2
#     while scorePlayer < 2 and scoreCpu < 2:
#         #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [1 , 3]
#         cpuChoice = randint(1, 3)
#         #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction float(input("1 pour pierre, 2 pour feuille ou 3 pour ciseaux: "))
#         playerChoice = float(input("1 pour pierre, 2 pour feuille ou 3 pour ciseaux: "))
#         #Si playerChoice est égale à cpuChoice
#         if playerChoice == cpuChoice:
#             #Alors écrire "Egalité!"
#             print("bah non, vous avez fait la même")
#         #Sinon si playerChoice égale à 1
#         elif playerChoice == 1:
#             #Si cpuChoice égale à 3
#             if cpuChoice == 3:
#                 #Alors écrire "Vous avez gagné!"
#                 print("gg mon reuf, il a joué les ciseaux ce boulet")
#                 #Incrémenter scorePlayer de 1
#                 scorePlayer = scorePlayer + 1
#             #Sinon 
#             else:
#                 #Alors, écrire "Vous avez Perdu!"
#                 print("raté du con")
#                 #Incrémenter scoreCpu de 1
#                 scoreCpu = scoreCpu + 1
#         #Sinon si playerChoice égale à 2
#         elif playerChoice == 2:
#             #Si cpuChoice égale à 1
#             if cpuChoice == 1:
#                 #Alors écrire "Vous avez gagné!"
#                 print("bien joué il a pas penser que tu jouerais la feuille")
#                 #Incrémenter scorePlayer de 1
#                 scorePlayer = scorePlayer + 1
#             #Sinon 
#             else:
#                 #Alors, écrire "Vous avez Perdu!"
#                 print("you lose pauv' merde")
#                 #Incrémenter scoreCpu à 1
#                 scoreCpu = scoreCpu + 1
#         #Sinon si playerChoice égale à 3
#         elif playerChoice == 3:
#             #Si cpuChoice égale de 2
#             if cpuChoice == 2:
#                 #Alors écrire "Vous avez gagné!"
#                 print("Alors là c'est bien joué, il avait pas vu venir le ciseau")
#                 #Incrémenter scorePlayer de 1
#                 scorePlayer = scorePlayer + 1
#             #Sinon
#             else:
#                 #Alors écrire "Vous avez Perdu!"
#                 print("tu pers face à un toaster, ta mère as honte de toi")
#                 #Incrémenter scoreCpu de 1
#                 scoreCpu = scoreCpu + 1
#         #Sinon : playerChoice ne renvoi à aucun élément du tableau game
#         else:
#             #Alors écrire "Choix impossible!"
#             print("t'as trois option et tu trouve le moyen de te foirer... débile")

#     #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
#     print(scorePlayer, "/", scoreCpu, ", bah voilà les scores, mouais pas ouf")

#             #------------------------BONUS PEUT-ÊTRE FINI (à valider)------------------------
#             #Tant que playAgain est différent 'y' ou 'n'
#                 #Assigner la résultante de l'appel d'input("Voulez vous rejouer (y/n) ? ") à la variable playAgain
#                 #Si playAgain différent de 'y' ou 'n'
#                     #Alors afficher un message d'erreur

# #Executer la fonction pierreFeuilleCiseaux
# pierreFeuilleCiseaux()









#Définir la fonction infiniteGameMode qui permet de jouer au shifumi contre l'ordinateur à l'infinie
    #Initialiser une variable infiniteContinue à 1
    #Initialiser une variable cpuChoice à None
    #Initialiser une variable playerChoice à None
    #Initialiser une variable cpuScore à 0
    #Initialiser une variable playerScore à 0
    #Tant que infiniteContinue est égale à 1
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [0 , 2]
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
        #Afficher une demande de continuer à jouer avec comme option oui(1) et non(0)
        #Définir la variable infinitContinue avec comme le retour de l'éxecution de la fonction input("Voulez-vous continuez (1 pour oui, 0 pour non)")
    #Sinon executer la fonction shifumiMenu














#Définir la fonction playerVersusCpuGameMode qui permet de jouer au shifumi contre l'ordinateur en fonction de set ou et de points
    #Initialiser la variable scorePlayer à 0
    #Initialiser la variable scoreCpu à 0
    #Initialiser la variable setPlayer à 0
    #Initialiser la variable setCpu à 0
    #Initialiser la variable playerChoice à None
    #Initialiser la variable cpuChoice à None
    
    #Tant que setPlayer < 2 et setCpu < 2, Alors...
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [1 , 3]
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("1 pour pierre, 2 pour feuille ou 3 pour ciseaux: ")
        #Si playerChoice est égale à cpuChoice
            #Alors écrire "Egalité!"
        #Sinon si playerChoice égale à 1
            #Si cpuChoice égale à 3
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon 
                #Alors, écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon si playerChoice égale à 2
            #Si cpuChoice égale à 1
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon 
                #Alors, écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu à 1
        #Sinon si playerChoice égale à 3
            #Si cpuChoice égale de 2
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon
                #Alors écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon : playerChoice ne renvoi à aucun élément du tableau game
            #Alors écrire "Choix impossible!"
        #Si scorePlayer est égal à 5, Alors...
            #Assigner à scorePlayer la valeur 0
            #Incrémenter setPlayer de 1
    #Sinon executer la fonction shifumiMenu












#Définir la fonction spokeGameMode qui permet de jouer au shifumi avec les règles avancés

    #Initialiser une variable infiniteContinue à 1
    #Initialiser une variable cpuChoice à None
    #Initialiser une variable playerChoice à None
    #Initialiser une variable cpuScore à 0
    #Initialiser une variable playerScore à 0
    #Tant que infiniteContinue est égale à 1
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [1 , 5]
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction float(input("1 pour pierre, 2 pour feuille, 3 pour ciseaux, 4 pour lézard ou 5 pour spoke: "))
        #Si playerChoice est égale à cpuChoice
            #Alors écrire "Egalité!"
        #Sinon si playerChoice égale à 1
            #Si cpuChoice égale à 3 ou à 4
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon
                #Alors, écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon si playerChoice égale à 2
            #Si cpuChoice égale à 1 ou à 5
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon
                #Alors, écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu à 1
        #Sinon si playerChoice égale à 3
            #Si cpuChoice égale de 2 ou à 4
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon
                #Alors écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon si playerChoice égale à 4
            #Si cpuChoice égale de 2 ou à 5
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon
                #Alors écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon si playerChoice égale à 5
            #Si cpuChoice égale de 1 ou à 3
                #Alors écrire "Vous avez gagné!"
                #Incrémenter scorePlayer de 1
            #Sinon
                #Alors écrire "Vous avez Perdu!"
                #Incrémenter scoreCpu de 1
        #Sinon : playerChoice ne renvoi à aucun élément du tableau game
            #Alors écrire "Choix impossible!"
        #Afficher les scores de la partie à partir de scorePlayer et scoreCpu 
        #Afficher une demande de continuer à jouer avec comme option oui(1) et non(0)
        #Définir la variable infinitContinue avec comme le retour de l'éxecution de la fonction input("Voulez-vous continuez (1 pour oui, 0 pour non)")
    #Sinon executer la fonction shifumiMenu





#----------------------------MENU------------------------------

#Définir une fonction shifumiMenu qui permet d'appeler les fonctions de jeux selon les préférences du ou des joueurs
def shifumiMenu():
    #Initialiser une variable gameMode à None
    gameMode = None
    #Appeler print("--------- MENU SIFUMI ----")
    print("--------- MENU SIFUMI ----")
    #Appeler print("0 - Quitter")
    print("0 - Quitter")
    #Appeler print("1 - Mode Infini")
    print("1 - Mode Infini")
    #Appeler print("2 - Mode Joueur vs Ordi")
    print("2 - Mode Joueur vs Ordi")
    #Appeler print("3 - Mode Joueur vs Joueur")
    print("3 - Mode Joueur vs Joueur")
    #Appeler print("---------------------------")
    print("---------------------------")
    #Définir la variable gameMode avec comme valeur le retour de l'éxecution de la fonction float(input("Mode de jeu : "))
    gameMode = float(input("Mode de jeu : "))


    #Si le gameMode est égale à 1
    if gameMode == 1:
        #Executer la fonction infiniteGameMode
        infinitGameMode()
    #Sinon si le gameMode est égale à 2
    elif gameMode == 2:
        #Executer la fonction playerVersusCpuGameMode
        playerVersusCpuGameMode()
    #Sinon si le gameMode est égale à 3
    elif gameMode == 3:
        #Executer la fonction playerVersusPlayerGameMode
        playerVersusPlayerGameMode()
    #Sinon si le gameMode est égale à 0
    elif gameMode == 0:
        #Afficher "arret du jeu"
        print("arrêt du jeu")
        print("arrêt du jeu.")
        print("arrêt du jeu..")
        print("arrêt du jeu...")
        #retourner
        return
    #Sinon si le gameMode est égale à 3.14
    elif gameMode == 3.14:
        #Executer la fonction spokeGameMode
        spokeGameMode()

#Executer la fonction shifumiMenu
shifumiMenu()



#FIN