#!/usr/bin/python
# -*- coding: utf-8 -*-

#obrazy do zmiennych

plansza_startowa = pg.image.load('graphics/PlanszaStartowa.png')
obraz_x = pg.image.load('graphics/x.png')
obraz_o = pg.image.load('graphics/o.png')
#ustawienie wymiarów obrazów
plansza_startowa = pg.transform.scale(plansza_startowa, (szerokosc,wysokosc + 300))
obraz_x = pg.transform.scale(obraz_x, (80,80))
obraz_o = pg.transform.scale(obraz_o, (80,80))
r = open('wynik.txt', "r")

punkty_X = int(r.readline())
punkty_Y = int(r.readline())
r.close()