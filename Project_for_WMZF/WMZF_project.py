import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import *
from tkinter import messagebox

def wartosc():
    x = a * (np.exp(-f / (2 * m) * t)) * np.sin((np.sqrt(abs((w * 2) - ((f / (2 * m)) * 2))) * t) + p)
    return round(x,5)

def zapis():
    zapis_t = repr(t)
    zapis_x = repr(wartosc())
    zapis_jednostka = jednostka
    plik = open("Drganie w chwili t", "w")
    plik.write("Wartosc drgania w ostatnio wybranej chwili czasu:\nt = " + zapis_t + " s\nwyniosla:\n" + zapis_x + zapis_jednostka)
    plik.close()

def wykres():
    t_data = []
    x_data = []
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 60)
    ax.set_ylim(-(a + 1), (a + 1))
    line, = ax.plot(0, 0)
    plt.title(title)
    plt.xlabel('Czas - t [s]')
    plt.ylabel(ylabel)
    plt.grid()
    def animation_frame(t):
        t_data.append(t)
        x_data.append(a * (np.exp(-f / (2 * m) * t)) * np.sin((np.sqrt(abs((w * 2) - ((f / (2 * m)) * 2))) * t) + p))
        line.set_xdata(t_data)
        line.set_ydata(x_data)
        return line,
    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 60, 0.1), interval=1, blit=True, repeat=False)
    if ((w * 2) - ((f / (2 * m)) * 2)) >= 0:
        return plt.show()
    else:
        return Label(nowe_okno, text='Brak drgan dla wprowadzonych parametrow! Zachodzi zanik eksponencjalny.').pack()

def mech():
    global nowe_okno
    nowe_okno = Toplevel(root)
    nowe_okno.title("Drgania mechaniczne: x(t)")
    nowe_okno.geometry("450x500+450+160")
    global title
    title = 'Drgania mechaniczne: x(t)'
    global ylabel
    ylabel = 'Wychylenie - x [m]'
    global jednostka
    jednostka = ' m'
    l_wzor = Label(nowe_okno, text='x = A * (exp(-f/(2m) * t)) * sin((sqrt(w^2 - ((f/2m)^2)) * t) + p)')
    global amplituda
    amplituda = Entry(nowe_okno, width=15)
    l_amplituda = Label(nowe_okno, text='Podaj wartosc \'A\' amplitudy drgan mechanicznych [m]:')
    global omega
    omega = Entry(nowe_okno, width=15)
    l_omega = Label(nowe_okno, text='Podaj wartosc \'w\' czestosci wlasnej drgan [rad/s]:')
    global wsplop
    wsplop = Entry(nowe_okno, width=15)
    l_wsplop = Label(nowe_okno, text='Podaj wartosc \'f\' wspolczynnika oporow ruchu [kg/s]:')
    global masa
    masa = Entry(nowe_okno, width=15)
    l_masa = Label(nowe_okno, text='Podaj mase \'m\' drgajacego ciala [kg]:')
    global faza
    faza = Entry(nowe_okno, width=15)
    l_faza = Label(nowe_okno, text='Podaj faze \'p\' poczatkowa ruchu [rad]:')
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
    lwybor = Label(nowe_okno, text='Wybierz wykres lub wartosc drgan dla konkretnej chwili czasu:')
    bwykres = Button(nowe_okno, text='Wykres', command=tkwykres)
    bwartosc = Button(nowe_okno, text='Wartosc w chwili czasu', command=tkwartosc1)
    exit = Button(nowe_okno, text="Wyjscie", command=root.destroy)
    lwybor.pack()
    bwykres.pack()
    bwartosc.pack()
    exit.pack()
    global clicks_mech
    clicks_mech += 1
    if clicks_mech == 1:
        mechbutton.config(state="disabled")
        elbutton.config(state="disabled")

