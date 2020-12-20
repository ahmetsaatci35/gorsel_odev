gelen_veri = "send-181-3-0-1\nreceive-170-3-0\n"
diziye_bol = gelen_veri.split("\n")
ekranda_cizgi = 0
def yeni_fanction(kod, parcala):
   if ((int(parcala[0]) >= 0 and int(parcala[0]) <= 255) and (int(parcala[1]) >= 1 and int(parcala[1]) <= 4) and (int(parcala[2]) >= 0 and int(parcala[2]) <= 1) and ((len(parcala) == 4 and int(parcala[3]) >= 0 and int(parcala[3]) <= 1) or len(parcala) == 3)):
      print("Kod Tipi: " + kod)
      if (int(parcala[0]) >= 0 and int(parcala[0]) <= 50):
         print("Sinyal Gucu: " + parcala[0] + " - Cok Zayif")
      elif (int(parcala[0]) >= 51 and int(parcala[0]) <= 100):
         print("Sinyal Gucu: " + parcala[0] + " - Zayif")
      elif (int(parcala[0]) >= 101 and int(parcala[0]) <= 150):
         print("Sinyal Gucu: " + parcala[0] + " - Orta")
      elif (int(parcala[0]) >= 151 and int(parcala[0]) <= 200):
         print("Sinyal Gucu: " + parcala[0] + " - Guclu")
      elif (int(parcala[0]) >= 201 and int(parcala[0]) <= 255):
         print("Sinyal Gucu: " + parcala[0] + " - Cok Guclu")
      else:
         print("Sinyal Gucu: Gecersiz")
      if (int(parcala[1]) == 1):
         print("Cihaz: " + parcala[1] + " - Televizyon")
      elif (int(parcala[1]) == 2):
         print("Cihaz: " + parcala[1] + " - Camasir Makinesi")
      elif (int(parcala[1]) == 3):
         print("Cihaz: " + parcala[1] + " - Buzdolabi")
      elif (int(parcala[1]) == 4):
         print("Cihaz: " + parcala[1] + " - Firin")
      else:
         print("Cihaz: Gecersiz")
      if (int(parcala[2]) == 0):
         print("Durumu: " + parcala[2] + " - Off")
      elif (int(parcala[2]) == 1):
         print("Durumu: " + parcala[2] + " - On")
      else:
         print("Durumu: Gecersiz")
      if (len(parcala) == 4):
         if (int(parcala[3]) == 0):
            print("Cevap: " + parcala[3] + " - Istenmiyor")
         elif (int(parcala[3]) == 1):
            print("Cevap: " + parcala[3] + " - Isteniyor")
         else:
            print("Cevap: Gecersiz")
   else:
      print("Error: ikinci bolum hatali")
for don_aktar in diziye_bol:
   if (len(don_aktar) > 0):
      parcala = don_aktar.split("-")
      veri_tipi = parcala.pop(0)
      ekranda_cizgi += 1
      if (ekranda_cizgi > 1):
          print("------")
      if (veri_tipi == "send"):
         if (len(parcala) != 4):
            print("Error: ikinci bolum hatali")
         else:
            yeni_fanction(veri_tipi + " - Giden", parcala)
      elif (veri_tipi == "receive"):
         if (len(parcala) != 3):
            print("Error: ikinci bolum hatali")
         else:
           yeni_fanction(veri_tipi + " - Gelen", parcala)
      else:
       print("Error: send ya da receive icermiyor")


