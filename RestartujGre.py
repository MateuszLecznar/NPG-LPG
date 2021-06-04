#!/usr/bin/python
# -*- coding: utf-8 -*-

def ResetujGre():
    global plansza, kto_wygral,czyj_ruch,remis,punkty_Y,punkty_X
    time.sleep(3)
    czyj_ruch="X"
    remis = False

    if kto_wygral == "X":
        punkty_X += 1
    elif kto_wygral == "O":
        punkty_Y += 1

    kto_wygral =None
    plansza=[[None]*3,[None]*3,[None]*3]
    ekran.fill(bialy)
    RysujPlansze()
RysujPlansze()