from random import randint
zar = randint(1,6)
print(f"zar = {zar}")

sayac = 0

while sayac <5:
    girdi = int(input("Devam etmek için 1 e bas = "))
    if girdi == 1:
        zar = randint(1, 6)
        print(f"zar = {zar}")
        sayac+=1
        if sayac==5:
         break
    elif girdi != 1:
        print("Uygulamadan Çıkış yapıldı. !")
        break
