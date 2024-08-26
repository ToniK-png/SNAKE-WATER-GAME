import random
computer =random.choice([1,0,-1])
youstr = input("Enter your Choice: ")
youDict = {"S":1,"W":0,"G":-1}
dict2 = {1:"Snake",0:"Water",-1:"Gun"}
you = youDict[youstr]
print(f"You chose {dict2[you]}\nComputer chose {dict2[computer]}")

if(computer ==you):
    print("Its a Draw")
else:
    if(computer==-1 and you==0):
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Lose!")
    elif(computer==0 and you==1):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==1 and you==0):
        print("You Lose")
    elif(computer==1 and you==-1):
        print("You Win!")
    else:
        print("something went wrong!")                        
