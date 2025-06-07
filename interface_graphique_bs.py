
from tkinter import *
from classes_bs import *


c = 0
list = []

def interface_graphique():
  global jeu_instance, c, list
  """Fonction pour lancer le jeu avec l'interface graphique"""
  fenetre = Tk()
  jeu_instance = Jeu()
  jeu_instance.initialise_plateau()

  Largeur = 390
  Hauteur = 300
  canevas = Canvas(fenetre, width=Largeur, height=Hauteur, bg='white', bd=0, highlightthickness=0)
  canevas.pack(padx=5, pady=5)

  def deplacer(td, ta):
    """Fonction pour deplacer les balles dans les tubes"""
    if jeu_instance.plateau.est_gagnant()==False:
      jeu_instance.deplace(td,ta)
      showgame(jeu_instance)
      if jeu_instance.plateau.est_gagnant()==True:
        canevas.create_text(200, 100, text="Vous avez gagné !", font="Arial 20 bold", fill="red")
        jeu_instance.afficher()

    else:
      canevas.create_text(200, 100, text="Vous avez gagné !", font="Arial 20 bold", fill="red")
      jeu_instance.afficher()



  """fonction pour deplacer les balles dans les tubes"""


  def tube_1():
    global list
    if len(list) == 0:
      list.append(0)

    else:
      list.append(0)
      deplacer(list[0], list[1])
      list = []


  def tube_2():
    global list
    if len(list) == 0:
      list.append(1)

    else:
      list.append(1)
      deplacer(list[0], list[1])
      list = []

    
  def tube_3():
    global list
    if len(list) == 0:
      list.append(2)

    else:
      list.append(2)
      deplacer(list[0], list[1])
      list = []


  def tube_4():
    global list
    if len(list) == 0:
      list.append(3)

    else:
      list.append(3)
      deplacer(list[0], list[1])
      list = []


  def tube_5():
    global list
    if len(list) == 0:
      list.append(4)

    else:
      list.append(4)
      deplacer(list[0], list[1])
      list = []


  def tube_6():
    global list
    if len(list) == 0:
      list.append(5)

    else:
      list.append(5)
      deplacer(list[0], list[1])
      list = []




  def showgame(jeu_instance):
      """Affiche le jeu sur l'interface graphique"""
      canevas.create_rectangle(0, 0, 390, 250, width=0, fill='white')
      
      for i in range(6):
          tube = jeu_instance.plateau.tubes[i].get_balles() 
          
          for j, balle in enumerate(tube):
              couleur = balle.afficher()  
              position = (i * 65 + 20, 230 - j * 30, i * 65 + 50, 200 - j * 30)
              
              canevas.create_oval(position[0], position[1], position[2], position[3], width=1, fill=couleur)


  def jouer():
    """Fonction pour recommencer le jeuS"""
    global jeu_instance
    jeu_instance = Jeu()
    jeu_instance.initialise_plateau()
    jeu_instance.afficher()
    showgame(jeu_instance)

  button_labels = [
      "tube_1", "tube_2", "tube_3", "tube_4",
        "tube_5", "tube_6", "jouer"]
  for label in button_labels:
    button = Button(fenetre, text=label, width=5,
                     command=eval(label))
    if label == "jouer":
      button.pack(side=BOTTOM)
    else:
      button.pack(side=LEFT)

  for i in range(6):
    canevas.create_line(25 + i * 64,
                        250,
                        60 + i * 64,
                        250,
                        width=3,
                        fill="black")
    
    
  fenetre.protocol("WM_DELETE_WINDOW", fenetre.destroy)
  showgame(jeu_instance)
  fenetre.mainloop()



