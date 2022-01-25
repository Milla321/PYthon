zoldsegek = ["karalábé", "vöröshagyma", "cékla"]
zoldseg = input("Kérem a zöldség nevét: ")

if zoldseg != "":
    if(zoldseg in zoldsegek):
        print("Rendben")
    else:
        print("Nincs ilyen zöldség!")
