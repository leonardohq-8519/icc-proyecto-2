from sklearn import datasets
import numpy as np

def calcular_promedio(ver=False):
    losDigitos = datasets.load_digits()


    imagenes_por_digito = {}
    for numero in range(10):
        if ver:
            imagenes = losDigitos.images[losDigitos.target == numero]
        else:
            imagenes = losDigitos.data[losDigitos.target == numero]
        imagenes_por_digito[numero] = imagenes


    promedios = {}
    for numero in range(10):
        promedio = np.mean(imagenes_por_digito[numero], axis=0)
        promedios[numero] = promedio
    return promedios

def main():
    promedios = calcular_promedio(ver=True)
    while True:
        entrada = input("Escribe un número del 0 al 9 para ver su imagen promedio: ")

        if entrada.isdigit():
            numero = int(entrada)
            if 0 <= numero <= 9:
                print(f"\n Matriz promedio del número {numero}:")
                np.set_printoptions(suppress=True)
                print(np.round(promedios[numero], 2))
                break
            else:
                print("El número debe estar entre 0 y 9.\n")
        else:
            print("Entrada inválida. Por favor escribe un número del 0 al 9.\n")

if __name__ == "__main__":
    main()
