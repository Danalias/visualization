from os import stat
import numpy as np
import matplotlib.pyplot as plt
import csv
import math
import seaborn as sn
import pandas as pd
from tools import *
import time

file_name = "oec.csv"

names = np.array(list())
mass = np.array(list())
period = np.array(list())
radius = np.array(list())
semimajoraxis = np.array(list())
eccentricity = np.array(list())
inclination = np.array(list())
temperature = np.array(list())
star_temp = np.array(list())

select_row = [2, 3, 4, 5, 6, 10, 11, 22]

data = dict()

with open(file_name, 'r') as f:
    reader = csv.reader(f)
    i = 0
    passed = False
    for row in reader:
        passed = False
        if (i == 0):
            i = 1
            continue
        for nb in select_row:
            if (row[nb] == ''):
                passed = True
        if (passed):
            continue
            # On prend les valeurs à moins de 10 masses de Jupiter et à moins de 10000 jours de révolution (outliers)
        if (float(row[2]) < 10 and float(row[4]) < 10000):
            names = np.append(names, row[0])
            mass = np.append(mass, float(row[2]))
            radius = np.append(radius, float(row[3]))
            period = np.append(period, float(row[4]))
            semimajoraxis = np.append(semimajoraxis, float(row[5]))
            eccentricity = np.append(eccentricity, float(row[6]))
            inclination = np.append(inclination, float(row[10]))
            temperature = np.append(temperature, float(row[11]))
            star_temp = np.append(star_temp, float(row[22]))

data['Mass'] = mass
data['Radius'] = radius
data['Period'] = period
data['S-Maxis'] = semimajoraxis
data['e'] = eccentricity
data['Inclinat°'] = inclination
data['Temp(K)'] = temperature
data['STemp(K)'] = star_temp

plt.hist(mass, bins=calculate_bins(mass))
plt.ylabel('Nombre de Planètes')
plt.xlabel('Masse (en masses de Jupiter)')
plt.savefig("Analyse_masse.pdf")

plt.clf()

plt.hist(period, bins=calculate_bins(period))
plt.ylabel('Nombre de Planètes')
plt.xlabel('Période de Révolution (en jours))')
plt.savefig("Analyse_période.pdf")

plt.clf()

plt.hist(radius, bins=calculate_bins(radius))
plt.ylabel('Nombre de Planètes')
plt.xlabel('Rayon (en rayons de Jupiter)')
plt.savefig("Analyse_rayon.pdf")

plt.clf()

plt.hist(semimajoraxis, bins=calculate_bins(semimajoraxis))
plt.ylabel('Nombre de Planètes')
plt.xlabel('Demi-Grand Axe (en unités astronomiques)')
plt.savefig("Analyse_DM_Axe.pdf")

plt.clf()

plt.hist(eccentricity, bins=calculate_bins(eccentricity))
plt.ylabel('Nombre de Planètes')
plt.xlabel('Excentricité (pas d\'unités)')
plt.savefig("Analyse_excentricité.pdf")

plt.clf()

plt.hist(inclination, bins=calculate_bins(inclination))
plt.ylabel('Nombre de Planètes')
plt.xlabel('Inclinaison (en degré)')
plt.savefig("Analyse_inclinaison.pdf")

plt.clf()

plt.hist(temperature, bins=calculate_bins(temperature))
plt.ylabel('Nombre de Planètes')
plt.xlabel('Température (en Kelvin)')
plt.savefig("Analyse_température.pdf")

plt.clf()


print(f"Moyenne de la période: {np.mean(period)}")
print(f"Ecart type de la période: {np.std(period)}")
print(f"Ecart type de la masse: {np.std(mass)}")
print(f"Ecart type du rayon: {np.std(radius)}")
print(f"Ecart type du demi-grand axe: {np.std(semimajoraxis)}")
print(f"Ecart type de l'excentricité: {np.std(eccentricity)}")
print(f"Ecart type de l'inclinaison: {np.std(inclination)}")
print(f"Ecart type de la température: {np.std(temperature)}")


subDf = pd.DataFrame(data, columns=["Mass", "Radius", "Period", "S-Maxis", "e", 'Inclinat°', "Temp(K)", "STemp(K)"])

corrMatrix = subDf.corr()

sn.heatmap(corrMatrix, annot=True)
plt.savefig("Matrice_Corrélation.pdf")

plt.clf()

def outliersDetection():
    df = pd.read_csv ('oec.csv')
    array = df.to_numpy()
    plt.plot(array[:, 2], array[:, 3], "o", markersize=1)
    plt.savefig("miseEnEvidenceOutliers.pdf")
    nb_points = array.shape[0]
    # On s'apercois en regardant le graph produit qu'il y a des outliers

outliersDetection()