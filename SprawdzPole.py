def SprawdzPole():
    #zczytujemy pole myszki
    x,y =pg.mouse.get_pos()

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
    print(Kolumna,Wiersz)

    if (Wiersz and Kolumna and plansza[Wiersz-1][Kolumna-1]is None):
            global czyj_ruch

            NarysujSymbol(Wiersz , Kolumna)
            SprawdzWygrana()