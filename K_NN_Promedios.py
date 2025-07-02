import cv2
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.neighbors
import sacar_promedios
import os

digits = sklearn.datasets.load_digits()

data = digits.data
labels = digits["target"]

avg = sacar_promedios.calcular_promedio()


#Version sin numpy / Me retiré de progra I:

'''
avg = {}
for i in range(len(labels)):
    if labels[i] in avg.keys():
        avg[labels[i]].append(data[i])
    else:
        avg[labels[i]] = [data[i]]

for j in avg.keys():
    li = []
    for k in range(len(avg[j][0])):
        val = []
        for l in range(len(avg[j])):
            val.append(avg[j][l][k])
        li.append(sum(val)/len(avg[j]))
    avg[j] = li
'''

target_folder = os.path.join(os.getcwd(), 'datasets')

files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))]

imagen = ""
while True:
    try:
        imagen = int(input(f"Seleccione un archivo: 0 al {len(files)-1}: "))
        img = f"datasets/n{imagen+1}.png"
        if imagen < len(files) and os.path.isfile(img):
            break
    except:
        pass
    print("Valor incorrecto")

mat = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
mat_re = cv2.resize(mat,(8,8))
mat_re = mat_re.flatten()

mat_normalized = ((255-mat_re)/255.0)*16

knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(list(avg.values()),list(avg.keys()))

predicted = knn.predict([mat_normalized])[0]
distances,neighbours = knn.kneighbors([mat_normalized],return_distance=True)

print(f"Soy la inteligencia artificial versión 2, y he detectado que el dígito ingresado corresponde al número {predicted}.")
print("Vecinos más cercanos:", neighbours[0])
print("Distancias: ",distances)

print(digits["images"][neighbours[0][0]])
