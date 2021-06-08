#!/usr/bin/python
# -*- coding: utf-8 -*-
import SprawdzPole

from Ustawienia_planszy_rysunek_okna import szerokosc, wysokosc



import random
def Komputer():
    w = random.uniform(0,szerokosc-1)
    k = random.uniform(0,wysokosc-1)

    SprawdzPole(w,k)