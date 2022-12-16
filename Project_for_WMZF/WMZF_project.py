import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def wartosc():
    x = a * (np.exp(-f / (2 * m) * t)) * np.sin((np.sqrt(abs((w * 2) - ((f / (2 * m)) * 2))) * t) + p)
    return x
def wykres():
    t_data = []
    x_data = []
    fig, ax = plt.subplots()
    ax.set_xlim(0, 60)
    ax.set_ylim(-(a + 1), (a + 1))
    line, = ax.plot(0, 0)
    plt.title(title)
    plt.xlabel('Czas - t[s]')
    plt.ylabel(ylabel)
    plt.grid()
    def animation_frame(t):
        t_data.append(t)
        x_data.append(a * (np.exp((-f / (2 * m)) * t)) * np.sin((np.sqrt(abs((w * 2) - ((f / (2 * m)) * 2))) * t) + p))
        line.set_xdata(t_data)
        line.set_ydata(x_data)
        return line,
    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 60, 0.1), interval=1, blit=True,
                              repeat=False)
    if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
        return plt.show()
    else:
        return print('Brak drgań dla wprowadzonych parametrów, zachodzi zanik eksponencjalny')
#WYBÓR: RODZAJ DRGAŃ
a = 0
while a == 0:
    opcja_1 = input('\nWybierz rodzaj drgań;\nWpisz 1 dla drgań mechanicznych lub 2 dla drgań elektrycznych:\n')
    try:
        opcja_1 = int(opcja_1)
        if (opcja_1 == 1 or opcja_1 == 2):
            a = a + 1
        else:
            print("Nie można tego użyć. Wybierz 1 lub 2.")
    except:
        print("To nie jest typ integer. Wprowadź 1 lub 2.")
#WYBÓR: MECHANICZNE - WARTOŚĆ LUB WYKRES
    if opcja_1 == 1:
        a = float(input('Podaj wartość \'A\' amplitudy drgań mechanicznych [m]:'))
        w = float(input('Podaj wartość \'omega\' częstości własnej drgań [rad/s]:'))
        f = float(input('Podaj wartość \'f\' współczynnika oporów ruchu [kg/s]:'))
        m = float(input('Podaj masę \'m\' drgającego ciała [kg]:'))
        p = float(input('Podaj fazę \'phi\' poczatkową ruchu [rad]:'))
        b = 0
        while b == 0:
            wybor = int(input('Wpisz 1, aby otrzymać wartość wychylenia w konkretnej chwili czasu lub 2, aby wyświetlić wykres drgań w funkcji czasu:'))
            match wybor:
#MECH-WARTOŚĆ
                case 1:
                    t = float(input('Podaj moment ruchu:[s]'))
                    b = 1
                    if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
                        print('Wartość wychylenia w  chwili czasu t=', t, 's wyniosła ', wartosc())
                    else:
                        print('Brak drgań dla wprowadzonych parametrów. Zachodzi zanik eksponencjalny')
#MECH-WYKRES
                case 2:
                    b=1
                    title = 'Drgania mechaniczne: x(t)'
                    ylabel = 'Wychylenie - x[m]'
                    wykres()
                case _:
                    print("Nie można tego użyć. Wybierz 1 lub 2.")
#WYBÓR: ELEKTRYCZNE - WARTOŚĆ LUB WYKRES
    if opcja_1==2:
        a = float(input('Podaj wartość \'Q\' amplitudy ładunku [C]:'))
        w = float(input('Podaj wartość \'omega\' częstości własnej drgań [rad/s]:'))
        f = float(input('Podaj wartość \'R\' rezystancji opornika w układzie [Ohm]:'))
        m = float(input('Podaj indukcyjność cewki \'L\' w ukłdzie [H]:'))
        p = float(input('Podaj fazę poczatkową ruchu \'phi\' [rad]:'))
        b = 0
        while b == 0:
            wybor = int(input(
                'Wpisz 1, aby otrzymać wartość ładunku w układzie w konkretnej chwili czasu lub 2, aby wyświetlić wykres drgań w funkcji czasu:'))
            match wybor:
#EL-WARTOŚĆ
                case 1:
                    t = float(input('Podaj moment drgań:[s]'))
                    b = 1
                    if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
                        print('Wartość ładunku w układzie dla chwili czasu t=', t, 's wyniosła ', wartosc())
                    else:
                        print('Brak drgań dla wprowadzonych parametrów. Zachodzi zanik eksponencjalny')
#EL-WYKRES
                case 2:
                    b = 1
                    title = 'Drgania elektryczne: q(t)'
                    ylabel = 'Wartość ładunku - q[C]'
                    wykres()
                case _:
                    print("Nie można tego użyć. Wybierz 1 lub 2.")