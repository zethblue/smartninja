# Initialisieren, Append, +, index referenzieren, slicen, len, in for schleife benutzen, remove

sweets = ["StrawberryJam"]
print sweets
fruits = ["Peach"]
print fruits
print " "

sweets.append("Chocolate")
print sweets
fruits.append ("Apple")
print " "

sweets.append(raw_input("Insert a sweet here"))
fruits.append(raw_input("Insert a Fruit here"))

sweetfruit = sweets + fruits
print sweetfruit
print " "
print "Length of List" ##LEN benutzen
print len(sweetfruit)
print " "
##Slicen##
print sweets[:-1]
print fruits[-1:]

sweets.pop(2)
print sweets
print sweetfruit



