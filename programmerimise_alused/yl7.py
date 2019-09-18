#Nimi
first_name = input("Nimi: ")
if first_name == "Jaanus":
    print ("No Tere Jaanus!")
else:
    print ("Tere, " + first_name + "!")
#Elukoht
location = input("Elukoht: ")
if location == "Saaremaa":
    print ("Vinge!!")
elif location == "Õnne 13":
    print ("dun-dundundun--dundun-dun-dadunda")
#Vanus
age = int(input("Vanus: "))
if age <= 17:
    print ("Olete liiga noor auto juhtimiseks.")
elif age == 18:
    print ("Õnnitleme täisealiseks saamise puhul!")
else:
    print ("Võite autot juhtida. ")
