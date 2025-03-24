import random
''' 
1 for snake 
-1 for water
0 for gun
'''
print("Please enter only (s , w , g )")

computer = random.choice([1,-1,0])
youstr = input("enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer==1 and you==1):
    print("DRAW")

elif(computer==1 and you==-1):
    print("YOU LOSSES")

elif(computer==1 and you==0):
    print("YOU WIN")

elif(computer==-1 and you==1):
    print("YOU WIN")

elif(computer==-1 and you==-1):
    print("DRAW")

elif(computer==-1 and you==0):
    print("YOU LOSSES")

elif(computer==0 and you==1):
    print("YOU LOSSES")

elif(computer==0 and you==-1):
    print("YOU WIN")

elif(computer==0 and you==0):
    print("DRAW")
