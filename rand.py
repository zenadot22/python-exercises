#task1
#printing random numbers
import random
rand = int(input("enter a number\n"))
r = random.randint(1,100)
while True:
        if rand ==r:
            print("correct guess")
            break
        if rand<r:
            print("guess too low",r)
            rand = int(input("enter a number"))
            continue
        if rand>r:
            print("guess too high",r)
            rand = int(input("enter a number"))
            continue
        else:
            print("out of range",r)
            continue

