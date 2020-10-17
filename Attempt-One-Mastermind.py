import random

#instructions
print("Welcome to Mastermind! Here are the instructions:\n4 numbers between 1 and 6 will be randonly generated. There may be repeated numbers.\n")
print("Your job is to guess the set of 4 numbers in 10 tries!\nA 0 marks that there is a correct number in the correct spot.\nAn X marks that there is a correct number in the wrong spot.")
print("Good luck!")

#generating random list, ranNum
ranNum = []
for i in range(4):
    n = random.randint(1,6)
    ranNum.append(n)
print(ranNum)  

#user input - REMEMBER TO CREATE CONDITIONS
userInput = input("Please enter 4 numbers, separated by a space:").split()
userList = list(map(int, userInput))
print(userList)

# "0" counter
def O_counter():
    O_count = 0
    if ranNum[0] == userList[0]:
        O_count += 1
    if ranNum[1] == userList[1]:
        O_count += 1
    if ranNum[2] == userList[2]:
        O_count += 1
    if ranNum[3] == userList[3]:
        O_count += 1
    print("0 count: " + str(O_count))

# "X" counter
def X_counter():
    X_count = 0
    for i in range(len(ranNum)):
        for j in range(len(userList)):
            if i != j and ranNum[i] == userList[j]:
                X_count += 1
    print("X count: " + str(X_count))
    
#while
while ranNum != userInput:
    O_counter()
    X_counter()
    print("Hmmm...keep guessing!")
    userInput = input("\nPlease enter 4 numbers, separated by a space:").split()
    userList = list(map(int, userInput))

        




