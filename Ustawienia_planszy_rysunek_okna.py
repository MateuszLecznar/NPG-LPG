
import random
import keyboard
import pygame as pg, sys, time
from pygame.locals import *
czyj_ruch = "X"
kto_wygral = None
remis = False
szerokosc = 400
wysokosc = 400

bialy = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (255, 0, 0)


powtorka =0
czy_moge=0

#ustawienia planszy
plansza = [[None] * 3, [None] * 3, [None] * 3]
#okno programu

pg.init()
fps = 30
zegar = pg.time.Clock()
ekran = pg.display.set_mode((szerokosc, wysokosc + 300), 0, 32)
pg.display.set_caption("Kolko i krzyzyk")

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