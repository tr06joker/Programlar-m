print("Yapan : tr06joker--Version : V1.0--Program : Sifer/")
sifreDegeri = -2
sifrelenecek_cümle = input("Şifrelenecek Cümleyi Giriniz: ")
for sifrem in sifrelenecek_cümle:
    print(chr(ord(sifrem) + sifreDegeri))
