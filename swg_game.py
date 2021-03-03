import random
def game(a,b):
    if (a=='s' and b=='s'):
        print("Draw")
    elif(a=='w' and b=='w'):
        print("Draw")
    elif(a=='g' and b=='g'):
        print("Draw")
    elif(a=='s' and b=='w'):
        print("Computer Wins")
    elif(a=='w' and b=='g'):
        print("Computer Wins")
    elif(a=='g' and b=='s'):
        print("Computer Wins")
    elif(a=='w' and b=='s'):
        print("You Win")
    elif(a=='g' and b=='w'):
        print("You Win")
    elif(a=='s' and b=='g'):
        print("You Win")
a = random.randint(1,3)
if a==1:
    c='s'
elif a==2:
    c='w'
elif a=='3':
    c='g'
b = input("Your Turn :Snake(s) , Water(w) , Gun(g): ")
game(c,b)