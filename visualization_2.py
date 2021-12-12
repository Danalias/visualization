from os import stat
import numpy as np
import csv
import pandas as pd
import plotly.express as px

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

select_row = [2, 3, 11, 22]

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
        if (float(row[2]) < 10):
            mass = np.append(mass, float(row[2]))
            radius = np.append(radius, float(row[3]))
            temperature = np.append(temperature, float(row[11]))
            star_temp = np.append(star_temp, float(row[22]))

labels={"Mass": "Mass", "Radius": "Radius", "Period": "Period", "S-Maxis": "Semi-Major Axis", "e": "Eccentricity", "Incinat°": "Inclination", "Temp(K)": "Temperature"}

data['Mass'] = mass
data['Radius'] = radius
data['Temp(K)'] = temperature
data['STemp(K)'] = star_temp

subDf = pd.DataFrame(data, columns=["Mass", "Radius", "Temp(K)", "STemp(K)"])
fig = px.parallel_coordinates(subDf,
                              color="Mass",
                              labels=labels,
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2)
fig.write_image("parallel_coordinate_plot.pdf")