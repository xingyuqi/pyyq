import random

def randomGuess():
    for i in range(5):
        guessNum = int(input())
        if guessNum < pickNum:
            print('number is smaller')
        elif guessNum > pickNum:
            print('number is bigger')
        else:
            break

    if guessNum ==  pickNum :
        return 'win'
    else:
        return 'lose'

print('Pick up a number between 1 - 20')
print('Please input a number')
pickNum = random.randint(1,20)
print(randomGuess())



