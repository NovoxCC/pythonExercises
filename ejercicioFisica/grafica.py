import numpy as np
import matplotlib.pyplot as plt

# Definir la permitividad eléctrica en el vacío (F/m)
EPS = 8.85e-12

# Definir la función de campo eléctrico E(r)
def E(r):
    return 1 / (2 * np.pi * EPS * r)

# Definir el intervalo de distancias desde el eje del cable (r)
r_values = np.linspace(0.01, 2, 100)  # Empezamos desde 0.01 para evitar división por cero

# Calcular la magnitud del campo eléctrico en cada punto del intervalo
E_values = E(r_values)

# Trazar la magnitud del campo eléctrico en función de la distancia desde el eje del cable
plt.plot(r_values, E_values)
plt.xlabel('Distancia desde el eje del cable (m)')
plt.ylabel('Magnitud del campo eléctrico (N/C)')
plt.title('Magnitud del campo eléctrico en función de la distancia desde el eje del cable')
plt.grid(True)
plt.savefig('campo_electrico.png')
plt.show()
