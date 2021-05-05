# stone paper scissor Game
import random 
def whoWin(comp,yourchoice):
    if(comp==yourchoice):
        return None
    elif(comp=='s'):
        if(yourchoice=='p'):
            return True
        elif(yourchoice=='a'):
            return False
    elif(comp=='p'):
        if(yourchoice=='a'):
            return True
        elif(yourchoice=='s'):
            return False
    elif(comp=='a'):
        if(yourchoice=='s'):
            return True
        elif(yourchoice=='p'):
            return False        
print("computer choice:Stone(s), paper (p),axe(a)")
rand=random.randint(1,3)
if(rand==1):
    comp='s'
elif(rand==2):
    comp='p'
elif(rand==3):
    comp='a'

yourchoice=input("your choice :Stone(s), paper (p),axe(a)\n")
a= whoWin(comp,yourchoice)
if(a==None):
    print("Game Tie")
elif a:
    print("you won,computer choose",comp)
else:
    print("you Loose,computer choose",comp)


