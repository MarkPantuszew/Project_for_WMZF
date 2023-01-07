import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import *
root = Tk()
#FUNKCJE
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
        return Label(root, text='Brak drgan dla wprowadzonych parametrow! Zachodzi zanik eksponencjalny.').pack()

def mech():
    global title
    title = 'Drgania mechaniczne: x(t)'
    global ylabel
    ylabel = 'Wychylenie - x [m]'
    global jednostka
    jednostka = 'm'
    l_wzor = Label(root, text='x = A * (exp(-f/(2m) * t)) * sin((sqrt(w^2 - ((f/2m)^2)) * t) + p)')
    global amplituda
    amplituda = Entry(root, width=15)
    l_amplituda = Label(root, text='Podaj wartosc \'A\' amplitudy drgan mechanicznych [m]:')
    global omega
    omega = Entry(root, width=15)
    l_omega = Label(root, text='Podaj wartosc \'w\' czestosci wlasnej drgan [rad/s]:')
    global wsplop
    wsplop = Entry(root, width=15)
    l_wsplop = Label(root, text='Podaj wartosc \'f\' wspolczynnika oporow ruchu [kg/s]:')
    global masa
    masa = Entry(root, width=15)
    l_masa = Label(root, text='Podaj mase \'m\' drgajacego ciala [kg]:')
    global faza
    faza = Entry(root, width=15)
    l_faza = Label(root, text='Podaj faze \'p\' poczatkowa ruchu [rad]:')
    l_wzor.pack()
    l_amplituda.pack()
    amplituda.pack()
    l_omega.pack()
    omega.pack()
    l_wsplop.pack()
    wsplop.pack()
    l_masa.pack()
    masa.pack()
    l_faza.pack()
    faza.pack()

def el():
    global title
    title = 'Drgania elektryczne: q(t)'
    global ylabel
    ylabel = 'Wartosc ladunku - q [C]'
    global jednostka
    jednostka = 'C'
    l_wzor = Label(root, text='q = Q * (exp(-R/(2L) * t)) * sin((sqrt(w^2 - ((R/2L)^2)) * t) + p)')
    global amplituda
    amplituda = Entry(root, width=15)
    l_amplituda = Label(root, text='Podaj wartosc \'Q\' amplitudy ladunku w ukladzie [C]:')
    global omega
    omega = Entry(root, width=15)
    l_omega = Label(root, text='Podaj wartosc \'w\' czestosci wlasnej drgan [rad/s]:')
    global wsplop
    wsplop = Entry(root, width=15)
    l_wsplop = Label(root, text='Podaj wartosc \'R\' rezystancji opornika [ohm]:')
    global masa
    masa = Entry(root, width=15)
    l_masa = Label(root, text='Podaj indukcyjnosc cewki \'L\' w ukladzie [H]:')
    global faza
    faza = Entry(root, width=15)
    l_faza = Label(root, text='Podaj faze \'p\' poczatkowa ruchu [rad]:')
    l_wzor.pack()
    l_amplituda.pack()
    amplituda.pack()
    l_omega.pack()
    omega.pack()
    l_wsplop.pack()
    wsplop.pack()
    l_masa.pack()
    masa.pack()
    l_faza.pack()
    faza.pack()

def tkwykres():
    global a
    a = float(amplituda.get())
    global w
    w = float(omega.get())
    global f
    f = float(wsplop.get())
    global m
    m = float(masa.get())
    global p
    p = float(faza.get())
    wykres()

def tkwartosc1():
    global a
    a = float(amplituda.get())
    global w
    w = float(omega.get())
    global f
    f = float(wsplop.get())
    global m
    m = float(masa.get())
    global p
    p = float(faza.get())
    global chwilat
    chwilat = Entry(root, width=15)
    l_chwilat = Label(root, text='Wprowadz chwile czasu \'t\' trwania drgania [s]:')
    l_chwilat.pack()
    chwilat.pack()
    zatwierdz = Button(root, text='Zatwierdz', command=tkwartosc2)
    zatwierdz.pack()

def tkwartosc2():
    global t
    t = float(chwilat.get())
    str_t = str(t)
    wartosc()
    zapis()
    l_wartosc = Label(root, text='Drganie w chwili ' + str_t + 's wyniosło:\n' + jednostka)
    l_wartosc.pack()
