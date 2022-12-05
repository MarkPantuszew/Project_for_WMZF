import numpy as np
def drgania_mech(a, w, f, m, p):
    a = float(input('Podaj wartosc amplitudy dla drgan mechanicznych: '))  # amplituda
    w = float(input('Podaj wartosc czestosci wlasnej dla drgan mechanicznych: '))  # czestosc wlasna
    f = float(input('Podaj wartosc wspolczynnika oporu ruchu dla drgan mechanicznych: '))  # wsp_op_ruchu
    m = float(input('Podaj wartosc masy dla drgan mechanicznych: '))  # masa
    p = float(input('Podaj wartosc amplitudy dla drgan mechanicznych: '))  # faza_poczatkowa
    t = np.linespace(0, 1000, 10000000)
    x = a * (np.exp(-(f/2m) * t)) * np.sin((np.sqrt(w ** 2 - (f/2m) ** 2)) * t + p))
    plt.plot(t, x, color='r', label='dr.mech')
    plt.show()
    return drgania_mech(a,w,f,m,p)
#