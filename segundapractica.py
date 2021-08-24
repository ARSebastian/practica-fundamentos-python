# Imprimir tu nombre
nombre = input("introduce tu nombre: ")
print(f"hola {nombre}")
print("Hola, {}". format (nombre))

tuedad = input("introduce tu edad:")
tuedad = int(tuedad)

#estructura de control if
if tuedad >= 18 and tuedad < 100:
    print("eres mayor de edad")
elif tuedad >= 100:
    print("eres inmortal?")
else :
    print("Eres menor de edad")

#estructura de control for
for i in range (0, 10):
    print(i)

