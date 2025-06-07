import random as rd


class Balle:
  """classe qui contient les balles"""

  def __init__(self, couleur):
    self.couleur = couleur

  def afficher(self):
    return self.couleur


class Tube:
  """classe qui contient les Tubes de balles"""

  def __init__(self):
    self.balles = []

  def empile(self, balle):
    self.balles.append(balle)

  def depile(self):
    if not self.est_vide():
      return self.balles.pop()

  def sommet(self):
    if not self.est_vide():
      return self.balles[-1]

  def est_vide(self):
    return len(self.balles) == 0


  def longueur(self):
    return len(self.balles)

  def get_balles(self):
    return self.balles
  
  def est_plein_monochrome(self):
    if not self.est_vide():
      couleur = self.balles[0].afficher()
      compteur = 0
      for b in self.balles:
        if b.afficher() == couleur:
          compteur += 1
        else:
          return False
      return compteur == 4
    return False

  def afficher(self):
    print(str([b.afficher() for b in self.balles]))

  def __str__(self):
    return str([b.afficher() for b in self.balles])

class Plateau:
  """classe Plateau qui contient les tubes"""

  def __init__(self):
    global gagner
    self.tubes = []

  def tableau (self): 
    """fonction qui retourne un tableau de balles"""
    tableau = []
    for tube in self.tubes:
      tableau.append([b.afficher() for b in tube.balles])
    return tableau
  
  def deplace_balle(self, td, ta):
    """fonction qui deplace les balles dans les tubes"""
    if not td.est_vide():
      balle = td.depile()
      ta.empile(balle)
      self.est_gagnant()

  def est_gagnant(self):
    """fonction qui verifie si le joueur a gagner"""
    x=0
    for tube in self.tubes:
      if tube.est_plein_monochrome() == True :
        x += 1
    if x == 4 :
      print('vous avez  gagner !')
      return True
    else:
      return False
      
  def afficher(self):
    for tube in self.tubes:
      tube.afficher()


  def __str__(self):
      str = ""
      for i in range (6):
        str += f"{i}: {self.tubes[i]}\n"
      return str
class Jeu:
  """ classe qui initialise le jeu"""
  def __init__(self):
    self.plateau = Plateau()

  def initialise_plateau(self):
    couleurs = ['red', 'green', 'blue', 'yellow']
    couleurs = couleurs * 4
    for y in range(4):
      name_tube = ("tube_" + str(y))
      name_tube = Tube()
      for x in range(4):
        couleur_aleatoire = rd.choice(couleurs)
        balle = Balle(couleur_aleatoire)        
        name_tube.empile(balle)
        couleurs.remove(couleur_aleatoire)
      self.plateau.tubes.append(name_tube)

    for i in range(4, 6):
      name_tube = Tube()
      self.plateau.tubes.append(name_tube)

  def deplace(self, td, ta):
      if ta < 6:
          if self.plateau.tubes[ta].longueur() < 4:
              td = self.plateau.tubes[td]
              ta = self.plateau.tubes[ta]
              self.plateau.deplace_balle(td, ta)
          else:
              print("Erreur : Tube de destination plein.")
      else:
          print("Erreur : Tube de destination invalide.")

  def afficher(self):
    self.plateau.afficher()
