import random
numbers = random.sample(range(73), 4)
print ("sisend: " + str(numbers))
numbers2 = [ numbers[0], numbers[-1] ]
print ("väljund: " + str(numbers2))