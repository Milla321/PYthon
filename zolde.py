zoldsegek = ["karalábé", "vöröshagyma", "cékla", "paprika"]
zoldsegDarab = 0
zoldseg = ''
while(zoldseg != "vege"):
    zoldseg = input("Kérem a zöldség nevét: ")
    if(zoldseg in zoldsegek):
        zoldsegDarab+=1
        print("OK")
    else:
        print("Nem megfelelő zöldség")

print("Elfogadott zöldségek száma: ", zoldsegDarab, "db")
