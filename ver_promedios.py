from sklearn import datasets
import numpy as np
import pandas as pd

losDigitos = datasets.load_digits()


promedios = {}

for numero in range(10):
    imagenes = losDigitos.images[losDigitos.target == numero]
    promedio = np.mean(imagenes, axis=0)
    promedios[numero] = np.round(promedio, 2)

final_df = pd.DataFrame()

for numero in range(10):
    matriz = pd.DataFrame(promedios[numero])
    matriz.columns = [f'C{i}' for i in range(8)]
    matriz.insert(0, "Número", numero)
    final_df = pd.concat([final_df, matriz], ignore_index=True)

    separador = pd.DataFrame([[""] * 9], columns=final_df.columns)
    final_df = pd.concat([final_df, separador], ignore_index=True)


final_df.to_excel("matrices_promedio_vertical.xlsx", index=False)

final_df.to_csv("matrices_promedio_vertical.csv", index=False)





