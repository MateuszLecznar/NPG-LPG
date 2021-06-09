import random
import keyboard
import pygame as pg, sys, time
import pygame.key
from pygame.locals import *
czyj_ruch = "X"
kto_wygral = None
remis = False
szerokosc = 400
wysokosc = 400
delta=0.0
bialy = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (255, 0, 0)

punkty_X = 0
punkty_Y = 0
powtorka =0
czy_moge = 0

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

def RysujPlansze():
    ekran.blit(plansza_startowa,(0,0))
    pg.display.update()
    time.sleep(1)
    ekran.fill(bialy)
    #rysowanie siatki
    pg.draw.line(ekran,czarny,(szerokosc/3,0),(szerokosc/3,wysokosc), 7)
    pg.draw.line(ekran, czarny, (szerokosc / 3*2, 0), (szerokosc / 3*2, wysokosc), 7)

    pg.draw.line(ekran,czarny,(0,wysokosc/3),(szerokosc,wysokosc/3),7)
    pg.draw.line(ekran, czarny, (0, wysokosc / 3*2), (szerokosc, wysokosc / 3*2), 7)
    pg.display.update()
    RysujDodatkoweInformacje()

def RysujDodatkoweInformacje():
    
    global remis,czas,delta
    #warunek ktory
    tresc_wiadomosci2 = "Jeśli chcesz cofnąc wciśnij 'b'"

    if kto_wygral is None:
        tresc_wiadomosci = "twoja tura "+czyj_ruch.upper()


    else:
        tresc_wiadomosci = kto_wygral.upper()+ " wygrales"
    if remis:
        tresc_wiadomosci="remis!"


    czcionka = pg.font.Font(None,30)
    Wiadomosc = czcionka.render(tresc_wiadomosci,True,bialy)
    Wiadomosc2 = czcionka.render(tresc_wiadomosci2, True, bialy)



    Punkty = "X: "+ str(punkty_X) + "  <--->  O:" + str(punkty_Y)
    punkty_wiadomosc= czcionka.render(Punkty,True,czarny)

    obramowanie_na_wiadomosc = Wiadomosc.get_rect(center = (szerokosc/2,500-50))
    obramowanie_na_punkty = punkty_wiadomosc.get_rect(center=(szerokosc / 2,600-50))
    obramowanie_na_wiadomosc2 = Wiadomosc2.get_rect(center=(szerokosc / 2, 700 - 50))

    ekran.fill((0,0,0),(0,400,500,100))
    ekran.fill((0, 0, 0), (0, 600, 700, 100))

    ekran.blit(Wiadomosc,obramowanie_na_wiadomosc)
    ekran.blit(punkty_wiadomosc,obramowanie_na_punkty)
    ekran.blit(Wiadomosc2 ,obramowanie_na_wiadomosc2)

    pg.display.update()


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

def NarysujSymbol(Wiersz, Kolumna):
    global plansza, czyj_ruch, ostatni_x , ostatni_o


    if Wiersz == 1:
        pozycjaX = 30
    elif Wiersz == 2:
        pozycjaX = szerokosc/3 + 30
    elif Wiersz == 3:
        pozycjaX = szerokosc/3*2 + 30

    if Kolumna == 1:
        pozycjaY = 30
    elif Kolumna == 2:
        pozycjaY = wysokosc / 3 + 30
    elif Kolumna == 3:
        pozycjaY = wysokosc / 3 * 2 + 30




        #wstawiamy flage ze dane pole zajete juz jest


    plansza[Wiersz-1][Kolumna -1] = czyj_ruch

    #rysujemy symbol

    if (czyj_ruch=="X"):
        ekran.blit(obraz_x,(pozycjaY,pozycjaX))
        ostatni_x = (Kolumna,Wiersz)



        czyj_ruch ="O"

    elif (czyj_ruch == "O"):

        ekran.blit(obraz_o,(pozycjaY,pozycjaX))
        ostatni_o=(Kolumna,Wiersz)

        czyj_ruch="X"
    pg.display.update()



def SprawdzPole(x,y):
    #zczytujemy pole myszki


    #współrzedna x

    if(x< szerokosc/3):
        Kolumna =1
    elif(x<szerokosc/3 *2):
        Kolumna = 2
    elif(x<szerokosc):
        Kolumna = 3
    else:
        Kolumna= None
    #wspolrzedna y
    if (y < wysokosc / 3):
        Wiersz = 1
    elif (y < wysokosc / 3 * 2):
        Wiersz = 2
    elif (y < wysokosc):
        Wiersz = 3
    else:
        Wiersz = None


    if (Wiersz and Kolumna and plansza[Wiersz-1][Kolumna-1]is None):
            global czyj_ruch

            NarysujSymbol(Wiersz , Kolumna)
            SprawdzWygrana()
    elif (Wiersz and Kolumna and plansza[Wiersz-1][Kolumna-1] and czyj_ruch=="O"):

        Komputer()



def Komputer():
    w = random.uniform(0,szerokosc-1)
    k = random.uniform(0,wysokosc-1)

    SprawdzPole(w,k)
def Cofnij():
    global czyj_ruch

    plansza[ostatni_x[1]-1][ostatni_x[0]-1]= None

    plansza[ostatni_o[1]-1][ostatni_o[0]-1] = None

    ekran.fill((255, 255, 255),(0,0,400, 400))
    # rysowanie siatki
    pg.draw.line(ekran, czarny, (szerokosc / 3, 0), (szerokosc / 3, wysokosc), 7)
    pg.draw.line(ekran, czarny, (szerokosc / 3 * 2, 0), (szerokosc / 3 * 2, wysokosc), 7)

    pg.draw.line(ekran, czarny, (0, wysokosc / 3), (szerokosc, wysokosc / 3), 7)
    pg.draw.line(ekran, czarny, (0, wysokosc / 3 * 2), (szerokosc, wysokosc / 3 * 2), 7)
    pg.display.update()


    for i in range (1,4):
        for j in range (1,4):


            czyj_ruch=plansza[j-1][i-1]

            NarysujSymbol(j,i)

    pg.display.update()






def ResetujGre():
    global plansza, kto_wygral,czyj_ruch,remis,punkty_Y,punkty_X
    time.sleep(3)
    czyj_ruch="X"
    remis = False
    c=0

    if kto_wygral == "X":
        punkty_X += 1
    elif kto_wygral == "O":
        punkty_Y += 1

    kto_wygral =None
    plansza=[[None]*3,[None]*3,[None]*3]
    ekran.fill(bialy)
    RysujPlansze()
RysujPlansze()
while(True):

    for zdarzenie in pg.event.get():

        if zdarzenie.type == QUIT:
            f = open('wynik.txt',"w")
            f.write(str(punkty_X)+'\n'+str(punkty_Y))
            f.close()
            pg.quit()
            sys.exit()
        elif(czyj_ruch=="X"):

            if zdarzenie.type == MOUSEBUTTONDOWN:

                if zdarzenie.button == 1:
                    x, y = pg.mouse.get_pos()
                    SprawdzPole(x,y)
                    czy_moge=0

        elif(czyj_ruch=="O"):
            Komputer()
        if (kto_wygral or remis):
            ResetujGre()
        if (keyboard.is_pressed('b')):
            if(czy_moge == 0):

                czy_moge=1

                Cofnij()
                time.sleep(1)
                czyj_ruch = 'X'





pg.display.update()
zegar.tick(fps)




