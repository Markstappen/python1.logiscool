def printer():
    print("Hellow Wolf")

#printer()

def printerbis(x):
    print(x)

mot = "nutella"
#printerbis(mot)

def estPremier(num):
    premier = True
    for i in range(2, num):
        if num % i == 0:
            premier = False
    if premier:
        print(num,"est un nombre premier" )
    else:
        print(num, "est pas un nombre premier")

nombre = int(input("Choisi un nbr"))
estPremier(nombre)

def right_triangle(a, b, c):
    if(a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
        print("C est un triangle rectangle")
    else:
        print("Ce n est pas un triangle rectangle")

right_triangle(3, 4, 5)
right_triangle(4, 5, 6)

def func_numbers(q, r, p):
    a = p + q**2 + r**2
    print(a)

func_numbers(p=3, q=2, r=1)