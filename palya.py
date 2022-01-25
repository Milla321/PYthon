#Talián Lászlóné
#SZOFT I/1//2/E  
#2022-01-15

teruletek = ("Budapest", "Miskolc", "Pécs", "Zalaegerszeg")
print(teruletek)
print(type(teruletek))
terulet = input("Kérem adja meg mely területhez tartozik az adott pálya: ")

if(terulet in teruletek):
    oregedesiIdo = int(input("A pálya öregedési ideje években: "))
    if(oregedesiIdo>2 and oregedesiIdo<6):
        print("A pálya felülvizsgálatot igébyel!")
    elif oregedesiIdo>5:
        print("Sürgős karbantartás!")
    else:
        print("Normál")
else:
    print("Nincs ilyen terület")
