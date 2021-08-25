#ibreria para generar datos aleatorios
import random

#libreria para generar graficas
import matplotlib.pyplot as plt

#Generar un numero aleatorio y lo imprime
print(random.randrange(10, 100, 2))

#Declara la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Imprime la lista
print("lista original", lista)
#mezcla los elementos de la lista al azar
random.shuffle(lista)
#imprime la lista mezclada
print("lista mixeada", lista)

#genera una grafica de campana de gauss
#genera los datos de la grafica
campana = [random.gauss(1,0.5) for i in range(1000)]
#arma la grafica
plt.hist(campana, bins=15)
#muestra la grafica
plt.show()