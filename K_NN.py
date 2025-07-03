import cv2
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.neighbors
import pandas as pd
import os

digits = sklearn.datasets.load_digits()

data = digits.data
labels = digits["target"]

target_folder = os.path.join(os.getcwd(), 'datasets')

files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))]

imagen = ""
while True:
    try:
        imagen = int(input(f"Seleccione un archivo: 0 al {len(files)-1}: "))
        img = f"datasets/n{imagen}.png"
        if imagen < len(files) and os.path.isfile(img):
            break
    except:
        pass
    print("Valor incorrecto")

mat = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

mat_re = cv2.resize(mat,(8,8))
mat_re = mat_re.flatten()

mat_normalized = ((255-mat_re)/255.0)*16

n = 3

while True:
    knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=n)
    knn.fit(data,labels)

    distances,neighbours = knn.kneighbors([mat_normalized],return_distance=True,n_neighbors=n)

    targets = []
    for i in neighbours[0]:
        targets.append(digits["target"][i])
    
    dc = {}

    for i in targets:
        dc[i] = targets.count(i)

    if len(dc.keys()) == n:
        done = False
        print(f"Con los vecinos actuales, pese a ser todos distintos, he detectado que el digito ingresado corresponde a: {list(dc.keys())[0]}.\n¿Quieres intentarlo nuevamente con un vecino más? Y/N")
        while True:
            ans = input().strip().lower()
            if ans == "n":
                done = True
                break
            elif ans == "y":
                n += 1
                break
        if done:
            break
    else:
        break

predicted = list(dc.keys())[list(dc.values()).index(max(list(dc.values())))]
print(f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {predicted}.")
print("Vecinos más cercanos:", neighbours[0])
print("Distancias: ",distances)

final_df = pd.DataFrame()

for numero in range(n):
    matriz = pd.DataFrame(digits["images"][neighbours[0][numero]])
    print(matriz)
    matriz.columns = [f'C{i}' for i in range(8)]
    matriz.insert(0, "Número", digits["target"][neighbours[0][2]])
    final_df = pd.concat([final_df, matriz], ignore_index=True)

    separador = pd.DataFrame([[""] * 9], columns=final_df.columns)
    final_df = pd.concat([final_df, separador], ignore_index=True)

final_df.to_excel("nearest_neightbours.xlsx", index=False)



