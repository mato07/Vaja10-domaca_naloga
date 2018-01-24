# -*- coding: utf-8 -*-

import random


def main():

    print
    print "Pozdravljen v igri skrito število. Poskusi uganiti število med 1 in 100."
    print

    skrito_stevilo = random.randint(1, 100)

    while True:

        ugani_stevilo = int(raw_input("Vnesi iskano število: "))

        if ugani_stevilo == skrito_stevilo:
            print "Čestitamo uganili ste število!"
            break
        elif ugani_stevilo < skrito_stevilo:
            print "Vaše število je manjše od iskanega. Poskusi znova."
        else:
            print "Vaše število je večje od iskanega. Poskusi znova."
    print
    print "Lep dan še naprej!"

if __name__ == '__main__':
    main()