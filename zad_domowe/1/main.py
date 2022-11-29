#zad_1
imie_2 = 'Magda\n'
moje_imie_2 = 'Marta\n'
moje_drugie_imie = 'Agnieszka'
print( imie_2, moje_imie_2, moje_drugie_imie )
print('--------------------------------------------------------------------------------------------------------------')

#zad_2
print(2>3)  # b=3 jest większa od a=2 dlatego nie prawda
print('a' < 'b') # a w  alfabecie idzie wczesniej niz b dlatego prawda
print(10>10) #10 nie jest > niz 10 => nie prawda
print(bool(33)) #bylo by nieprawda jesli w nawiasie było 0 albo liczby ujemne albo nic by nie było w nawiasach
print(bool('False')) # jesli jest cos w nawiasach to zawsze bedzie prawda
print('--------------------------------------------------------------------------------------------------------------')

#zad 3
print(10//3)  #  dzielenie " do gory" целочисленное деление
print(10 ** 3) # potega
y = 3; y += 1 # y += y +1
print(y)

print('--------------------------------------------------------------------------------------------------------------')

#zad_4
zm_1 = '2'
print(zm_1)
zm_2 = '2.5'
print(zm_2)
e = 10
przekatne_romba_1 = e
f = 10
przekatne_romba_2 = f
p =(1/2*  przekatne_romba_1 * przekatne_romba_2 )
print(p)
print('Pole rombu o przekątnych ',e,' i ',f,' wynosi ',p,'')
print('--------------------------------------------------------------------------------------------------------------')
#zad_5
linia1 = 'ATOM 1 C AMFBA 1 39.272 30.272 53.968 1.00 0.00 C'
linia_2 ='ATOM 2 O AMFBA 1 42.771 29.112 54.038 1.00 0.00 O'
print(linia1[9:13])
x_1 = float(linia1[17:23])
print(str(x_1))
y_1 = float(linia1[24:30])
print(str(y_1))
z_1 = float(linia1[31:37])
print(str(z_1))
x_2 = float(linia_2[17:23])
y_2 =  float(linia_2[24:30])
z_2 = float (linia_2[31:37])
dr = ( (x_1-x_2) ** 2 + (y_1-y_2) ** 2 + (z_1-z_2) ** 2)**(1/2)
print('Odległość atomu węgla o współrzędnych ',x_1,' ',y_1,' i ',z_1,'  od atomu tlenu o współrzędnych ',x_2,' ',y_2,' i ',z_2,' wynosi ',dr,' ')
print('--------------------------------------------------------------------------------------------------------------')

#zad_6
znaki = 'abcdef'
print(5*znaki)
imie = ' Mark '
print( 10 * imie)
nazwisko = 'Pantsiusheu'
print( (imie + nazwisko)*2) # mozna tylko dodawac albo mnozyc

d_1 = '++++'
d_2 = '- - - - - - - -'
d_3 = '++++'
d_7 = '- - - - - - - -'
d_4 = '++'
d_5 = '++'
print( d_1+d_2+d_3+d_7+d_4+d_5)