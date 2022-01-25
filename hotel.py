
class Hotel:
    def olvas_fajl(self):
        fp = open('adat.txt', 'r')
        lines = fp.readlines()
        fp.close()
        self.vendegek = []
        for line in lines:
            (nev, erkezes, ar) = line.split(':')
            vendeg = Vendeg(nev, erkezes, ar)
            self.vendegek.append(vendeg)
            
    def ir_fajlhoz(self, vendeg):
        fp = open('ujak.txt', 'r')
        fp.write(vendeg.nev)
        fp.write(':')
        fp.write(vendeg.erkezes)
        fp.write(':')
        fp.write(vendeg.ar)
        fp.close()

    def osszeg(self):
        pass
    
    def beker(self):
        pass
