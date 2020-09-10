# zadanie 1
formaty = (' .jpg ', '.bmp ', 'png')
filename_1 = 'obrazek.jpg'
filename = filename_1

is_image = filename.endswith(formaty)

print(is_image)

is_image = (filename[-4:]) == ".jpg"
print(is_image)
# zadanie 2
song = " work work work work work work work"
zlicz_work = song.count('work')
print(zlicz_work)
# zadanie 3

song = "jkahfjk jkshfjs hfj jsfhjshfj sjfh jshf tired kjshajkshajsh"
kiedy_zmeczy = song.find('tired')
print(kiedy_zmeczy)

# zadanie 4 zamiana tekstu
song = 'spiewa sobie dirty Dirty tired song '
zamiana = song.replace('dirty', 'programming').replace('tired', 'pyton').replace('Dirty', 'Programming')
print(zamiana)

# zadanie 5 -

num = 128
akcja = ((num+32)*3-64//2)
print(num, akcja)

# zadanie 6 - działania matematyczne
div_res = (akcja//100) ** 4
mod_res = (akcja % 100 + 2)
print(div_res, mod_res)

# zadanie 7
zlotowki_1 = 14
grosze_1 = 23
zlotowki_2 = 10
grosze_2 = 50

suma_1 = (zlotowki_1 + zlotowki_2)
suma_2 = (grosze_1 + grosze_2)
print(suma_1,suma_2,sep=',')

# zadanie 8
zlotowki_1, grosze_1 = 26,78
zlotowki_2, grosze_2 = 4,50
grosze_wynik = (grosze_1 + grosze_2) % 100
grosze_wynik2 = (grosze_1 + grosze_2) // 100
kwota = (zlotowki_1 + zlotowki_2) + grosze_wynik2
print(kwota, grosze_wynik, sep= ',', end='zł\n')
# zadanie 9 if
a = 2
#while
#if a == 2:
#    print('kiss my ass', a + 1)
#else:
#    print('dupa jasia')
# zadanie 10
i = 0
while i < 6:
    i += 1
    if i == 3:
        break
    print(i)
# zadanie 11
x = 10
print(-3>x!=10)
# zadanie 12
x = input('Podaj liczbę od 0 do 100 \n')
x1= float(x)
if ( 100 > x1 and x1 >50) or x1 == 99:
    print('trafiony')
else:
    print('Twoja liczba powiększona o 10 to:', (x1 + 10))

# zadanie 12