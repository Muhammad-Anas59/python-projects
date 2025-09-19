import random
comp=random.randint(0,2)
user=int(input("Enter 0 for snake,1 for water,2 for gun : "))
def check(comp,user):
    if comp==user:
        return 0
    elif comp==0 and user==1 :
        return -1
    elif comp==1 and user==2:
        return -1
    elif comp==2 and user==0:
        return -1
    return 1
score=check(comp,user)
print("You selected : ",user)
print("Computer selected : ",comp)
if score==1:
    print( "You Won: ")
elif score==0:
    print("It's a draw : ")
else:
    print("You lost:")
