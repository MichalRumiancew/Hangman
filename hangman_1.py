import random

#powitanie
print('Czesc, podaj swoje imie: ')
imie = input()

#lista hasel
lista = ['Michał','tata', 'slowo']

#haslo
haslo = str(lista[random.randint(0,len(lista)-1)])
tablica = list(haslo)

#tablica sluzy do wyswiatlania _ _ _ _
for i in range(len(haslo)):
    tablica[i] = '_'

#zmienna reprezentujaca ilosc zyc
zycia = 6

#petla while, w ktorej bedzie realizowana gra
while zycia > 0:
    print('')
    print(imie, ' pozostalo ci ', zycia, ' zyc')
    print('')
    print(' '.join(tablica))
    print(' ')

    #prosimy uzytkownika o podanie litery
    print('Podaj swoja litere: ')
    litera = input()

    #udalo sie odgadnac
    if litera in haslo:
        #zmieniamy znak podkreslenia na odgadnieta litere
        for i in range(len(haslo)):
            if(haslo[i] == litera):
                tablica[i] = litera
        #sprawdzant czy tablica jest juz rowna haslu
        #czy udalo sie odgadnac caly wyraz
        if ''.join(map(str,tablica)) == haslo:
            print('')
            print(imie, ' pozostalo ci ', zycia, ' zyc')
            print('')
            print(' '.join(tablica))
            print(' ')
            print(imie, ' wygrales!')
            break
    #nie udalo sie
    else:
        zycia -= 1