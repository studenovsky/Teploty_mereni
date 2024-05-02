# teploty_engine.py - program pro zpracování teplotních dat
# autor: Jaroslav Studenovský <studenovskyj@jirovcovka.net>

import sys

#Volí se soubor, který se má otevřít
if len(sys.argv)>=2:
    filename=sys.argv[1]
else:
    filename="teploty.txt"

#Vytvoření proměnných
pocitadlo = 0
max_teplota = float('-inf')
min_teplota = float('inf')
soucet_zapornych_teplot = 0
soucet_kladnych_teplot = 0
pocitadlo_zapornych_teplot = 0
pocitadlo_kladnych_teplot = 0

#Otevření souboru a zpracování dat
fd = open(filename, "r")
for line in fd:
    cislo = line.strip()
    try:
        teplota = float(cislo)
        pocitadlo += 1

        if teplota > max_teplota:
            max_teplota = teplota
        if teplota < min_teplota:
            min_teplota = teplota
        
        if teplota < 0:
            soucet_zapornych_teplot += teplota
            pocitadlo_zapornych_teplot += 1
        if teplota > 0:
            soucet_kladnych_teplot += teplota
            pocitadlo_kladnych_teplot += 1
    except ValueError:
        pass
fd.close()

#Výpis výsledků
print("Celkem bylo nalezeno", pocitadlo, "teplot.")
print("Nejvyšší teplota byla", max_teplota)
print("Nejnižší teplota byla", min_teplota)
print("Průměrná záporná teplota byla", soucet_zapornych_teplot / pocitadlo_zapornych_teplot)
print("Průměrná kladná teplota byla", soucet_kladnych_teplot / pocitadlo_kladnych_teplot)

#Zápis výsledků do souboru
fd = open("statistika.txt", "w", encoding="utf-8")
fd.write(filename + ", Jaroslav Studenovský, 7.E \n")
fd.write("Celkem bylo nalezeno " + str(pocitadlo) + " teplot.\n")
fd.write("Nejvyšší teplota byla " + str(max_teplota) + "\n")
fd.write("Nejnižší teplota byla " + str(min_teplota) + "\n")
fd.write("Průměrná záporná teplota byla " + str(soucet_zapornych_teplot / pocitadlo_zapornych_teplot) + "\n")
fd.write("Průměrná kladná teplota byla " + str(soucet_kladnych_teplot / pocitadlo_kladnych_teplot))
fd.close()

#Konec programu