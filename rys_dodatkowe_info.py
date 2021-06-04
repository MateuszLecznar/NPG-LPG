#!/usr/bin/python
# -*- coding: utf-8 -*-

def RysujDodatkoweInformacje():
    global remis
    # warunek ktory wygral

    if kto_wygral is None:
        tresc_wiadomosci = "twoja tura " + czyj_ruch.upper()
    else:
        tresc_wiadomosci = kto_wygral.upper() + " wygrales"
    if remis:
        tresc_wiadomosci = "remis!"

    czcionka = pg.font.Font(None, 30)
    Wiadomosc = czcionka.render(tresc_wiadomosci, True, bialy)

    Punkty = "X: " + str(punkty_X) + "  <--->  O:" + str(punkty_Y)
    punkty_wiadomosc = czcionka.render(Punkty, True, czarny)

    obramowanie_na_wiadomosc = Wiadomosc.get_rect(center=(szerokosc / 2, 500 - 50))
    obramowanie_na_punkty = punkty_wiadomosc.get_rect(center=(szerokosc / 2, 600 - 50))

    ekran.fill((0, 0, 0), (0, 400, 500, 100))
    ekran.blit(Wiadomosc, obramowanie_na_wiadomosc)
    ekran.blit(punkty_wiadomosc, obramowanie_na_punkty)
    pg.display.update()