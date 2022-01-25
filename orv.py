from paciens import Paciens

paciensek = []
class Orv:
    def beolvas(self):
        fajlnev = 'paciens.txt'
        fajlmod = 'r'
        fp = open(fajlnev, fajlmod, encoding='utf-8')
        sorok = fp.readlines()[1:]
        fp.close()
        #self.paciensek = []
        print(sorok[1])
        for sor in sorok:
            print (sor)
            (nev, tunet, kezeles, ido, ar) = sor.split(':')

            paciens = Paciens(nev, tunet, kezeles, ido, ar)
            paciensek.append(paciens)

    def moxavalKezeltek(self):
        for record in paciensek:
            if(record.kezeles == 'moxa'):
                print(record.nev)

    def bevetel(self):
        bevetel = 0
        for record in paciensek:
            bevetel += int(record.ar)
        print (bevetel)

    def tizezernelNagyobbBevetel(self):
        for record in paciensek:
            if(int(record.ar)>11000):
                print(record.nev)


Orv().beolvas()
Orv().moxavalKezeltek()
Orv().bevetel()
Orv().tizezernelNagyobbBevetel()
