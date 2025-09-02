boleano =  ("1" == 1)
print(type(boleano), boleano)
boleano2 =  "char" * 3
print(type(boleano2), boleano2)
booleano3 = str(5 * 3)
print(type(booleano3), booleano3)
#funciones ejercicio encuesta para 6 users
# Nombre
# Carrera
# Idea de proyecto para este curso 
for x in range(7,1):
    nombre= input("¿Cual es tu nombre? ")
    carrera= input("Dime la carrera que estas estudiando ")
    idea= input("¿Cual es tu idea de proyecto para el curso POO? ")
    print("Tu nombre es: ", nombre)
    print("Estas estudiando: ", carrera) 
    print("Tu idea de proyecto es: ", idea)
    