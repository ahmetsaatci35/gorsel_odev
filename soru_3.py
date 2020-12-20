ifade = input("ifade:")
aranan_ifade = input("aranan ifade: ")
if ifade.find(aranan_ifade) == -1:
    print("aranan ifade bulunamadı.")
else:
    print(ifade[ifade.find(aranan_ifade) -1: ifade.find(aranan_ifade) + len(aranan_ifade) +1])