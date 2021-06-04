#!/usr/bin/python
# -*- coding: utf-8 -*-

#ustawienia planszy
plansza = [[None] * 3, [None] * 3, [None] * 3]
#okno programu

pg.init()
fps = 30
zegar = pg.time.Clock()
ekran = pg.display.set_mode((szerokosc, wysokosc + 300), 0, 32)
pg.display.set_caption("Kolko i krzyzyk")