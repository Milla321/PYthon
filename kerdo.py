# név: Kurdi Tibor
# osztály: SZOFT I/E/2
# készült: 2022-01-03

def vizsgalABetu(vizsgalando):
    if(vizsgalando.startswith('a',0,1)):
        return True
    else:
        return False

nev = input("Kérek adjon meg egy nevet: ");
aValkezdodoSzavak = 0

if(nev == 'erno'):
    print("Szia!")
    szo = 'szo'
    while szo != 'end':
        szo = input("Kérek egy szót: ");
        aValKezdodik = vizsgalABetu(szo)
        if(aValKezdodik):
            #print ("a-val kezdődik")
            aValkezdodoSzavak += 1
        else:
            pass

    print("'a' betüvel ennyi szó kezdődött:", aValkezdodoSzavak, "db")
