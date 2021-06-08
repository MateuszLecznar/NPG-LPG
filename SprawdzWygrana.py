#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
import RysujDodatkoweInformacje
from pygame.locals import*
def SprawdzWygrana():
    global plansza,kto_wygral, remis

    #sprawdzanie wygranej w poziomie

    for Wiersz in range (0,3):
        if ((plansza[Wiersz][0] == plansza[Wiersz][1] == plansza[Wiersz][2]) and (plansza[Wiersz][0] is not None)):
            kto_wygral= plansza[Wiersz][0]
            pg.draw.line(ekran,(128,0,0),(0,(Wiersz + 1)*wysokosc/3 -wysokosc /6 ),(szerokosc,(Wiersz +1 )*wysokosc/3-wysokosc/6),4)
            break
    # Sprawdzanie w pionie
    for Kolumna in range(0, 3):
        if ((plansza[0][Kolumna] == plansza[1][Kolumna] == plansza[2][Kolumna]) and (plansza[0][Kolumna] is not None)):
            kto_wygral= plansza[0][Kolumna]
            pg.draw.line(ekran,(128,0,0),((Kolumna + 1)*szerokosc/3 -szerokosc /6,0 ),((Kolumna +1 )*szerokosc/3-szerokosc/6,szerokosc),4)
            break

    #Sprawdzanie na ukos
    if (plansza[0][0]==plansza[1][1]==plansza[2][2]and (plansza[0][0] is not None)):
        kto_wygral = plansza [0][0]
        pg.draw.line(ekran,(128,0,0),(50,50),(350,350),4)
    if (plansza[0][2] == plansza[1][1] == plansza[2][0] and (plansza[0][2] is not None)):
        kto_wygral = plansza[0][2]
        pg.draw.line(ekran, (128, 0, 0), (350, 50), (50, 350), 4)
    #jezeli nikt nie wygral
    if (all ([all(Wiersz) for Wiersz in plansza]) and kto_wygral is None):
            remis=True
    RysujDodatkoweInformacje()