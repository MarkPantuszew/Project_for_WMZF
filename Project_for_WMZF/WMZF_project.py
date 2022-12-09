import numpy as np
import matplotlib.pyplot as plt

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
        print("To nie jest liczba. Wprowadź 1 lub 2.")
    if opcja_1 == 1:
        b = 0
        while b == 0:
            wybor = int(input('Wpisz 1, aby otrzymać wartość wychylenia w konkretnej chwili czasu lub 2, aby wyświetlić wykres drgań w funkcji czasu:'))
            match wybor:
                case 1:
                    t = float(input('Podaj moment ruchu:[s]'))
                    b = 1
                    def drgania_mech():
                        a = float(input('Podaj wartość amplitudy drgań mechanicznych [m]:'))
                        w = float(input('Podaj wartość czestości własnej drgań [1/s]:'))
                        f = float(input('Podaj wartość współczynnika oporów ruchu [kg/s]:'))
                        m = float(input('Podaj masę drgającego ciała [kg]:'))
                        p = float(input('Podaj fazę poczatkową ruchu [rad]:'))
                        x = a * (np.exp(-f / (2 * m)) * t) * np.sin((np.sqrt((w ** 2) - ((f / (2 * m)) ** 2)) * t) + p)
                        return x
                    x = drgania_mech()
                    print('Wartość wychylania dla chwili czasu t=',t,'s wyniosła ',x)
                case 2:
                    a = float(input('Podaj wartość amplitudy drgań mechanicznych [m]:'))
                    w = float(input('Podaj wartość czestości własnej drgań [1/s]:'))
                    f = float(input('Podaj wartość współczynnika oporów ruchu [kg/s]:'))
                    m = float(input('Podaj masę drgającego ciała [kg]:'))
                    p = float(input('Podaj fazę poczatkową ruchu [rad]:'))
                    t = np.linspace(0, 1000, 100)
                    x = a * (np.exp(-f / (2 * m)) * t) * np.sin((np.sqrt((w ** 2) - ((f / (2 * m)) ** 2)) * t) + p)
                    plt.plot(x,t,color='r',label='Drgania mechaniczne: x(t)')
                    plt.show()
                    b = 1
                case _:
                    print("Nie można tego użyć. Wybierz 1 lub 2.")
        if opcja_1==2:
        #a tu RLC
            print(455677777)

