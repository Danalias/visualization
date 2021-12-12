from faker import Faker
import names
import random
from random import randint

import pandas as pd
import numpy as np

from termcolor import colored

import matplotlib.pyplot as plt

class Generator:
    def __init__(self):
        self.fake = Faker()

        self.df = pd.DataFrame(columns=('fullName', 'gender', 'age', 'address', 'numberPurchases', 'totalSpent', 'livingDistanceFromClosestShop'))
        self.size = randint(310, 400)
        
        self.current = 0

        self.success("Ready to generate a dataset of size " + str(self.size))
        self.generate()

    def success(self, str):
        print(colored("SUCCESS: " + str, 'green'))

    def warning(self, str):
        print(colored("WARNING: " + str, 'yellow'))

    def failure(self, str):
        print(colored("FAILURE: " + str, 'red'))

    def generate(self):
        while self.current < self.size:
            self.generateNameAndAge()
            self.current = self.current + 1
        self.generateNumberPurchases()
        self.generateTotalSpent()
        self.generateDistance()

    def generateDistance(self):
        i = 0
        dist = 1

        while i < self.size:
            if self.df.loc[i, 'numberPurchases'] >= 6:
                dist = randint(1, 3)
            elif self.df.loc[i, 'numberPurchases'] >= 4:
                dist = randint(5, 7)
            elif self.df.loc[i, 'numberPurchases'] >= 2:
                dist = randint(7, 10)
            else:
                dist = randint(10, 15)
                self.warning(str(dist))
            self.df.loc[i, 'livingDistanceFromClosestShop'] = dist
            i = i + 1

    def generateAmountSpent(self):
        minPurchase = 1.99
        maxPurchase = 99.99

        amountSpent = round(random.uniform(minPurchase, maxPurchase), 2)
        self.success("Amount generated is " + str(amountSpent))
        return(amountSpent)

    def generateTotalSpent(self):
        i = 0

        while i < self.size:
            tmp = 0
            j = 0
            while j < self.df.loc[i, 'numberPurchases']:
                tmp = tmp + self.generateAmountSpent()
                j = j + 1
            self.df.loc[i, 'totalSpent'] = tmp
            print(i, " totalSpent = ", tmp)
            i = i + 1
            
    def generateNumberPurchases(self):
        i = 0
        j = 0

        numberPurchases = []

        while i < 4*self.size/5:
            numberPurchases.append(randint(1, 3))
            i = i + 1
        while i < self.size:
            numberPurchases.append(randint(1, 10))
            i = i + 1
        random.shuffle(numberPurchases)
        print(numberPurchases)
        print(self.calcMean(numberPurchases))
        self.optimizeMean(numberPurchases)

        while j < self.size:
            self.df.loc[j, 'numberPurchases'] = numberPurchases[j]
            j = j + 1
        
    def calcMean(self, numberPurchases):
        result = 0
        
        for i in numberPurchases:
            result = result + i

        return(result/len(numberPurchases))

    def pullDown(self, numberPurchases):
        upper = 0
        j = 0

        for i in numberPurchases:
            if i > upper:
                upper = i

        while j < len(numberPurchases):
            if numberPurchases[j] == upper:
                numberPurchases[j] = upper - 1
            j = j + 1
        
        print(numberPurchases)
        print(self.calcMean(numberPurchases))

    def pullUp(self, numberPurchases):
        downer = 10
        j = 0

        for i in numberPurchases:
            if i < downer:
                downer = i
        while j < len(numberPurchases):
            if numberPurchases[j] == downer:
                numberPurchases[j] = downer + 1
            j = j + 1
        
        print(numberPurchases)
        print(self.calcMean(numberPurchases))

    def optimizeMean(self, numberPurchases):
        while self.calcMean(numberPurchases) >= 2.7:
            self.pullDown(numberPurchases)
        while self.calcMean(numberPurchases) <= 2.3:
            self.pullUp(numberPurchases)
        while self.calcMean(numberPurchases) >= 2.7:
            self.pullDown(numberPurchases)

    
    def generateNameAndAge(self):
        stop = False
        gender = randint(0, 1)
        ageMin = randint(18, 29)
        ageMax = randint(66, 87)
        age = randint(ageMin, ageMax)

        while stop == False:
            if gender == 0:
                name = names.get_full_name(gender='female')
            else:
                name = names.get_full_name(gender='male')
            if name not in self.df['fullName']:
                self.df.loc[self.current, 'fullName'] = name
                self.df.loc[self.current, 'gender'] = "female" if gender == 0 else "male"
                self.df.loc[self.current, 'age'] = age
                self.df.loc[self.current, 'address'] = self.fake.address()

                stop = True

def main():
    g = Generator()

    print(g.df)
    g.df.to_csv("./data.csv", index=False, encoding="utf-8-sig", sep=",")

if __name__ == "__main__":
    main()