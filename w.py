#estructuras de control 1-5
for x in range(5):
    print(f"Hola {x}")
print("-----")
#5-9
for x in range(5,10):
    print(f"Hola {x}")
print("-----")
#5-10 en 3
for x in range(5,10,3):
    print(f"Hola {x}")
print("-----")
#10 a -1    
for x in range(10,0,-1):
    print(f"Hola {x}")
print("-----")
#multiplos de 4
xp=0
xf=20
for x in range(xp,xf,2):
    if(x % 4 == 0):
        print(f"hola {x}")
#ejemplo supermercado uso ifs
variable=input("Bienvenido al supermercado, para cerrar el menu darle al 0")
valor=float(input("Ingrese el valor de compra para determinar el descuento: "))
descuento=0
if(valor>=50000 and valor<80000):
     print("El descuento es del 5%")
    descuento=0.05
elif(valor>=80000 and valor<100000):
    print("El descuento es del 8%")
    descuento=0.08
elif(valor>=100000):
    print("El descuento es del 10%")
    descuento=0.1
else:
    print("No hay descuento")
totaldescuento=valor*descuento
valorf=valor-totaldescuento
    print("El valor a pagar es: ", valorf)

