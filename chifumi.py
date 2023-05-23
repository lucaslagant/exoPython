import random

player = input("Pierre (p), Feuille (f), ou Ciseaux (c) ?")

computer = random.randint(1, 3)


if computer == 1:
    computer = "Pierre"
elif computer == 2:
    computer = "Feuille"
elif computer == 3:
    computer = "Ciseaux"
if player == "p":
    print("Vous avez choisi Pierre .")
    print("L'ordinateur a choisi", computer)
elif player == "f":
    print("Vous avez choisi Feuille .")
    print("L'ordinateur a choisi", computer)
elif player == "c":
    print("Vous avez choisi Ciseaux .")
    print("L'ordinateur a choisi", computer)
if (player == 'p' and computer == "Ciseaux") or (player == 'f' and computer == "Pierre") or (player == 'c' and computer == "Feuille"):
    print("Le joueur gagne !")
elif (player == 'p' and computer == "Feuille") or (player == 'f' and computer == "Ciseaux") or (player == 'c' and computer == "Pierre"):
    print("L'ordinateur gagne !")
elif (player == 'p' and computer == "Pierre") or (player == 'f' and computer == "Feuille") or (player == 'c' and computer == "Ciseaux"):
    print("Egalité !")