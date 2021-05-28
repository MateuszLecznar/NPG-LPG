import pygame as pg, sys, time
from pygame.locals import*
#ustawienia planszy
plansza = [[None] * 3, [None] * 3, [None] * 3]
#okno programu

szerokosc= 100
wysokosc=100
pg.init()
fps = 30
zegar = pg.time.Clock()
ekran = pg.display.set_mode((szerokosc, wysokosc + 200), 0, 32)
#obrazy do zmiennych
plansza_startowa = pg.image.load('graphics/PlanszaStartowa.png')
obraz_x = pg.image.load('graphics/x.png')
obraz_o = pg.image.load('graphics/o.png')
#ustawienie wymiarów obrazów
plansza_startowa = pg.transform.scale(plansza_startowa, (szerokosc,wysokosc + 200))
obraz_x = pg.transform.scale(obraz_x, (80,80))
obraz_o = pg.transform.scale(obraz_o, (80,80))

