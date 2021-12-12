import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize():
    a = 1
    b = 2
    p = 99

    i = 1

    df = pd.read_csv("oec.csv")
    columnsNamesArr = df.columns.values
    while i < len(columnsNamesArr):
        print(str(i) + " = " + columnsNamesArr[i])
        i = i + 1
    
    a = int(input("entrez un chiffre entre 1 et 24 (default = 1):") or "1")
    b = int(input("entrez encore un chiffre entre 1 et 24 (default = 2):") or "2")
    p = int(input("entrez encore un pourcentage d'affichage des data entre 1 et 100 (default = 2):") or "2")
    size = int(df.shape[0]*p/100)
    df = df[:size]
    print(df)

    array = df.to_numpy()
    plt.plot(array[:, a], array[:, b], "o", markersize=1)
    plt.title(columnsNamesArr[a] + " in function of " + columnsNamesArr[b])
    plt.xlabel(columnsNamesArr[a])
    plt.ylabel(columnsNamesArr[b])
    plt.show()
    print(array)
    
def main():
    visualize()
    
if __name__ == "__main__":
    main()