M = [["*"]*3,
     ["*"]*3,
     ["*"]*3,
     ]

print(M)
gameOver = False
current_player = 0

while not gameOver:
    i = int(input("Choisis la ligne entre 0 et 3 : "))
    j = int(input("Choisis la colonne entre 0 et 3 : "))

    M[i][j] = "O" if current_player==0 else "X"


    if current_player == 0:
        current_player = 1
    else:
        current_player = 0

    for i in range(len(M)):
        if M[i][0] == M[i][1] and M[i][0] == M[i][2]:
            gameOver = True 

    for j in range(len(M)):
        if M[0][j] == M[1][j] and M[0][j] == M[2][j] and M[0][j] !="*":
            gameOver = True

    
    if M[0][0] == M[1][1] and M[0][0] == M[2][2] and M[0][0] !="*":
        gameOver = True

    if M[2][0] == M[1][1] and M[2][0] == M[0][2] and M[2][0] !="*":
        gameOver = True 
 
 


    print()