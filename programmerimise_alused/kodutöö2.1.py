import random

Max1 = 100
Min1 = 1
#For random: random.randint(Min1,Max1)
#For predefined: put the numbers in list1 and remove lines 9 - 11
list1 = []
Number = 5
for i in range(1, Number + 1):
    value = int(input("Sisend %d : " %i))
    list1.append(value)

print("Sisend: ", list1)
list1.sort()
print("Väljund: ", list1[Number - 2])
