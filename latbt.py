from dolgozo import Dolgozo

class Latbt:

  def olvas_fajl(self):
    fp = open('latbt.txt', 'r', encoding='utf-8')
    lines = fp.readlines()
    fp.close()

    self.dolgozok = []
    for line in lines:
      (nev, telepules, fizetes) = line.split(':')
      dolgozo = Dolgozo(nev, telepules, fizetes)
      self.dolgozok.append(dolgozo)

  def szamitAtlag(self):
    osszesFizu = 0
    for dolgozok in self.dolgozok:
        osszesFizu += int(dolgozok.fizetes)

    print("Fizetések átlaga: ", osszesFizu/len(self.dolgozok))

  def kiirTelepulesek(self):
    for dolgozok in self.dolgozok:
        print("Dolgozó: "+ dolgozok.nev + " - Település: " + dolgozok.telepules)

  def bekerDolgozo(self):
    ujNev = input("Kérem az új dolgozó nevét: ")
    ujTelepules = input("Kérem az új dolgozó települését: ")
    ujFizetes = input("Kérem az új dolgozó fizetését: ")
    ujdolgozo = Dolgozo(ujNev, ujTelepules, ujFizetes)
    self.kiirFajlba(ujdolgozo)

  def kiirFajlba(self, dolgozo):
    fp = open('uj.txt', 'a', encoding='utf-8')
    fp.write(dolgozo.nev)
    fp.write(':')
    fp.write(dolgozo.telepules)
    fp.write(':')
    fp.write(dolgozo.fizetes)
    fp.write('\n');
    fp.close()


latbt = Latbt()
latbt.olvas_fajl()
latbt.szamitAtlag()
latbt.kiirTelepulesek()
latbt.bekerDolgozo()
