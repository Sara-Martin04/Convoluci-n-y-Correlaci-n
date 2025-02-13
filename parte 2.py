import numpy as np
import matplotlib.pyplot as plt

# Parámetros
Ts = 1.25e-3  # Período de muestreo en segundos
fs = 1 / Ts  # Frecuencia de muestreo
n = np.arange(9)  # Valores de n de 0 a 8

# Definir señales
x1 = np.cos(2 * np.pi * 100 * n * Ts)
x2 = np.sin(2 * np.pi * 100 * n * Ts)

# Calcular correlación cruzada
corr = np.correlate(x1, x2, mode='full')
k = np.arange(-len(n) + 1, len(n))  # Ejes de correlación

# Graficar señales originales
plt.figure(figsize=(12,5))
plt.subplot(2,1,1)
plt.stem(n, x1, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.plot(n, x1, 'b-', alpha=0.5)
plt.stem(n, x2, linefmt='g-', markerfmt='go', basefmt='r-')
plt.plot(n, x2, 'g-', alpha=0.5)
plt.title("Señales")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.legend(["x1[n] = cos(2π100nTs)", "x2[n] = sin(2π100nTs)"])
plt.grid()

# Graficar la correlación cruzada
plt.subplot(2,1,2)
plt.stem(k, corr, linefmt='m-', markerfmt='mo', basefmt='r-')
plt.plot(k, corr, 'm-', alpha=0.5)
plt.title("Correlación de señales")
plt.xlabel("k")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.show()
