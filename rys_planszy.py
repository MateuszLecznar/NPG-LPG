# !/usr/bin/python
# -*- coding: utf-8 -*-


import pygame as pg, sys, time
from pygame.locals import *


def rysuj_plansze():
    ekran.blit(plansza_startowa, (0, 0))
    pg.display.update()
    time.sleep(1)
    ekran.fill(bialy)

    pg.draw.line(ekran, czarny, (szerokosc / 3, 0), (szerokosc / 3, wysokosc), 7)
    pg.draw.line(ekran, czarny, (szerokosc / 3 * 2, 0), (szerokosc / 3 * 2, wysokosc), 7)

    pg.draw.line(ekran, czarny, (0, wysokosc / 3), (szerokosc, wysokosc / 3), 7)
    pg.draw.line(ekran, czarny, (0, wysokosc / 3 * 2), (szerokosc, wysokosc / 3 * 2), 7)

    pg.display.update()


rysuj_plansze()
