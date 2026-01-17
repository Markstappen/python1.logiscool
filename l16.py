rooms = []
items = []
inGame = True
solution = "4611"
guess = ""
lives = "3"

print("Bienvenue dans mon escape room. Essaie de trouver la sortie. Il y a 4 piece (0-3)")

while inGame:
    room_number = input("Quel piece veut tu visiter?")
    if room_number == "0":
        if "key" in items:
            print("Plus rien a faire dans cette piece")
        else:
            print("Tu as trouver la cle.")
            items.append("key")
    elif room_number == "1":
        if "key" in items:
            print("Vous ouvrez la porte est vous trouvez un calcul : 23  x 2")
        else:
            print("La porte est bloque, il nous faut une cle")
    elif room_number == "2":
        print("Je suis + grand que 10, + petit que 30 est la somme de mes chiffres est 2. Qui suis je?")
    elif room_number == "4":
        print("Tu rentre dans une piece, tu vois une creature, tu decides de t en approcher, grave erreur il te mord." \
        " Tu sors tout de suite de la piece et referme la porte. tu perd une vie")
        lives -= 1
    elif room_number == "-1":   
        print("Story so far")
        print(items)
    elif room_number == "3":
        print("Je suis devant la sortie, qui requiert un code. ")
        guess == input ("quel est le code?") 
        if guess == solution:
            print("Vous avez trouvez le bon code")
            inGame = False
        else:
            print("pas le bon code")
            lives -= 1
    if lives == "0":
        print("Tu es mort")
print("vous etes sorti felicitation")
