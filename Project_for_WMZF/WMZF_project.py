import numpy as np
import matplotlib as plt
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
        # def drgania_mech():
        #     a = float(input('Podaj wartosc amplitudy dla drgan mechanicznych: '))  # amplituda
        #     w = float(input('Podaj wartosc czestosci wlasnej dla drgan mechanicznych: '))  # czestosc wlasna
        #     f = float(input('Podaj wartosc wspolczynnika oporu ruchu dla drgan mechanicznych: '))  # wsp_op_ruchu
        #     m = float(input('Podaj wartosc masy dla drgan mechanicznych: '))  # masa
        #     p = float(input('Podaj wartosc fazy poczatkowej dla drgan mechanicznych: '))  # faza_poczatkowa
        #     t = 1
        #     x = a * (np.exp(-f / (2 * m)) * t) * np.sin((np.sqrt((w ** 2) - ((f / (2 * m)) ** 2)) * t) + p)
        #     return x
        # x = drgania_mech()#trzeba uzuyc funkcji global
        # print(x)
        print('ty kistiu' )
        b = 0
        while b == 0:
            wybor = int(input('Wpisz liczbe "1" zeby wprowadzic wartosc czasu albo liczbe "2" zeby wartosc czasu ustanowila sie domyslnie: '))
            match wybor:
                case 1:
                    czas=float(input('Podaj wartosc czasu, przeciez tego chciales kurwa: '))#tu nie trzeba obslugiwac wyjatki
                    b=1
                case 2:
                    t=1
                    print(t)
                    b=1
                case _:
                    print("Nie mozna tego uzyc!Wybierz 1 albo 2")






                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
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
