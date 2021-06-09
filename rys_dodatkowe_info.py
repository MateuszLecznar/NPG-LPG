#!/usr/bin/python
# -*- coding: utf-8 -*-

def RysujDodatkoweInformacje():
    global remis
    # warunek ktory
    tresc_wiadomosci2 = "Jeśli chcesz cofnąc wciśnij 'b'"

    if kto_wygral is None:
        tresc_wiadomosci = "twoja tura " + czyj_ruch.upper()

    else:
        tresc_wiadomosci = kto_wygral.upper() + " wygrales"
    if remis:
        tresc_wiadomosci = "remis!"

    czcionka = pg.font.Font(None, 30)
    Wiadomosc = czcionka.render(tresc_wiadomosci, True, bialy)
    Wiadomosc2 = czcionka.render(tresc_wiadomosci2, True, bialy)

    Punkty = "X: " + str(punkty_X) + "  <--->  O:" + str(punkty_Y)
    punkty_wiadomosc = czcionka.render(Punkty, True, czarny)

    obramowanie_na_wiadomosc = Wiadomosc.get_rect(center=(szerokosc / 2, 500 - 50))
    obramowanie_na_punkty = punkty_wiadomosc.get_rect(center=(szerokosc / 2, 600 - 50))
    obramowanie_na_wiadomosc2 = Wiadomosc.get_rect(center=(szerokosc / 3, 700 - 50))
    ekran.fill((0, 0, 0), (0, 400, 500, 100))
    ekran.fill((0, 0, 0), (0, 600, 700, 100))
    ekran.blit(Wiadomosc, obramowanie_na_wiadomosc)
    ekran.blit(punkty_wiadomosc, obramowanie_na_punkty)
    ekran.blit(Wiadomosc2, obramowanie_na_wiadomosc2)
    pg.display.update()