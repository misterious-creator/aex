import os
import sys
if len(sys.argv) < 2:
    print("usage: aex fichier.aex")
    sys.exit()
chemin = sys.argv[1]
cheminaex = chemin.split(".")
condition = True
if not chemin.lower().endswith(".aex"):
    print("AEX ERROR")
    sys.exit()
with open(chemin,"r") as contenu:
  fichier = contenu.read()
caracters = []
for caracter in fichier:
    caracters.append(caracter)
#parser
compteur = 0
aex = []
while compteur < len(caracters) and condition:
    if caracters[compteur] == "w" and condition:
        if compteur + 1 < len(caracters) and caracters[compteur + 1] == '"':
            if compteur + 2 < len(caracters):
                aex.append(("w", caracters[compteur + 2]))
                compteur += 3
            else:
                print("erreur")
                condition = False
                break
        elif compteur + 1 < len(caracters) and caracters[compteur + 1] == "m":
            aex.append(("w", "m"))
            compteur += 2
        elif compteur + 1 < len(caracters) and caracters[compteur + 1] == "i":
            aex.append(("w", "i"))
            compteur += 2
        else:
            print("erreur")
            condition = False
            break
    elif len(caracters) <= compteur:
        break
    elif caracters[compteur] == "m" and condition:
        if compteur + 1 < len(caracters) and caracters[compteur + 1] == "i":
            aex.append(("m", "i"))
            compteur += 2
        elif (
          compteur + 2 < len(caracters)
          and caracters[compteur + 1].isdigit()
          and caracters[compteur + 2].isdigit()
          ):
            sommenb = caracters[compteur + 1] + caracters[compteur + 2]
            aex.append(("m", int(sommenb)))
            compteur += 3
        else:
            print("error")
            condition = False
            break
    elif len(caracters) <= compteur:
        break
    elif caracters[compteur] == "-" and condition:
        if compteur + 1 < len(caracters) and caracters[compteur + 1] == "-":
            aex.append(("-", "--"))
            compteur += 2
        else:
            aex.append(("-", "-"))
            compteur += 1
    elif len(caracters) <= compteur:
        break
    elif caracters[compteur] == "+" and condition:
        aex.append(("+", "+"))
        compteur += 1
    elif len(caracters) <= compteur:
        break
    elif caracters[compteur] == "c" and condition:
        aex.append(("c", "c"))
        compteur += 1
    elif len(caracters) <= compteur:
        break
    elif caracters[compteur] == "t" and condition:
        if (
            compteur + 2 < len(caracters)
            and caracters[compteur + 1].isdigit()
            and caracters[compteur + 2].isdigit()
        ):
            nbjoint = caracters[compteur + 1] + caracters[compteur + 2]
            aex.append(("t", int(nbjoint)))
            compteur += 3
        elif compteur + 1 < len(caracters) and caracters[compteur + 1] == "m":
            aex.append(("t", "m"))
            compteur += 2
        else:
            print("error")
            condition = False
            break
    elif len(caracters) <= compteur:
        break
    elif caracters[compteur] == "\n":
      with open(chemin, "w", encoding="utf-8") as haha:
        haha.write("")
    else:
        if (
            caracters[compteur] not in
            ["i", "w", "m", "-", "+", "c", "t", '"',"\n"]
            and not caracters[compteur].isdigit()
        ):
            print("error")
            condition = False
            break
        compteur += 1
# executer
memoire = []
for x, y in aex:
  if condition == False:
    break
  if x == "w":
      if y == "m":
          if memoire:
                print(memoire[-1])
      elif y == "i":
            print(input())
      else:
            print(y)
  elif x == "m":
        if y == "i":
            m = input()
            if m.isdigit():
                memoire.append(int(m))
            else:
                memoire.append(ord(m[0]))
        else:
            if str(y).isdigit():
                memoire.append(int(y))
            else:
                memoire.append(ord(str(y)[0]))
  elif x == "-":
        if y == "--":
            memoire.clear()
        else:
            if len(memoire) >= 2:
                b = memoire.pop()
                a = memoire.pop()
                memoire.append(a - b)
  elif x == "+":
        if len(memoire) >= 2:
            b = memoire.pop()
            a = memoire.pop()
            memoire.append(a + b)
  elif x == "c":
        os.system("cls" if os.name == "nt" else "clear")
  elif x == "t":
        if y == "m":
            if memoire:
                valeur = memoire.pop()
                if isinstance(valeur, int):
                    if 0 <= valeur <= 1114111:
                        memoire.append(chr(valeur))
                    else:
                        memoire.append(valeur)
                elif isinstance(valeur, str):
                    if len(valeur) == 1:
                        memoire.append(ord(valeur))
                    else:
                        memoire.append(valeur)
        elif isinstance(y, int):
            if 0 <= y < len(memoire):
                valeur = memoire[y]
                if isinstance(valeur, int):
                    if 0 <= valeur <= 1114111:
                        memoire[y] = chr(valeur)
                elif isinstance(valeur, str):
                    if len(valeur) == 1:
                        memoire[y] = ord(valeur)