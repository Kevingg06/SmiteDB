from random import sample

comillaSimple = "'"

def insertTable(clave1, clave2):
    print(f"values({comillaSimple}{clave1}{comillaSimple}, {comillaSimple}{clave2}{comillaSimple}")

def insertWithoutValues(clave1, clave2):
    print(f"({comillaSimple}{clave1}{comillaSimple}, {comillaSimple}{clave2}{comillaSimple}")

def printAll(lista1, lista2):
    insertTable(lista1[0], lista2[0])
    for i in range(1, len(lista1)):
        insertWithoutValues(lista1[i], lista2[i])


vector1 = ['Kevin Gonzalez', 'Damian Maldonado', 'Martín Galeano', 'Agustín Oliverio', 'Ezequiel Fernandez', 'Nicolás Lopez', 'Valentín Cañete', 'Benjamín Castro Madrid', 'Agustina Gonzalez', 'Matheo Moro']]

for i in range(90):
    vector1.append(vector1)

print(len(vector1))
print(len(vector2))

printAll(vector1, vector2)
