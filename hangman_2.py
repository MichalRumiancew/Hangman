import random

#powitanie
print('Czesc, podaj swoje name: ')
name = input()

#word_list hasel
word_list = ['Michał','tata', 'slowo']

#password
password = str(word_list[random.randint(0,len(word_list)-1)])
table = list(password)

#table sluzy do wyswiatlania _ _ _ _
for i in range(len(password)):
    table[i] = '_'

#zmienna reprezentujaca ilosc zyc
zycia = 6

#petla while, w ktorej bedzie realizowana gra
while zycia > 0:
    print('')
    print(name, ' pozostalo ci ', zycia, ' zyc')
    print('')
    print(' '.join(table))
    print(' ')

    #prosimy uzytkownika o podanie litery
    print('Podaj swoja litere: ')
    litera = input()

    #udalo sie odgadnac
    if litera in password:
        #zmieniamy znak podkreslenia na odgadnieta litere
        for i in range(len(password)):
            if(password[i] == litera):
                table[i] = litera
        #sprawdzant czy table jest juz rowna haslu
        #czy udalo sie odgadnac caly wyraz
        if ''.join(map(str,table)) == password:
            print('')
            print(name, ' pozostalo ci ', zycia, ' zyc')
            print('')
            print(' '.join(table))
            print(' ')
            print(name, ' wygrales!')
            break
    #nie udalo sie
    else:
        zycia -= 1