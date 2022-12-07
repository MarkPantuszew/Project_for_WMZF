a = 0
while a ==0:
    opcja_1 =input('Wpisz liczbe "1" zeby przejsc do drgan mechanicznych albo liczbe "2" zeby wybrac grdania w ukladzie RLC: ')
    try:
        opcja_1=int(opcja_1)
        if(opcja_1==1 or opcja_1==2):
            a = a + 1
        else:
            print("Nie mozna tego uzyc. Wybierz 1 albo 2")
    except:
        print("Podajes nie liczbe!")
    if opcja_1==1:
            print(4)
        #tu wstawimy drgania mechaniczne
    if opcja_1==2:                                                                 #ewentualnie z else tez mozna przejscie wymysliec
        #a tu RLC
            print(455677777)
            
# import numpy as np
#
#
# # import matplotlib as plt
#
# def drgania_mech():
#     a = float(input('Podaj wartosc amplitudy dla drgan mechanicznych: '))  # amplituda
#     w = float(input('Podaj wartosc czestosci wlasnej dla drgan mechanicznych: '))  # czestosc wlasna
#     f = float(input('Podaj wartosc wspolczynnika oporu ruchu dla drgan mechanicznych: '))  # wsp_op_ruchu
#     m = float(input('Podaj wartosc masy dla drgan mechanicznych: '))  # masa
#     p = float(input('Podaj wartosc fazy poczatkowej dla drgan mechanicznych: '))  # faza_poczatkowa
#     t = 1
#     x = a * (np.exp(-f / (2 * m)) * t) * np.sin((np.sqrt((w ** 2) - ((f / (2 * m)) ** 2)) * t) + p)
#     return x
# a, w, f, m, p, t, x = drgania_mech()
# print(x)





import numpy as np
def drgania_mech(a, w, f, m, p):
    a = float(input('Podaj wartosc amplitudy dla drgan mechanicznych: '))  # amplituda
    w = float(input('Podaj wartosc czestosci wlasnej dla drgan mechanicznych: '))  # czestosc wlasna
    f = float(input('Podaj wartosc wspolczynnika oporu ruchu dla drgan mechanicznych: '))  # wsp_op_ruchu
    m = float(input('Podaj wartosc masy dla drgan mechanicznych: '))  # masa
    p = float(input('Podaj wartosc amplitudy dla drgan mechanicznych: '))  # faza_poczatkowa
    t = np.linespace(0, 1000, 10000000)
    x = a * (np.exp(-(f/2m) * t)) * np.sin((np.sqrt(w * 2 - (f/2m) * 2)) * t + p))
    plt.plot(t, x, color='r', label='dr.mech')
    plt.show()
    return drgania_mech(a,w,f,m,p)
# Kamil - próba środa