def el():
    global nowe_okno
    nowe_okno = Toplevel(root)
    nowe_okno.title("Drgania elektryczne: q(t)")
    nowe_okno.geometry("500x450+450+160")
    global title
    title = 'Drgania elektryczne: q(t)'
    global ylabel
    ylabel = 'Wartosc ladunku - q [C]'
    global jednostka
    jednostka = ' C'
    l_wzor = Label(nowe_okno, text='x = Q * (exp(-R/(2L) * t)) * sin((sqrt(w^2 - ((R/2L)^2)) * t) + p)')
    global amplituda
    amplituda = Entry(nowe_okno, width=15)
    l_amplituda = Label(nowe_okno, text='Podaj wartosc \'Q\' amplitudy ladunku w ukladzie [C]:')
    global omega
    omega = Entry(nowe_okno, width=15)
    l_omega = Label(nowe_okno, text='Podaj wartosc \'w\' czestosci wlasnej drgan [rad/s]:')
    global wsplop
    wsplop = Entry(nowe_okno, width=15)
    l_wsplop = Label(nowe_okno, text='Podaj wartosc \'R\' rezystancji opornika [ohm]:')
    global masa
    masa = Entry(nowe_okno, width=15)
    l_masa = Label(nowe_okno, text='Podaj indukcyjnosc cewki \'L\' w ukladzie [H]:')
    global faza
    faza = Entry(nowe_okno, width=15)
    l_faza = Label(nowe_okno, text='Podaj faze \'p\' poczatkowa ruchu [rad]:')
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
    lwybor = Label(nowe_okno, text='Wybierz wykres lub wartosc drgan dla konkretnej chwili czasu:')
    bwykres = Button(nowe_okno, text='Wykres', command=tkwykres)
    bwartosc = Button(nowe_okno, text='Wartosc w chwili czasu', command=tkwartosc1)
    exit = Button(nowe_okno, text="Wyjscie", command=root.destroy)
    lwybor.pack()
    bwykres.pack()
    bwartosc.pack()
    exit.pack()
    global click_el
    click_el+=1
    if click_el == 1:
        elbutton.config(state="disabled")
        mechbutton.config(state="disabled")

def tkwykres():
    global a
    global w
    global f
    global m
    global p
    try:
        if amplituda.get() == '':
            a = 0
        else:
            a = float(amplituda.get())
        if omega.get() == '':
            w = 0
        else:
            w = float(omega.get())
        if wsplop.get() == '':
            f = 0
        else:
            f = float(wsplop.get())
        if masa.get() == '':
           m= 0
        else:
            m = float(masa.get())
        if faza.get() == '':
            p = 0
        else:
            p = float(faza.get())
        if m == 0:
            messagebox.showerror("Bład", "Nie mogę wykonać dzielenia przez 0!")
        else:
            wykres()
    except ValueError:
        messagebox.showerror("Blad!", "Proszę podać wartosći liczbowe")
        #czegoś brakuje
def tkwartosc1():
    global a
    global w
    global f
    global m
    global p
    try:
        if amplituda.get() == '':
            a = 0
        else:
            a = float(amplituda.get())
        if omega.get() == '':
            w = 0
        else:
            w = float(omega.get())
        if wsplop.get() == '':
            f = 0
        else:
            f = float(wsplop.get())
        if masa.get() == '':
            m = 0
        else:
            m = float(masa.get())
        if faza.get() == '':
            p = 0
        else:
            p = float(faza.get())
        if m == 0:
            messagebox.showerror("Błąd!", "Nie mogę wykonać dzielenia przez 0!")

        else:
            global chwilat
            chwilat = Entry(nowe_okno, width=15)
            l_chwilat = Label(nowe_okno, text='Wprowadz chwile czasu \'t\' trwania drgania [s]:')
            l_chwilat.pack()
            chwilat.pack()
            zatwierdz = Button(nowe_okno, text='Zatwierdz', command=tkwartosc2)
            zatwierdz.pack()
    except ValueError:
        messagebox.showerror("Błąd!", "Proszę podać wartości liczbowe")
        # czegoś brakuje
def tkwartosc2():
    global t
    try:
        t = float(chwilat.get())
        if ((w * 2) - ((f / (2 * m)) * 2)) < 0:
            zanik = Label(nowe_okno, text='Brak drgan dla wprowadzonych parametrow! Zachodzi zanik eksponencjalny.')
            zanik.pack()
        else:
            str_t = str((chwilat.get()))
            x = str(wartosc())
            zapis()
            l_wartosc = Label(nowe_okno, text='Wartość drgania w chwili t =' + str_t + 's wyniosła:\n' + x + jednostka)
            l_wartosc.pack()
    except ValueError:
        messagebox.showerror("Bląd!", "Proszę podać wartosći liczbowe")
def zamykanie_okna():
    if messagebox.askokcancel("Zamykanie okna","Czy chcesz zamknąć okno?"):
        root.destroy()
root = Tk()
clicks_mech,click_el = 0,0
root.protocol("WM_DELETE_WINDOW",zamykanie_okna)
root.title("Drgania")
root.geometry("300x80+550+200")
lrodzaj = Label(root, text='Wybierz rodzaj tłumionych drgan harmonicznych:')
mechbutton = Button(root, text='Mechaniczne', command=mech, fg='red',)
elbutton = Button(root, text='Elektryczne', command=el, fg='blue')
lrodzaj.pack()
mechbutton.pack()
elbutton.pack()
root.mainloop()
