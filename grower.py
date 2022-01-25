from product import Product

class Grower:
    def read_file(self):
        fp = open('products.txt', 'r', encoding='utf-8')
        lines = fp.readlines()
        fp.close()

        self.products = []

        for line in lines[1::]:
            (id, name, price, quantity) = line.split(';')
            product = Product(id, name, price, quantity)
            self.products.append(product)

    # legdrágább zöldség
    def larger(self):
        bigger = 0
        for product in self.products:
            if int(product.price) > bigger:
                bigger = product.price
        print("A legnagyobb Ár: ", bigger)

    # Az összes paprika ára
    def calcPepperPrice(self):
        for prod in self.products:
            if(prod.name == "paprika"):
                print("Az összes paprika érétke: ", int(prod.price)*int(prod.weight))

    # Mennyi a vöröshagyma és a karalábé tömege együtt?
    def sumOnionKohlrabiWeight(self):
        ossztomeg = 0
        for prod in self.products:
            if(prod.name == "vöröshagyma" or prod.name == "karalábé"):
                ossztomeg += prod.weight
        print("A vöröshagyma és a karalábé össztömege: ", ossztomeg, "kg")

    # Mi a neve legnagyobb tömegű zöldségnek?
    def showLargerWeight(self):
        tomeg = 0
        nev = '~'
        for prod in self.products:
            if(prod.weight > tomeg):
                tomeg = prod.weight
                nev = prod.name
        print("A legtöbb mennyiségű zöldség: " , nev , " (", tomeg , "kg)")

    # Van karalábé?
    def isHaveKohlrabi(self):
        for prod in self.products:
            if(prod.name == "karalábé" and prod.weight > 0):
                print("Igen van karalábé! (" , prod.weight , "kg)")
                return
        print("Sajna Nincs karalábé!")



    # Hány zöldség drágább mint 700 Ft.
    def moreThenSevenhundred(self):
        minAr = 700
        zoldsegNevek = ''
        darab = 0
        for prod in self.products:
            if(prod.price > 700):
                darab+=1
                zoldsegNevek+=prod.name + ", "
        print("Ennyi zöldség drágább mint", minAr , "Ft:" , darab , "db" , "(", zoldsegNevek,")")


grower = Grower()
grower.read_file()
grower.larger()
grower.calcPepperPrice()
grower.sumOnionKohlrabiWeight()
grower.showLargerWeight()
grower.isHaveKohlrabi()
grower.moreThenSevenhundred()
