import random

amax = 100
amin = 0
vastus = random.randint(amin, amax)
algarv = 101

while algarv != vastus:
    algarv = int(input("arv: "))
    if algarv > vastus:
        print ("liiga suur")
    elif algarv < vastus:
        print ("liiga väike")
print ("õige vastus!")