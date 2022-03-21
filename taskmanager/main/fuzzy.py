from django.http import HttpResponse
from matplotlib import pylab as plt
from matplotlib import colors
import numpy as np
import math


class Fuzzy:

    def __init__(self, inp_speed, inp_price, inp_family, inp_beauty, inp_comfort, inp_salon):
        self.inp_speed = inp_speed
        self.inp_price = inp_price
        self.inp_family = inp_family
        self.inp_beauty = inp_beauty
        self.inp_comfort = inp_comfort
        self.inp_salon = inp_salon

    def Fclass(self, Ux, Func=lambda x, Ux: np.array([1] * len(Ux)), method='base'):
        massiv = np.array([Func(el, Ux) for el in Ux])
        if method == 'base':
            masmu = np.min(massiv / np.max([list(zip(el, massiv.T[nom])) for nom, el in enumerate(massiv)], axis=2),
                           axis=1)
        elif method == 'alternative':
            masmu = np.min(massiv / massiv.T, axis=1)
        else:
            masmu = np.array([0] * len(Ux))
            print('Неизвестный метод', method)
        return dict(np.array([Ux, masmu]).T)

    def calc(self):
        rules = []

        price = str(self.inp_price)
        speed = str(self.inp_speed)
        family = str(self.inp_family)
        beauty = str(self.inp_beauty)
        comfort = str(self.inp_comfort)
        salon = str(self.inp_salon)

        if speed == 'Не важно':
            self.speed1 = 0.1
            self.speed2 = 0.6
            self.speed3 = 0.9
            self.speed4 = 0.3
            self.speed5 = 0.7
            self.speed6 = 0.5
            self.speed7 = 1.
            self.speed8 = 0.9
            self.speed9 = 0.2
            self.speed10 = 0.4
            self.speed11 = 0.6
            self.speed12 = 0.3

            rules.append(1)

        if speed == 'Важно':
            self.speed1 = 0.9
            self.speed2 = 0.3
            self.speed3 = 0.1
            self.speed4 = 0.8
            self.speed5 = 0.2
            self.speed6 = 0.7
            self.speed7 = 0.
            self.speed8 = 0.1
            self.speed9 = 0.8
            self.speed10 = 0.4
            self.speed11 = 0.3
            self.speed12 = 0.7
            rules.append(1)

        if speed == 'Без разницы':
            self.speed1 = 0.4
            self.speed2 = 0.9
            self.speed3 = 0.3
            self.speed4 = 1.
            self.speed5 = 0.6
            self.speed6 = 0.2
            self.speed7 = 0.5
            self.speed8 = 0.6
            self.speed9 = 0.4
            self.speed10 = 0.3
            self.speed11 = 0.1
            self.speed12 = 0.9
            rules.append(1)

        if price == 'Важна':
            self.price1 = 0.8
            self.price2 = 1.
            self.price3 = 0.2
            self.price4 = 0.1
            self.price5 = 0.3
            self.price6 = 0.9
            self.price7 = 0.7
            self.price8 = 0.4
            self.price9 = 0.6
            self.price10 = 1.
            self.price11 = 0.5
            self.price12 = 0.4
            rules.append(1)

        if price == 'Не важна':
            self.price1 = 0.3
            self.price2 = 0.1
            self.price3 = 0.9
            self.price4 = 0.7
            self.price5 = 0.6
            self.price6 = 0.1
            self.price7 = 0.
            self.price8 = 0.8
            self.price9 = 0.3
            self.price10 = 0.1
            self.price11 = 0.3
            self.price12 = 0.8
            rules.append(1)

        if price == 'Без разницы':
            self.price1 = 0.3
            self.price2 = 0.4
            self.price3 = 0.5
            self.price4 = 0.4
            self.price5 = 0.8
            self.price6 = 0.5
            self.price7 = 0.3
            self.price8 = 0.6
            self.price9 = 0.2
            self.price10 = 0.5
            self.price11 = 0.8
            self.price12 = 0.1
            rules.append(1)

        if family == 'Без разницы':
            self.family1 = 0.4
            self.family2 = 0.7
            self.family3 = 0.8
            self.family4 = 0.1
            self.family5 = 0.9
            self.family6 = 0.4
            self.family7 = 0.7
            self.family8 = 0.2
            self.family9 = 0.8
            self.family10 = 0.5
            self.family11 = 1.
            self.family12 = 0.6
            rules.append(1)

        if family == 'Важно':
            self.family1 = 0.9
            self.family2 = 0.3
            self.family3 = 0.5
            self.family4 = 0.9
            self.family5 = 0.1
            self.family6 = 0.6
            self.family7 = 0.3
            self.family8 = 0.8
            self.family9 = 0.2
            self.family10 = 0.7
            self.family11 = 0.
            self.family12 = 0.3
            rules.append(1)

        if family == 'Не важно':
            self.family1 = 0.1
            self.family2 = 1.
            self.family3 = 0.3
            self.family4 = 0.5
            self.family5 = 0.7
            self.family6 = 0.8
            self.family7 = 0.4
            self.family8 = 0.6
            self.family9 = 0.9
            self.family10 = 0.3
            self.family11 = 0.5
            self.family12 = 0.7
            rules.append(1)

        if beauty == 'Без разницы':
            self.beauty1 = 0.4
            self.beauty2 = 0.7
            self.beauty3 = 0.8
            self.beauty4 = 0.6
            self.beauty5 = 0.5
            self.beauty6 = 0.7
            self.beauty7 = 0.3
            self.beauty8 = 0.5
            self.beauty9 = 0.2
            self.beauty10 = 0.8
            self.beauty11 = 0.3
            self.beauty12 = 1.
            rules.append(1)

        if beauty == 'Важно':
            self.beauty1 = 0.9
            self.beauty2 = 0.3
            self.beauty3 = 0.5
            self.beauty4 = 0.9
            self.beauty5 = 0.2
            self.beauty6 = 0.4
            self.beauty7 = 1.
            self.beauty8 = 0.3
            self.beauty9 = 0.9
            self.beauty10 = 0.4
            self.beauty11 = 0.8
            self.beauty12 = 0.5
            rules.append(1)

        if beauty == 'Не важно':
            self.beauty1 = 0.1
            self.beauty2 = 1.
            self.beauty3 = 0.3
            self.beauty4 = 0.2
            self.beauty5 = 0.8
            self.beauty6 = 0.6
            self.beauty7 = 0.
            self.beauty8 = 0.7
            self.beauty9 = 0.5
            self.beauty10 = 0.8
            self.beauty11 = 0.3
            self.beauty12 = 0.9
            rules.append(1)

        if comfort == 'Без разницы':
            self.comfort1 = 0.4
            self.comfort2 = 0.7
            self.comfort3 = 0.8
            self.comfort4 = 0.5
            self.comfort5 = 0.4
            self.comfort6 = 0.9
            self.comfort7 = 0.3
            self.comfort8 = 0.7
            self.comfort9 = 0.1
            self.comfort10 = 0.6
            self.comfort11 = 0.3
            self.comfort12 = 0.7
            rules.append(1)

        if comfort == 'Важно':
            self.comfort1 = 0.9
            self.comfort2 = 0.3
            self.comfort3 = 0.5
            self.comfort4 = 0.9
            self.comfort5 = 0.2
            self.comfort6 = 0.5
            self.comfort7 = 0.7
            self.comfort8 = 0.1
            self.comfort9 = 1.
            self.comfort10 = 0.7
            self.comfort11 = 0.4
            self.comfort12 = 0.5
            rules.append(1)

        if comfort == 'Не важно':
            self.comfort1 = 0.1
            self.comfort2 = 1.
            self.comfort3 = 0.3
            self.comfort4 = 0.1
            self.comfort5 = 0.8
            self.comfort6 = 0.7
            self.comfort7 = 0.4
            self.comfort8 = 0.9
            self.comfort9 = 0.
            self.comfort10 = 0.3
            self.comfort11 = 0.8
            self.comfort12 = 0.7
            rules.append(1)

        if salon == 'Без разницы':
            self.salon1 = 0.4
            self.salon2 = 0.7
            self.salon3 = 0.8
            self.salon4 = 0.1
            self.salon5 = 0.5
            self.salon6 = 0.8
            self.salon7 = 0.4
            self.salon8 = 0.3
            self.salon9 = 0.
            self.salon10 = 0.9
            self.salon11 = 1.
            self.salon12 = 0.2
            rules.append(1)

        if salon == 'Важен':
            self.salon1 = 0.9
            self.salon2 = 0.3
            self.salon3 = 0.5
            self.salon4 = 0.6
            self.salon5 = 0.9
            self.salon6 = 0.2
            self.salon7 = 0.1
            self.salon8 = 0.8
            self.salon9 = 1.
            self.salon10 = 0.4
            self.salon11 = 0.5
            self.salon12 = 0.6
            rules.append(1)

        if salon == 'Не важен':
            self.salon1 = 0.1
            self.salon2 = 1.
            self.salon3 = 0.3
            self.salon4 = 0.2
            self.salon5 = 0.1
            self.salon6 = 0.8
            self.salon7 = 0.9
            self.salon8 = 0.4
            self.salon9 = 0.
            self.salon10 = 0.8
            self.salon11 = 0.3
            self.salon12 = 0.2
            rules.append(1)

        print(rules)

        mclass = np.array(
            [[self.price1, self.speed1, self.family1, self.beauty1, self.comfort1, self.salon1],
             [self.price2, self.speed2, self.family2, self.beauty2, self.comfort2, self.salon2],
             [self.price3, self.speed3, self.family3, self.beauty3, self.comfort3, self.salon3],
             [self.price4, self.speed4, self.family4, self.beauty4, self.comfort4, self.salon4],
             [self.price5, self.speed5, self.family5, self.beauty5, self.comfort5, self.salon5],
             [self.price6, self.speed6, self.family6, self.beauty6, self.comfort6, self.salon6],
             [self.price7, self.speed7, self.family7, self.beauty7, self.comfort7, self.salon7],
             [self.price8, self.speed8, self.family8, self.beauty8, self.comfort8, self.salon8],
             [self.price9, self.speed9, self.family9, self.beauty9, self.comfort9, self.salon9],
             [self.price10, self.speed10, self.family10, self.beauty10, self.comfort10, self.salon10],
             [self.price11, self.speed11, self.family11, self.beauty11, self.comfort11, self.salon11],
             [self.price12, self.speed12, self.family12, self.beauty12, self.comfort12, self.salon12]])
        Uclass = ['Lada_Vesta', 'Toyota_RAV4', 'Hyonday_Creta', 'Mitsubishi_Outlander',
                  'Toyota_Land_Cruiser_Prado', 'Skoda_Kodiaq', 'Mazda_CX-5', 'Kia_Rio',
                  'Haval_F7', 'Nissan_Qashqai', 'Kia_Sportage', 'Ford_Focus']

        dclass = dict()
        for nom, el in enumerate(Uclass):
            dclass[nom] = mclass[nom]
        dclass

        res1 = self.Fclass(range(len(rules)), Func=lambda x, Ux: dclass[x])
        print(res1)

        for el in res1:
            print('{} - {}'.format(Uclass[int(el)], res1[el]))

        out = format(Uclass[int(list(res1.keys())[np.argmax(list(res1.values()))])])

        img = 'img/' + out + ".jpg"

        total = {}

        total.update({out: img})

        return total
