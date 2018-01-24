# -*- coding: utf-8 -*-

import random

def ponavljajoca_stevila (x):

    loto_listek = []
    for i in range(x):
        nakljucno_stevilo = random.randint(1, 39)
        loto_listek.append(nakljucno_stevilo)
    return loto_listek

def neponavljajoca_stevila (x):

    loto_listek = []

    for i in range(x):
        while True:
            nakljucno_stevilo = random.randint(1, 39)
            if nakljucno_stevilo not in loto_listek:
                break
        loto_listek.append(nakljucno_stevilo)
    return loto_listek

def main():

    print
    print "Pozdravljeni v generatorju loto števil!"
    print

    stevilo = raw_input("Prosim vnesite koliko loto števil želite določiti: ")

    #print "Vaša srečna loto števila so: ", ponavljajoca_stevila(int(stevilo))
    print "Vaša srečna loto števila so: ", neponavljajoca_stevila(int(stevilo))

if __name__ == '__main__':
    main()


