# Convoluci-n-y-Correlaci-n
## Descripción 
Este proyecto contiene el código para mostrar diferentes tipos de señales, entre ellas una señal EEG obtenida del sitio web Physionet, del estudio EEG signals from an RSVP Task (Señales EEG de una presentación visual serial rápida); también tres gráficos resultantes de la convolución de los dígitos de las cédulas y los dígitos de los códigos estudiantiles; y para la última gráfica se realizó la correlación entre dos señales.  

Este proyecto se dividió en tres partes: 

### Parte a (Señal resultante de la convolución) 

[1] Convolución =  Esta es un operación matemática entre dos señales, es decir dos funciones que su resultado es una tercera función,para que se entienda mejor piensa que tu estas en la playa y caminas en la arena viendo como tus huellas dejan rastro en ella,pero alguien más pisar tus huellas con un pie volteado, la convolución es ver como estas dos huellas se combinan cuando una está normal y la otra en el sentido contrario. Se utiliza en procesamiento de señales,filtrado y análisis de sistemas.

![Imagen de WhatsApp 2025-02-12 a las 21 47 05_f056a580](https://github.com/user-attachments/assets/1b176788-d6c1-4e43-8a28-4967150ce6cc)


Teniendo en cuenta tres diferentes sistemas los cuales son: 

h1[n]={5,6,0,0,6,7,4}

h2[n]={5,6,0,0,6,9,8}

h3[n]={5,6,0,0,7,1,6}
 
Y tres diferentes señales las cuales son:

x1[n]={1,0,7,6,7,3,6,7,3,2}

x2[n]={1,0,0,6,7,9,6,6,1,8}

x3[n]={1,0,7,4,5,5,8,9,9,0}

Con estos tres sistemas y estas tres señales, se encontró la señal resultante de la convolución por medio de dos tipos de cálculos, manuales y con las funciones de python. 

![IMG_0120 jpeg](https://github.com/user-attachments/assets/e79f8ed0-0c14-47d0-9838-83771375d3f4)

*calculos manuales*

![IMG_0119 jpeg](https://github.com/user-attachments/assets/4fcbf68f-5c8c-4130-ae0a-d3b7fe4464c4)

*calculos python*

También se obtuvieron gráficas  con los dos tipos de cálculos manuales y de las funciones de python.

 ![IMG_0124 jpeg](https://github.com/user-attachments/assets/fc475528-91b2-4d60-a058-e42c1610a2d3)
 
*graficas manuales*

![convoluciones](https://github.com/user-attachments/assets/e9d91491-b652-4721-bccd-146e764eb813)

*graficas python*

Para realizar los calculos y graficas en python realizamos el siguiente codigo:
```
        #calcular la convolucion
        conv_result = np.convolve(x_n, y_n)
        
        # Eje de tiempo para la señal r
        n_conv = np.arange(len(conv_result))
        
        # Graficar la convolución
        ax.stem(n_conv, conv_result, linefmt='b-', markerfmt='bo', basefmt='r-')
        ax.plot(n_conv, conv_result, 'b-', alpha=0.5)  # Línea continua para mejor visualización
        ax.set_xlabel('n')
        ax.set_ylabel('Amplitud')
        ax.set_title(title)
        ax.grid()
```
definiendo las señales de la siguiente manera:
```
# Definir las señales discretas y realizar la convolución para cada caso
signals = [
    (np.array([5, 6, 0, 0, 6, 7, 4]), np.array([1, 0, 7, 6, 7, 3, 6, 7, 3, 2]), 'Convolución de Paula'),
    (np.array([5, 6, 0, 0, 6, 9, 8]), np.array([1, 0, 0, 6, 7, 9, 6, 6, 1, 8]), 'Convolución de Sara'),
    (np.array([5, 6, 0, 0, 7, 1, 6]), np.array([1, 0, 7, 4, 5, 5, 8, 9, 9, 0]), 'Convolución de Cristian')
]

plot_convolutions(signals)
```

### Parte B (Correlación entre dos señales)   


[1] Correlación : Acá se puede evidenciar que tan parecidas son las señales,mide la similitud entre dos señales, imaginemos que queremos encontrar la relación entre dos canciones, lo que hacemos es tomar un fragmento de cada canción colocándolos uno encima del otro comparando cada pedazo y mirando que tan similares son; existen dos tipos de correlación 

- Correlación cruzada :Comparar dos señales diferentes para encontrar similitudes en distintas posiciones en el tiempo.
  
  ![Imagen de WhatsApp 2025-02-12 a las 21 47 58_9aa3ae57](https://github.com/user-attachments/assets/1a04d022-004f-45ba-90d7-031fb81d911e)


- Autocorrelación: Compara una señal consigo misma para detectar patrones repetitivos.
  
  ![Imagen de WhatsApp 2025-02-12 a las 21 48 26_45671dda](https://github.com/user-attachments/assets/d75cb76c-1684-4bbf-93ed-16adb339bbac)

Para realizar esta parte de la practica implementamos el siguiente codigo:

1. se define la señal y se calcula la correlacion
```
# Definir señales
x1 = np.cos(2 * np.pi * 100 * n * Ts)
x2 = np.sin(2 * np.pi * 100 * n * Ts)

# Calcular correlación cruzada
corr = np.correlate(x1, x2, mode='full')
k = np.arange(-len(n) + 1, len(n))  # Ejes de correlación
```

2. Se grafica la señal original
```
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
```

4. Se grafica la correlacion cruzada
```
# Graficar la correlación cruzada
plt.subplot(2,1,2)
plt.stem(k, corr, linefmt='m-', markerfmt='mo', basefmt='r-')
plt.plot(k, corr, 'm-', alpha=0.5)
plt.title("Correlación de señales")
plt.xlabel("k")
plt.ylabel("Amplitud")
plt.grid()
```
Obtuvimos lo siguiente:

![correlacion](https://github.com/user-attachments/assets/991743dc-10ce-473f-823b-e9feb7686747)
*señal original y señal correlacion cruzada*

### Parte C (Señal EEG) 
Para esta última parte de la práctica se utilizó datos de la extensión .edf del estudio Señales EEG de una presentación visual serial rápida (RSVP) a diferentes velocidades de 5, 6 y 10 Hz, los datos que elegimos fueron los del paciente 13 a los 10 Hz

### Referencias
[1]. HERNÁNDEZ, A., MORA, N. J. E., & VEGA, H. R. (2020). Enseñanza en el análisis de señales aleatorias usando correlación y sus aplicaciones. Utopía y Praxis Latinoamericana, 25(3), 190-200.

