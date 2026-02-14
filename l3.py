import math


print(math.pi)
print(math.tau)
print(math.inf)
def task1(r):
    print("circumference is:",math.tau*r)
    print("the area is:",math.pi*r**2)

task1(3)

def task2():
    print(math.sqrt(5))
    print(math.log(math.exp(5)))
task2()
import random

def task3():
    for i in range(6):
        print(random.randrange(1,100))
        print(random.randint(1,99))


task3()



from place import calcul

def task4():
    print(calcul.sum(5, 10))
    print(calcul.multiply(5, 10))
task4()


def task5():
    chances=7
    solution = random.randit(1,99)
    rep = -1
    while chances != 0:
        chances -= 1
        rep = int(input("give me your guess "))
        if rep == solution:
            print("you win")
            chances = 0
        else:
            print("try again")
            if chances == 0:
                print('The right number is ',solution)
