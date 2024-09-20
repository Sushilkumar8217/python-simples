'''
snake =  1
water = -1
gun   =  0

'''
import random

computer = random.choice([1,-1,0])
you = input("enter your choice:")

you_dict={"s":1,"w":-1,"g":0}
rev_dict={1:"snake",-1:"water",0:"gun"}
yourchoice=you_dict[you]

print(f"you choose:{rev_dict[yourchoice]}")
print(f"computer choose:{rev_dict[computer]}")

if(yourchoice == computer):
    print("draw!")
else:
    if(computer==1 and yourchoice==-1):  # 1-(-1)=2
        print("you loose!")
    elif(computer==1 and yourchoice == 0): # 1-(-0)=1
        print("you win!")
               
    elif(computer==-1 and yourchoice == 1): # -1 -(1)=-2
        print("you win!")
               
    elif(computer==-1 and yourchoice == 0):  #-1 -(-0)=-1
        print("you loose!")
               
    elif(computer==0 and yourchoice == 1):   #  0-(-1)=1
        print("you loose!")
               
    elif(computer==0 and yourchoice == -1):   # 0-(-1)=1
        print("you win!")
    else:
        print("something went wrong")
        
        
        # or pattern trace code is below

    # if((computer-yourchoice)==1 or (computer-yourchoice)==-2):
    #     print("you win!")
    # else:
    #     print("you loose")    
         
