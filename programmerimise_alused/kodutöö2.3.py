list1 = [1, 1, 1, 2, 2, 3, 6, 6, 6, 6, 5, 5, 5, 5]

print("Sisend: ", list1)
list1 = list(dict.fromkeys(list1))
list1.sort()
print("Väljund: ", list1[-2])
