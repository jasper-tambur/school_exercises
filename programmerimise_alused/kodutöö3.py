n=int(input("Sisend: "))
list1 = [k * k for k in range(0, n)]
print("Väljund: ", ", ".join( repr(e) for e in list1 ) )
