import os
import sys


def printFirstStage():
    print('-', '-', '-')
    print('-', '-', '-')
    print('-', '-', '-')


def printStage(stages):
    for i in range(1, 4):
        if i == 1:
            print(f"{stages[0]} {stages[1]} {stages[2]}")
        elif i == 2:
            print(f"{stages[3]} {stages[4]} {stages[5]}")
        elif i == 3:
            print(f"{stages[6]} {stages[7]} {stages[8]}")


def user1Winner(stages):
    if (stages[0] == 'X') and (stages[1] == 'X') and (stages[2] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[3] == 'X') and (stages[4] == 'X') and (stages[5] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[6] == 'X') and (stages[7] == 'X') and (stages[8] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[0] == 'X') and (stages[3] == 'X') and (stages[6] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[1] == 'X') and (stages[4] == 'X') and (stages[7] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[2] == 'X') and (stages[5] == 'X') and (stages[8] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[0] == 'X') and (stages[4] == 'X') and (stages[8] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[2] == 'X') and (stages[4] == 'X') and (stages[6] == 'X'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()


def equal(user1Chooses, user2Chooses):
    if len(user1Chooses) == 5 and len(user2Chooses) == 4:
        print("Equal")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()


def user2Winner(stages):
    if (stages[0] == 'O') and (stages[1] == 'O') and (stages[2] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[3] == 'O') and (stages[4] == 'O') and (stages[5] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[6] == 'O') and (stages[7] == 'O') and (stages[8] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[0] == 'O') and (stages[3] == 'O') and (stages[6] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[1] == 'O') and (stages[4] == 'O') and (stages[7] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[2] == 'O') and (stages[5] == 'O') and (stages[8] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[0] == 'O') and (stages[4] == 'O') and (stages[8] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()
    elif (stages[2] == 'O') and (stages[4] == 'O') and (stages[6] == 'O'):
        print("user1 won :)")
        ch = input("Do you want to countinue?(y/n)")
        if ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes' or ch == 'YES':
            os.system('cls')
            printFirstStage()
            playGame()
        else:
            print("End of game")
            sys.exit()


def playGame():
    stages = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    user1Chooses = []
    user2Chooses = []
    while 1:
        guesUser1 = int(
            input("user1: Please enter wich location you want(0-8)..."))

        while (guesUser1 >= 9 or guesUser1 < 0) or (guesUser1 in user1Chooses) or (guesUser1 in user2Chooses):
            print("Invalid location")
            guesUser1 = int(
                input("user1: Please enter wich location you want(0-8)..."))

        user1Chooses.append(guesUser1)
        stages.pop(guesUser1)
        stages.insert(guesUser1, 'X')

        os.system('cls')

        printStage(stages)

        user1Winner(stages)

        equal(user1Chooses, user2Chooses)

        guesUser2 = int(
            input("user2: Please enter wich location you want(0-8)..."))

        while (guesUser2 >= 9 or guesUser2 < 0) or (guesUser2 in user2Chooses) or (guesUser2 in user1Chooses):
            print("Invalid location")
            guesUser2 = int(
                input("user2: Please enter wich location you want(0-8)..."))

        user2Chooses.append(guesUser2)
        stages.pop(guesUser2)
        stages.insert(guesUser2, 'O')

        os.system('cls')

        printStage(stages)

        user2Winner(stages)


printFirstStage()
playGame()