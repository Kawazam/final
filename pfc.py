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




#Définir une fonction shifumiTurn(movePlayer1, movePlayer2) qui renvoi le vainqueur du tour (j1 ou j2) à partir de leur choix respectif. Un retour à 0 signinfie pas de vainqueur
def shifumiTurn(movePlayer1, movePlayer2):
    #Si movePlayer1 est égale à movePlayer2
    if movePlayer1 == movePlayer2:
        #Alors écrire "Egalité!"
        print("Égalité !")
        #Retourner 0
        return 0
    #Sinon si movePlayer1 égale à 1
    elif movePlayer1 == 1:
        #Si movePlayer2 égale à 3
        if movePlayer2 == 3:
            #Alors afficher "+1 pt pour le Joueur 1"
            print("+1 pt pour le Joueur 1")
            #Retourner 1
            return 1
        #Sinon
        else:
            #Alors afficher "+1 pt pour le Joueur 2"
            print("+1 pt pour le Joueur 2")
            #Retourner 2
            return 2
    #Sinon si movePlayer1 égale à 2
    elif movePlayer1 == 2:
        #Si movePlayer2 égale à 1
        if movePlayer2 == 1:
            #Alors afficher "+1 pt pour le Joueur 1"
            print("+1 pt pour le Joueur 1")
            #Retourner 1
            return 1
        #Sinon
        else:
            #Alors afficher "+1 pt pour le Joueur 2"
            print("+1 pt pour le Joueur 2")
            #Retourner 2
            return 2
    #Sinon si movePlayer1 égale à 3
    elif movePlayer1 == 3:
        #Si movePlayer2 égale de 2
        if movePlayer2 == 2:
            #Alors afficher "+1 pt pour le Joueur 1"
            print("+1 pt pour le Joueur 1")
            #Retourner 1
            return 1
        #Sinon
        else:
            #Alors afficher "+1 pt pour le Joueur 2"
            print("+1 pt pour le Joueur 2")
            #Retourner 2
            return 2
    #Sinon Si aucun des 2 movePlayer n'est valide (entre 1 et 3)
    elif (movePlayer1 < 1 or movePlayer1 > 3):
        #Alors écrire "Choix impossible!"
        print("Choix Impossible !")
        #Retourner 0




#Définir la fonction infiniteGameMode qui permet de jouer au shifumi contre l'ordinateur à l'infinie
    #Initialiser une variable infiniteContinue à 1
    #Initialiser une variable cpuChoice à None
    #Initialiser une variable playerChoice à None
    #Initialiser une variable cpuScore à 0
    #Initialiser une variable playerScore à 0
    #Tant que infiniteContinue est égale à 1
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [0 , 2]
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Que faites-vous ce tour ? ")
        #Si le retour de l'appel de la fonction shifumiTurn(playerChoice, cpuChoice) est égal à 1, Alors...
            #Incrémenter playerScore de 1
        #Sinon Si le retour de l'appel de la fonction shifumiTurn(playerChoice, cpuChoice) est égal à 2, Alors...
            #Incrémenter cpuScore de 1
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
        #Si le retour de l'appel de la fonction shifumiTurn(playerChoice, cpuChoice) est égal à 1, Alors...
            #Incrémenter scorePlayer de 1
        #Sinon Si le retour de l'appel de la fonction shifumiTurn(playerChoice, cpuChoice) est égal à 2, Alors...
            #Incrémenter scoreCpu de 1
        #Si scorePlayer est égal à 5, Alors...
            #Assigner à scorePlayer la valeur 0
            #Incrémenter setPlayer de 1
    #Sinon executer la fonction shifumiMenu





#Définir la fonction playerVersusPlayerGameMode qui permet de jouer au shifumi contre l'ordinateur en fonction de set ou et de points
    #Initialiser la variable scorePlayer1 à 0
    #Initialiser la variable scorePlayer2 à 0
    #Initialiser la variable setPlayer1 à 0
    #Initialiser la variable setPlayer2 à 0
    #Initialiser la variable playerChoice1 à None
    #Initialiser la variable playerChoice2 à None
    
    #Tant que setPlayer < 2 et setCpu < 2, Alors...
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [0 , 2]
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction input("Que faites-vous ce tour ? ")
        #Si le retour de l'appel de la fonction shifumiTurn(playerChoice, cpuChoice) est égal à 1, Alors...
            #Incrémenter scorePlayer1 de 1
        #Sinon Si le retour de l'appel de la fonction shifumiTurn(playerChoice, cpuChoice) est égal à 2, Alors...
            #Incrémenter scorePlayer2 de 1
        #Si scorePlayer1 est égal à 5, Alors...
            #Assigner à scorePlayer1 la valeur 0
            #Incrémenter setPlayer1 de 1
            #Afficher les set gagné de la partie jusque-là pour les deux participants
        #Si scorePlayer2 est égal à 5, Alors...
            #Assigner à scorePlayer2 la valeur 0
            #Incrémenter setPlayer2 de 1
            #Afficher les set gagné de la partie jusque-là pour les deux participants
    #Éxecuter la fonction shifumiMenu