#_______________________________________________________________________________________________________________________

#wybór rodzaj drgań
lrodzaj = Label(root, text='Wybierz rodzaj tłumionych drgan harmonicznych:')

mechbutton = Button(root, text='Mechaniczne', command=mech, fg='red')
elbutton = Button(root, text='Elektryczne', command=el, fg='blue')

lrodzaj.pack()
mechbutton.pack()
elbutton.pack()

#wykres/wartość
lwybor = Label(root, text='Wybierz wykres lub wartosc drgan dla konkretnej chwili czasu:')
bwykres = Button(root, text='Wykres', command = tkwykres)
bwartosc = Button(root, text='Wartosc', command=tkwartosc1)
lwybor.pack()
bwykres.pack()
bwartosc.pack()

#przycisk wyjścia
exit = Button(root, text="Wyjscie", command=root.destroy)
exit.pack()
root.mainloop()

# #WYBÓR: MECHANICZNE - WARTOŚĆ LUB WYKRES
#     if opcja_1 == 1:
#         print('Drgania mechaniczne:\n x = A * (exp(-f/(2m) * t)) * sin((sqrt(w^2 - ((f/2m)^2)) * t) + p)')
#         a = float(input('Podaj wartosc \'A\' amplitudy drgan mechanicznych [m]:'))
#         w = float(input('Podaj wartosc \'w\' czestosci wlasnej drgan [rad/s]:'))
#         f = float(input('Podaj wartosc \'f\' wspolczynnika oporow ruchu [kg/s]:'))
#         m = float(input('Podaj mase \'m\' drgajacego ciala [kg]:'))
#         p = float(input('Podaj faze \'p\' poczatkowa ruchu [rad]:'))
#         b = 0
#         while b == 0:
#             wybor = int(input('Wpisz 1, aby otrzymac wartosc wychylenia w konkretnej chwili czasu lub 2, aby wyswietlic wykres drgan w funkcji czasu:'))
#             match wybor:
# #MECH-WARTOŚĆ
#                 case 1:
#                     t = float(input('Podaj moment ruchu:[s]'))
#                     b = 1
#                     if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
#                         print('Wartosc wychylenia w chwili czasu t =', t, 's wyniosla ', wartosc(), 'm')
#                         drganie = 'Wartosc wychylenia '
#                         jednostka = ' m'
#                         zapis()
#                     else:
#                         print('Brak drgan dla wprowadzonych parametrow. Zachodzi zanik eksponencjalny')
# #WYBÓR: ELEKTRYCZNE - WARTOŚĆ LUB WYKRES
#     if opcja_1==2:
#         print('Drgania elektryczne:\n q = Q * (exp(-R/(2L) * t)) * sin((sqrt(w^2 - ((R/2L)^2)) * t) + p)')
#         a = float(input('Podaj wartosc \'Q\' amplitudy ladunku [C]:'))
#         w = float(input('Podaj wartosc \'omega\' czestosci wlasnej drgan [rad/s]:'))
#         f = float(input('Podaj wartosc \'R\' rezystancji opornika w ukladzie [Ohm]:'))
#         m = float(input('Podaj indukcyjnosc cewki \'L\' w ukldzie [H]:'))
#         p = float(input('Podaj faze poczatkowa ruchu \'phi\' [rad]:'))
#         b = 0
#         while b == 0:
#             wybor = int(input(
#                 'Wpisz 1, aby otrzymac wartosc ladunku w ukladzie w konkretnej chwili czasu lub 2, aby wyswietlic wykres drgan w funkcji czasu:'))
#             match wybor:
# #EL-WARTOŚĆ
#                 case 1:
#                     t = float(input('Podaj moment drgan:[s]'))
#                     b = 1
#                     if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
#                         print('Wartosc ladunku w ukladzie w chwili czasu t =', t, 's wyniosla ', wartosc(), 'C')
#                         drganie = 'Wartosc ladunku w ukladzie RLC '
#                         jednostka = ' C'
#                         zapis()
#                     else:
#                         print('Brak drgan dla wprowadzonych parametrow. Zachodzi zanik eksponencjalny')
