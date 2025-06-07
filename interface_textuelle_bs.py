from classes_bs import *

line = "***************************************"
gagner = False

def game ():
  global gagner
  jeu_instance = Jeu()
  jeu_instance.initialise_plateau()
  print(jeu_instance.plateau)
  while jeu_instance.plateau.est_gagnant()==False:
    print(line)
    tube_d = int(input('tube départ? '))
    tube_a = int(input('tube arrivee? '))
    jeu_instance.deplace(tube_d,tube_a)
    print(line)
    print(jeu_instance.plateau)

    print(line)



def interface_textuelle():
  """Fonction pour lancer le jeu avec l'interface textuelle"""
  global gagner
  print('bienvenue dans le jeu des tubes et des balles')
  print('les tubes sont numeroter de 0 a 5')
  game()
  while gagner == False:
    print(line)
    rejouer = input('voulez vous rejouer? (oui/non) ')
    print(line)
    if rejouer == 'oui':
      game()
    else:
      gagner = True
      print('merci d\'avoir jouer')
      break