#Définir la fonction spokeGameMode qui permet de jouer au shifumi avec les règles avancés
def spokeGameMode():
    #Initialiser une variable cpuChoice à None
    cpuChoice = None
    #Initialiser une variable playerChoice à None
    playerChoice = None
    #Initialiser une variable cpuScore à 0
    cpuScore = 0
    #Initialiser une variable playerScore à 0
    playerScore = 0
    #Initialiser une variable cpuName avec comme valeur un nom aléatoir dans la liste ("Jean", "Michel", "Etienne")
    # cpuName = randint("Jean", "Michel", "Etienne", "Bob")
    #Tant que infiniteContinue est égale à 1
    while playerScore < 5 and cpuScore < 5:
        #Définir la variable cpuChoice avec comme valeur le retour de l'éxecution de la fonction randint() dans l'intervalle [1 , 5]
        cpuChoice = randint(1, 5)
        #Définir la variable playerChoice avec comme valeur le retour de l'éxecution de la fonction float(input("1 pour pierre, 2 pour feuille, 3 pour ciseaux, 4 pour lézard ou 5 pour spoke: "))
        playerChoice = float(input("1 pour pierre, 2 pour feuille, 3 pour ciseaux, 4 pour lézard ou 5 pour spoke: "))
        #Si playerChoice est égale à cpuChoice
        if playerChoice == cpuChoice:
            #Alors écrire "Egalité!"
            print("Égalité, essaie encore !")
        #Sinon si playerChoice égale à 1
        elif playerChoice == 1:
            #Si cpuChoice égale à 3 ou à 4
            if cpuChoice == 3 or cpuChoice == 4:
                #Alors écrire "Vous avez gagné!"
                print("Vous marquez 1 point")
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
            #Sinon
            else:
                #Alors, écrire "Vous avez Perdu!"
                print("L'ordinateur marque 1 point")
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
        #Sinon si playerChoice égale à 2
        elif playerChoice == 2:
            #Si cpuChoice égale à 1 ou à 5
            if cpuChoice == 1 or cpuChoice == 5:
                #Alors écrire "Vous avez gagné!"
                print("Vous marquez 1 point")
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
            #Sinon
            else:
                #Alors, écrire "Vous avez Perdu!"
                print("L'ordinateur marque 1 point")
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
        #Sinon si playerChoice égale à 3
        elif playerChoice == 3:
            #Si cpuChoice égale de 2 ou à 4
            if cpuChoice == 2 or cpuChoice == 4:
                #Alors écrire "Vous avez gagné!"
                print("Vous marquez 1 point")
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
            #Sinon
            else:
                #Alors, écrire "Vous avez Perdu!"
                print("L'ordinateur marque 1 point")
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
        #Sinon si playerChoice égale à 4
        elif playerChoice == 4:
            #Si cpuChoice égale de 2 ou à 5
            if cpuChoice == 2 or cpuChoice == 5:
                #Alors écrire "Vous avez gagné!"
                print("Vous marquez 1 point")
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
            #Sinon
            else:
                #Alors, écrire "Vous avez Perdu!"
                print("L'ordinateur marque 1 point")
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
        #Sinon si playerChoice égale à 5
        elif playerChoice == 5:
            #Si cpuChoice égale de 1 ou à 3
            if cpuChoice == 1 or cpuChoice == 3:
                #Alors écrire "Vous avez gagné!"
                print("Vous marquez 1 point")
                #Incrémenter playerScore de 1
                playerScore = playerScore + 1
            #Sinon
            else:
                #Alors, écrire "Vous avez Perdu!"
                print("L'ordinateur marque 1 point")
                #Incrémenter cpuScore de 1
                cpuScore = cpuScore + 1
        #Sinon : playerChoice ne renvoi à aucun élément du tableau game
        else:
            #Alors écrire "Choix impossible!"
            print("Se choix ne fait pas parti des propositions.")
    #Afficher les scores de la partie à partir de playerScore et cpuScore 
    print("Voici le score final: ", playerScore, "/", cpuScore)
    #Afficher une demande de continuer à jouer avec comme option oui(1) et non(0)
    print("retour au menu")
    print("retour au menu.")
    print("retour au menu..")
    print("retour au menu...")
    #Sinon executer la fonction shifumiMenu
    shifumiMenu()





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