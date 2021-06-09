#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame.locals import*

from Ustawienia_planszy_rysunek_okna import ekran, obraz_x
from ustawienia_poczatkowe_3x3 import szerokosc, wysokosc


def NarysujSymbol(Wiersz, Kolumna):
    global plansza, czyj_ruch, ostatni_x , ostatni_o


    if Wiersz == 1:
        pozycjaX = 30
    elif Wiersz == 2:
        pozycjaX = szerokosc/3 + 30
    elif Wiersz == 3:
        pozycjaX = szerokosc/3*2 + 30

    if Kolumna == 1:
        pozycjaY = 30
    elif Kolumna == 2:
        pozycjaY = wysokosc / 3 + 30
    elif Kolumna == 3:
        pozycjaY = wysokosc / 3 * 2 + 30




        #wstawiamy flage ze dane pole zajete juz jest


    plansza[Wiersz-1][Kolumna -1] = czyj_ruch

    #rysujemy symbol

    if (czyj_ruch=="X"):
        ekran.blit(obraz_x,(pozycjaY,pozycjaX))
        ostatni_x = (Kolumna,Wiersz)



        czyj_ruch ="O"

    elif (czyj_ruch == "O"):

        ekran.blit(obraz_o,(pozycjaY,pozycjaX))
        ostatni_o=(Kolumna,Wiersz)

        czyj_ruch="X"
    pg.display.update()
