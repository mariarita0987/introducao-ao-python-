import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

horas_estudo = [1, 2, 3, 4, 5, 6, 2, 4, 5, 7, 8, 3, 6, 7, 8]
notas = [4, 5, 6, 7, 8, 10, 3, 6, 7, 8, 9,  8, 9, 5, 9]

plt.scatter(horas_estudo, notas)

coeficientes = np.polyfit(horas_estudo, notas, 1)
funcao_tendencia = np.poly1d(coeficientes)

plt.plot(horas_estudo, funcao_tendencia(horas_estudo), color='orange', linestyle='--')
plt.title("horas de estudo vs notas")
plt.xlabel("horas de estudo")
plt.ylabel("notas")
plt.show()