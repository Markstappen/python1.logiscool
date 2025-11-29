def task1():
    x_pos = int(input("What is the x position?\n"))
    y_pos = int(input("what is the y position?\n"))
    if x_pos >=0:
        if y_pos:
            print("1")
        else:
            print("2")
    else:
        if y_pos >=0:
            print("3")
        else:
            print("4")
task1()

def Pgdc():
    number_1 = int("What is the first numb?\n")
    number_2 = int("What is the highest num?\n")
    gdc = 1
    for i in range(1,number_1+1):
        if number_1 % i == 0 and number_2 % i == 0:
            gdc = i
    print(gdc)
Pgdc()


