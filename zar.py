from random import randint
zar = randint(0,6)
print(f"zar = {zar}")

sayac = 0

while sayac <5:
    girdi = int(input("Devam etmek için 1 e bas = "))
    if girdi == 1:
        zar = randint(0, 6)
        print(f"zar = {zar}")
        sayac+=1
        if sayac==5:
         break
    else:
        break





