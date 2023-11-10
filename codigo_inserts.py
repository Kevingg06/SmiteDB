comillaSimple = "'"
def insertTable(clave1, clave2, clave3 ,clave4):
    print(f"values({comillaSimple}{clave1}{comillaSimple}, {comillaSimple}{clave2}{comillaSimple}, {comillaSimple}{clave3}{comillaSimple}, {comillaSimple}{clave4}{comillaSimple}),")

def insertWithoutValues(clave1, clave2, clave3 ,clave4):
    print(f"({comillaSimple}{clave1}{comillaSimple}, {comillaSimple}{clave2}{comillaSimple}, {comillaSimple}{clave3}{comillaSimple}, {comillaSimple}{clave4}{comillaSimple}),")

def printAll(lista1, lista2, lista3, lista4):
    for i in range(len(listaDificultades)):
        insertWithoutValues(lista1[i], lista2[i], lista3[i], lista4[i])

