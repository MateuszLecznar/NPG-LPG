#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame.locals import*

from Ustawienia_planszy_rysunek_okna import plansza, ekran, czarny, wysokosc, szerokosc

from NarysujSymbol import ostatni_x, ostatni_o, NarysujSymbol


def Cofnij():
    global czyj_ruch

    plansza[ostatni_x[1]-1][ostatni_x[0]-1]= None

    plansza[ostatni_o[1]-1][ostatni_o[0]-1] = None

    ekran.fill((255, 255, 255),(0,0,400, 400))
    # rysowanie siatki
    pg.draw.line(ekran, czarny, (szerokosc / 3, 0), (szerokosc / 3, wysokosc), 7)
    pg.draw.line(ekran, czarny, (szerokosc / 3 * 2, 0), (szerokosc / 3 * 2, wysokosc), 7)

    pg.draw.line(ekran, czarny, (0, wysokosc / 3), (szerokosc, wysokosc / 3), 7)
    pg.draw.line(ekran, czarny, (0, wysokosc / 3 * 2), (szerokosc, wysokosc / 3 * 2), 7)
    pg.display.update()


    for i in range (1,4):
        for j in range (1,4):


            czyj_ruch=plansza[j-1][i-1]

            NarysujSymbol(j,i)

    pg.display.update()




