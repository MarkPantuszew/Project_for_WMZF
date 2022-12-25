import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def wartosc():
    x = a * (np.exp(-f / (2 * m) * t)) * np.sin((np.sqrt(abs((w ** 2) - ((f / (2 * m)) ** 2))) * t) + p)
    return x
def zapis():
    zapis_t = repr(t)
    zapis_x = repr(wartosc())
    zapis_drganie = drganie
    zapis_jednostka = jednostka
    plik = open("Drganie w chwili t", "w")
    plik.write(zapis_drganie + "w ostatnio wybranej chwili czasu:\nt = " + zapis_t + " s\nwyniosla:\n" + zapis_x + zapis_jednostka)
    plik.close()
def wykres():
    t_data = []
    x_data = []
    fig, ax = plt.subplots()
    ax.set_xlim(0, 60)
    ax.set_ylim(-(a + 1), (a + 1))
    line, = ax.plot(0, 0)
    plt.title(title)
    plt.xlabel('Czas - t [s]')
    plt.ylabel(ylabel)
    plt.grid()
    def animation_frame(t):
        t_data.append(t)
        x_data.append(a * (np.exp(-f / (2 * m) * t)) * np.sin((np.sqrt(abs((w ** 2) - ((f / (2 * m)) ** 2))) * t) + p))
        line.set_xdata(t_data)
        line.set_ydata(x_data)
        return line,
    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 60, 0.1), interval=1, blit=True, repeat=False)
    if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
        return plt.show()
    else:
        return print('Brak drgan dla wprowadzonych parametrow, zachodzi zanik eksponencjalny')
#WYBÓR: RODZAJ DRGAŃ
a = 0
while a == 0:
    opcja_1 = input('\nWybierz rodzaj drgan;\nWpisz 1 dla drgan mechanicznych lub 2 dla drgan elektrycznych:\n')
    try:
        opcja_1 = int(opcja_1)
        if (opcja_1 == 1 or opcja_1 == 2):
            a = a + 1
        else:
            print("Nie mozna tego uzyc. Wybierz 1 lub 2.")
    except:
        print("To nie jest typ integer. Wprowadz 1 lub 2.")
#WYBÓR: MECHANICZNE - WARTOŚĆ LUB WYKRES
    if opcja_1 == 1:
        print('Drgania mechaniczne:\n x = A * (exp(-f/(2m) * t)) * sin((sqrt(w^2 - ((f/2m)^2)) * t) + p)')
        a = float(input('Podaj wartosc \'A\' amplitudy drgan mechanicznych [m]:'))
        w = float(input('Podaj wartosc \'w\' czestosci wlasnej drgan [rad/s]:'))
        f = float(input('Podaj wartosc \'f\' wspolczynnika oporow ruchu [kg/s]:'))
        m = float(input('Podaj mase \'m\' drgajacego ciala [kg]:'))
        p = float(input('Podaj faze \'p\' poczatkowa ruchu [rad]:'))
        b = 0
        while b == 0:
            wybor = int(input('Wpisz 1, aby otrzymac wartosc wychylenia w konkretnej chwili czasu lub 2, aby wyswietlic wykres drgan w funkcji czasu:'))
            match wybor:
#MECH-WARTOŚĆ
                case 1:
                    t = float(input('Podaj moment ruchu:[s]'))
                    b = 1
                    if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
                        print('Wartosc wychylenia w chwili czasu t =', t, 's wyniosla ', wartosc(), 'm')
                        drganie = 'Wartosc wychylenia '
                        jednostka = ' m'
                        zapis()
                    else:
                        print('Brak drgan dla wprowadzonych parametrow. Zachodzi zanik eksponencjalny')
#MECH-WYKRES
                case 2:
                    b=1
                    title = 'Drgania mechaniczne: x(t)'
                    ylabel = 'Wychylenie - x [m]'
                    wykres()
                case _:
                    print("Nie mozna tego uzyc. Wybierz 1 lub 2.")
#WYBÓR: ELEKTRYCZNE - WARTOŚĆ LUB WYKRES
    if opcja_1==2:
        print('Drgania elektryczne:\n q = Q * (exp(-R/(2L) * t)) * sin((sqrt(w^2 - ((R/2L)^2)) * t) + p)')
        a = float(input('Podaj wartosc \'Q\' amplitudy ladunku [C]:'))
        w = float(input('Podaj wartosc \'omega\' czestosci wlasnej drgan [rad/s]:'))
        f = float(input('Podaj wartosc \'R\' rezystancji opornika w ukladzie [Ohm]:'))
        m = float(input('Podaj indukcyjnosc cewki \'L\' w ukldzie [H]:'))
        p = float(input('Podaj faze poczatkowa ruchu \'phi\' [rad]:'))
        b = 0
        while b == 0:
            wybor = int(input(
                'Wpisz 1, aby otrzymac wartosc ladunku w ukladzie w konkretnej chwili czasu lub 2, aby wyswietlic wykres drgan w funkcji czasu:'))
            match wybor:
#EL-WARTOŚĆ
                case 1:
                    t = float(input('Podaj moment drgan:[s]'))
                    b = 1
                    if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
                        print('Wartosc ladunku w ukladzie w chwili czasu t =', t, 's wyniosla ', wartosc(), 'C')
                        drganie = 'Wartosc ladunku w ukladzie RLC '
                        jednostka = ' C'
                        zapis()
                    else:
                        print('Brak drgan dla wprowadzonych parametrow. Zachodzi zanik eksponencjalny')
#EL-WYKRES
                case 2:
                    b = 1
                    title = 'Drgania elektryczne: q(t)'
                    ylabel = 'Wartosc ladunku - q [C]'
                    wykres()
                case _:
                    print("Nie mozna tego uzyc. Wybierz 1 lub 2.")
