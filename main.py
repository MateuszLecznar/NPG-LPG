from Cofnij import Cofnij
from Komputer import Komputer
from RestartujGre import ResetujGre
from ustawienia_poczatkowe_3x3 import punkty_X, punkty_Y, kto_wygral, remis
import Ustawienia_planszy_rysunek_okna
import keyboard
import SprawdzPole

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pygame as pg, sys,time
from pygame.locals import*
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
        if(czy_moge==0):
            if(keyboard.is_pressed('b')):
                czy_moge=1

                Cofnij()
                time.sleep(1)
                czyj_ruch = 'X'