import numpy as np
def drgania_mech(a, w, f, m, p):
    a = float(input('Podaj wartosc amplitudy dla drgan mechanicznych: [m]'))  # amplituda
    w = float(input('Podaj wartosc czestosci wlasnej dla drgan mechanicznych: [1/s]'))  # czestosc wlasna
    f = float(input('Podaj wartosc wspolczynnika oporów ruchu: [1/(s*kg)]'))  # wsp_op_ruchu
    m = float(input('Podaj masę drgającego ciała: [kg]'))  # masa
    p = float(input('Podaj fazę początkową dla drgan mechanicznych: [rad]'))  # faza_poczatkowa
    t = np.linespace(0, 1000, 10000000)
    x = a * (np.exp(-(f/2m) * t)) * np.sin((np.sqrt(w ** 2 - (f/2m) ** 2)) * t + p))
    plt.plot(t, x, color='r', label='dr.mech')
    plt.show()
    return()
#