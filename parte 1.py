import numpy as np 
import matplotlib.pyplot as plt

def plot_convolutions(signals):
    fig, axes = plt.subplots(len(signals), 1, figsize=(10, 4 * len(signals)))
    if len(signals) == 1:
        axes = [axes]
    
    for ax, (y_n, x_n, title) in zip(axes, signals):
        # Calcular la convolución
        conv_result = np.convolve(x_n, y_n)
        
        # Eje de tiempo para la señal resultante
        n_conv = np.arange(len(conv_result))
        
        # Graficar la convolución
        ax.stem(n_conv, conv_result, linefmt='b-', markerfmt='bo', basefmt='r-')
        ax.plot(n_conv, conv_result, 'b-', alpha=0.5)  # Línea continua para mejor visualización
        ax.set_xlabel('n')
        ax.set_ylabel('Amplitud')
        ax.set_title(title)
        ax.grid()
        
        print(f"Resultado de la convolución ({title}):", conv_result)
    
    plt.tight_layout()
    plt.savefig("convoluciones.png")
    plt.show()
    print("Imagen guardada como convoluciones.png")

# Definir las señales discretas y realizar la convolución para cada caso
signals = [
    (np.array([5, 6, 0, 0, 6, 7, 4]), np.array([1, 0, 7, 6, 7, 3, 6, 7, 3, 2]), 'Convolución de Paula'),
    (np.array([5, 6, 0, 0, 6, 9, 8]), np.array([1, 0, 0, 6, 7, 9, 6, 6, 1, 8]), 'Convolución de Sara'),
    (np.array([5, 6, 0, 0, 7, 1, 6]), np.array([1, 0, 7, 4, 5, 5, 8, 9, 9, 0]), 'Convolución de Cristian')
]

plot_convolutions(signals)
