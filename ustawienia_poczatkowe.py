#!/usr/bin/python
# -*- coding: utf-8 -*-

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

punkty_X = 0
punkty_Y = 0
powtorka =0
czy_moge=0