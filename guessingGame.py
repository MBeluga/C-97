import random
randomnum = random.randint (1,9)
print (randomnum)
guess = input ("Enter your guess:")
if guess == randomnum:
        print ("You win!")
else:
    while guess != randomnum:
        print ("Try Again!")
        guess = input ("Enter your guess:")
        if guess == randomnum:
            print ("You win!")