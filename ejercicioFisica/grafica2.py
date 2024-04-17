import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
a = 1  # Radio interior del cilindro interior
b = 2  # Radio exterior del cilindro interior / Radio interior del cilindro exterior
c = 3  # Radio exterior del cilindro exterior
l = 1  # Carga positiva uniforme por unidad de longitud en el cilindro interior

# Función para calcular el campo eléctrico E en función de la distancia r desde el eje del cable
def calcular_campo_electrico(r):
    epsilon_0 = 8.85e-12  # Permitividad del vacío
    if r < a:
        return 0  # Campo eléctrico cero dentro del cilindro interior
    elif a <= r < b:
        return l / (2 * np.pi * epsilon_0 * r)  # Campo eléctrico dentro del cilindro interior
    elif b <= r <= c:
        return l / (2 * np.pi * epsilon_0 * r)  # Campo eléctrico dentro del cilindro exterior
    else:
        return 0  # Campo eléctrico cero fuera del cilindro exterior

# Valores de r desde 0 hasta 2c
r_values = np.linspace(0.01,  8, 100)
# Calcular el campo eléctrico para cada valor de r
E_values = [calcular_campo_electrico(r) for r in r_values]

# Graficar el campo eléctrico en función de r
plt.plot(r_values, E_values)
plt.title('Campo Eléctrico en función de la distancia desde el eje del cable')
plt.xlabel('Distancia desde el eje del cable (m)')
plt.ylabel('Campo Eléctrico (N/C)')
plt.grid(True)
plt.show()
