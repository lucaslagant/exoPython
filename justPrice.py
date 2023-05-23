import random

price = random.randint(1, 10)

score = 100

tentatives = 0

print("Devinez le juste prix ! Le prix est un nombre entre 1 et 10 inclus.")

while True:
    number = int(input())
    tentatives += 1
    if number < price:
        print("Le juste prix est plus haut")
    if number > price:
        print("Le juste prix est plus bas")
    if number == price:
        print("Félicitations , vous avez trouvé le juste prix {} en {} essais, votre score est {} points !".format(price, tentatives, int(score/tentatives)))

print("Partie terminée")