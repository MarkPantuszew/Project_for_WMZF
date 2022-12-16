import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#WYBÓR: RODZAJ DRGAŃ
a = 0
while a == 0:
    opcja_1 = input('Wybierz rodzaj drgań;\nWpisz 1 dla drgań mechanicznych lub 2 dla drgań elektrycznych:\n')
    try:
        opcja_1 = int(opcja_1)
        if (opcja_1 == 1 or opcja_1 == 2):
            a = a + 1
        else:
            print("Nie można tego użyć. Wybierz 1 lub 2.")
    except:
        print("To nie jest typ interger. Wprowadź 1 lub 2.")

#WYBÓR: MECHANICZNE - WARTOŚĆ LUB WYKRES
    if opcja_1 == 1:
        a = float(input('Podaj wartość amplitudy drgań mechanicznych [m]:'))
        w = float(input('Podaj wartość częstości własnej drgań [rad/s]:'))
        f = float(input('Podaj wartość współczynnika oporów ruchu [kg/s]:'))
        m = float(input('Podaj masę drgającego ciała [kg]:'))
        p = float(input('Podaj fazę poczatkową ruchu [rad]:'))
        b = 0
        while b == 0:
            wybor = int(input('Wpisz 1, aby otrzymać wartość wychylenia w konkretnej chwili czasu lub 2, aby wyświetlić wykres drgań w funkcji czasu:'))
            match wybor:
#MECH-WARTOŚĆ
                case 1:
                    t = float(input('Podaj moment ruchu:[s]'))
                    b = 1
                    def mech_wartosc():
                        x = a * (np.exp(-f / (2 * m)) * t) * np.sin((np.sqrt(abs((w ** 2) - ((f / (2 * m)) ** 2))) * t) + p)
                        if ((w ** 2) - ((f / (2 * m)) ** 2)) >= 0:
                            return print('Wartość wychylania dla chwili czasu t=', t, 's wyniosła ', x)
                        else:
                            return print('Brak drgań dla wprowadzonych parametrów. Zachodzi zanik eksponencjalny')
                    mech_wartosc()
#MECH-WYKRES
                case 2:
                    b=1
                    def mech_wykres():
                        t = np.linspace(0, 60, 1)
                        t_data = []
                        x_data = []
                        x = a * (np.exp((-f / (2 * m)) * t)) * np.sin((np.sqrt(abs((w ** 2) - ((f / (2 * m)) ** 2))) * t) + p)
                        fig, ax = plt.subplots()
                        ax.set_xlim(0,60)
                        ax.set_ylim(-(a + 1), (a + 1))
                        line, = ax.plot(0, 0)
                        plt.plot(t, x, color='y')
                        plt.title('Drgania mechaniczne: x(t)')
                        plt.xlabel("Czas - t[s]")
                        plt.ylabel("Wychylenie - x[m]")
                        plt.grid()
                        def animation_frame(t):
                            t_data.append(t)
                            x_data.append(a * (np.exp((-f / (2 * m)) * t)) * np.sin(
                                (np.sqrt(abs((w ** 2) - ((f / (2 * m)) ** 2))) * t) + p))
                            line.set_xdata(t_data)
                            line.set_ydata(x_data)
                            return line,
                        animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0,60, 0.1), interval=1,blit=True, repeat=False)
                        if ((w ** 2) - ((f / (2 * m)) ** 2)) >= 0:
                            return plt.show()
                        else:
                            return print('Brak drgań dla wprowadzonych parametrów, zachodzi zanik eksponencjalny')
                    mech_wykres()
                case _:
                    print("Nie można tego użyć. Wybierz 1 lub 2.")
#WYBÓR: ELEKTRYCZNE - WARTOŚĆ LUB WYKRES
    if opcja_1==2:
        a = float(input('Podaj wartość amplitudy ładunku [C]:'))
        w = float(input('Podaj wartość częstości własnej drgań [1/s]:'))
        r = float(input('Podaj wartość rezystancji opornika w układzie [Ohm]:'))
        l = float(input('Podaj indukcyjność cewki w ukłdzie [H]:'))
        p = float(input('Podaj fazę poczatkową ruchu [rad]:'))
        b = 0
        while b == 0:
            wybor = int(input(
                'Wpisz 1, aby otrzymać wartość ładunku w układzie w konkretnej chwili czasu lub 2, aby wyświetlić wykres drgań w funkcji czasu:'))
            match wybor:
                # EL-WARTOŚĆ
                case 1:
                    t = float(input('Podaj moment drgań:[s]'))
                    b = 1

                    def el_wartosc():
                        x = a * (np.exp(-r / (2 * l)) * t) * np.sin(
                            (np.sqrt(abs((w ** 2) - ((r / (2 * l)) ** 2))) * t) + p)
                        if ((w ** 2) - ((r / (2 * l)) ** 2)) >= 0:
                            return print('Wartość ładunku w układzie dla chwili czasu t=', t, 's wyniosła ', x)
                        else:
                            return print('Brak drgań dla wprowadzonych parametrów. Zachodzi zanik eksponencjalny')
                    el_wartosc()
                # EL-WYKRES
                case 2:
                    b = 1
                    def el_wykres():
                        t = np.linspace(0, 60, 1)
                        t_data = []
                        q_data = []
                        x = a * (np.exp((-r / (2 * l)) * t)) * np.sin((np.sqrt(abs((w ** 2) - ((r / (2 * l)) ** 2))) * t) + p)

                        fig, ax = plt.subplots()
                        ax.set_xlim(0, 60)
                        ax.set_ylim(-(a + 1), (a + 1))
                        line, = ax.plot(0, 0)

                        plt.title('Drgania elektryczne: q(t)')
                        plt.xlabel('Czas - t[s]')
                        plt.ylabel('Wartość łądunku w RLC - q[C]')
                        plt.grid()
                        def animation_frame(t):
                            t_data.append(t)
                            q_data.append(a * (np.exp((-r / (2 * l)) * t)) * np.sin((np.sqrt(abs((w ** 2) - ((r / (2 * l)) ** 2))) * t) + p))
                            line.set_xdata(t_data)
                            line.set_ydata(q_data)
                            return line,
                        animation = FuncAnimation(fig,  func=animation_frame, frames=np.arange(0, 60, 0.1), interval=1,blit=True,repeat=False)
                        if ((w ** 2) - ((r / (2 * l)) ** 2)) >= 0:
                            return plt.show()
                        else:
                            return print('Brak drgań dla wprowadzonych parametrów, zachodzi zanik eksponencjalny')
                    el_wykres()
                case _:
                    print("Nie można tego użyć. Wybierz 1 lub 2.")
