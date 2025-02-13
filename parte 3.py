import pyedflib
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# Cargar la señal desde un archivo EDF
archivo = "rsvp_10Hz_13b.edf"
f = pyedflib.EdfReader(archivo)

# Obtener datos de la señal
num_canales = f.signals_in_file
canales = f.getSignalLabels()
fs = f.getSampleFrequencies()[0]  # Frecuencia de muestreo (asumimos la misma para todos los canales)

# Selección de canal
canal_seleccionado = 0
senal = f.readSignal(canal_seleccionado)
nombre_canal = canales[canal_seleccionado]

# Crear vector de tiempo en segundos
max_tiempo = 5  # Reducir el tiempo a los primeros 5 segundos
num_muestras = int(fs * max_tiempo)

tiempo = np.arange(num_muestras) / fs
senal = senal[:num_muestras]

# Caracterización de la señal
total = np.sum(senal)
media_manual = np.mean(senal)
desv_manual = np.std(senal)
coef_var_manual = desv_manual / media_manual

# Clasificación de la señal
clasificacion = "Señal fisiológica" if "EEG" in nombre_canal else "Otra señal biomédica"

# Transformada de Fourier
y_f = fft(senal)
freqs = fftfreq(len(senal), 1/fs)

# Estadísticos en función de la frecuencia
frecuencia_media = np.mean(np.abs(freqs))
frecuencia_mediana = np.median(np.abs(freqs))
desviacion_frecuencia = np.std(np.abs(freqs))

# Histograma de frecuencias con mayor cantidad de bins para columnas más bajas
bins_count = 60  # Aumentando el número de bins
hist_f, bins_f = np.histogram(np.abs(freqs), bins=bins_count, density=True)
bin_centers_f = (bins_f[:-1] + bins_f[1:]) / 2

# Gráficos
fig, axs = plt.subplots(3, 1, figsize=(12, 12), constrained_layout=True)

# Señal en función del tiempo
axs[0].plot(tiempo, senal, color='pink')
axs[0].set_title(f"Señal EEG")
axs[0].set_xlabel("Tiempo (s)")
axs[0].set_ylabel("Amplitud")
axs[0].grid()

# Transformada de Fourier
axs[1].plot(freqs[:len(freqs)//2], np.abs(y_f[:len(y_f)//2]), color='blue')
axs[1].set_title("Transformada de Fourier de la Señal")
axs[1].set_xlabel("Frecuencia (Hz)")
axs[1].set_ylabel("Magnitud")
axs[1].grid()

# Histograma de frecuencias mejorado con densidad de probabilidad
axs[2].bar(bin_centers_f, hist_f, width=np.diff(bins_f)[0], color='teal', alpha=0.7, edgecolor='black', linewidth=1.2)
axs[2].plot(bin_centers_f, hist_f, color='red', linewidth=2, label="Densidad de Probabilidad")
axs[2].set_title("Histograma")
axs[2].set_xlabel("Frecuencia (Hz)")
axs[2].set_ylabel("Densidad")
axs[2].grid(axis='y', linestyle='--', alpha=0.7)
axs[2].legend()

# Agregar datos estadísticos en la interfaz
stats_text = f"""
Clasificación de la señal: {clasificacion}
Frecuencia de muestreo: {fs:.2f} Hz
Media de la señal: {media_manual:.4f}
Desviación estándar de la señal: {desv_manual:.4f}
Coeficiente de variación: {coef_var_manual:.4f}
Frecuencia media: {frecuencia_media:.4f} Hz
Frecuencia mediana: {frecuencia_mediana:.4f} Hz
Desviación estándar de la frecuencia: {desviacion_frecuencia:.4f} Hz
"""
axs[2].text(0.05, -0.5, stats_text, transform=axs[2].transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(facecolor='white', alpha=0.7))

plt.show()

# Cerrar el archivo EDF
f._close()
