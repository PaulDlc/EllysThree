#Ingresando numero de filas
N = int(input("Ingrese numero de filas (entre 1 y 50): "))
while(N<1 or N>50):
    N = int(input("DATO ERRONEO!! INGRESE VALOR ENTRE 1 Y 50 NUEVAMENTE: "))

#Ingresando numero de columnas
M = int(input("Ingrese numero de columnas (entre 1 y 50): "))
while(M<1 or M>50):
    M = int(input("DATO ERRONEO!! INGRESE VALOR ENTRE 1 Y 50 NUEVAMENTE: "))

#Crear lista donde se guardaran los numeros
lista_numeros = []

#guardando numeros para la matriz
for i in range(N):
    b = "Ingrese fila " + str(i+1) + " con "+ str(M) + " numeros: "
    cadena = input(b)
    while (len(cadena) != M):
        cadena=input("DATOS ERRONEOS POR FAVOR INGRESE CADENA NUAVAMENTE: ")
    lista_numeros.append(cadena)

print("-------------------------------------------------------------------------\n")
print("Matriz Original:\n")
for i in range(len(lista_numeros)):
    print(lista_numeros[i])
print("-------------------------------------------------------------------------\n")
#Contador de cambios
cont = 0

#Convirtiendo cada fila en multiplos de 3
for i in range(N):
    b = int(lista_numeros[i])
    if (b % 3 == 0):
        b = list(lista_numeros[i])
    elif (b % 3 == 1):
        b = list(lista_numeros[i])
        for j in range(len(b)):
            b[j] = int(b[j])
            
        for j in range(len(b)):
            if b[j] != 0 and b[j] != 9:
                b[j] = b[j] -1
                cont = cont+1
                break
    elif (b % 3 == 2):
        b = list(lista_numeros[i])
        for j in range(len(b)):
            b[j] = int(b[j])

        for j in range(len(b)):
            if b[j] != 0 and b[j] != 9:
                b[j] = b[j] + 1
                cont = cont + 1
                break
    for j in range(len(b)):
        b[j] = str(b[j])
    b= "".join(b)
    lista_numeros[i] = b

print("Matriz con filas multiplos de 3:\n")
for i in range(len(lista_numeros)):
    print(lista_numeros[i])
print("-------------------------------------------------------------------------\n")

print("Total de cambios hechos: " + str(cont))
