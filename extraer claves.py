codigo = input("Ingrese los inserts: ")
vector = []

comillas = codigo.index('"')
coma = codigo.index(',')
parentesis = codigo.index('(')
cantParentesis = codigo.count('(')
aux = codigo

for i in range(len(codigo)):
    if cantParentesis > 0:
        #print(parentesis)
        parentesis = aux.index('(')
        aux = aux[parentesis+1:]
        cantParentesis -= 1
        comillas = aux.index('"')
        coma = aux.index(',')
        vector.append(aux[1:coma-1])
print(vector)
