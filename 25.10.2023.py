# Namų darbai 25/10/2023:
#
#
# 1. Sukurkite prekių sąrašą su kainomis ir raskite brangiausią prekę.

# prekiu_sarasas = [
#     {"preke": "Arbuzas", "kaina": 5.25},
#     {"preke": "Limonadas", "kaina": 6.99},
#     {"preke": "Sokoladas", "kaina": 10.29}
# ]
#
# a = prekiu_sarasas[0]
# b = prekiu_sarasas[1]
# c = prekiu_sarasas[2]
#
# verte = max(a["kaina"],b["kaina"],c["kaina"])
#
# if a["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {a["preke"]}')
# if b["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {b["preke"]}')
# if c["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {c["preke"]}')



# 2. Sukurkite žodyną su studento pažymiais ir raskite ar studentas išlaikė egzaminą;


# studento_pazymiai = {
#     'Matematika': 6,
#     'Anglu': 7,
#     'Geografija': 6
# }
#
# if studento_pazymiai['Matematika'] <= 5:
#     print('Matematikos neislaike')
# else:
#     print('Matematikos islaike')
# if studento_pazymiai['Anglu'] <= 5:
#     print('Anglu neislaike')
# else:
#     print('Anglu islaike')
# if studento_pazymiai['Geografija'] <= 5:
#     print('Geografijos neislaike')
# else:
#     print('Geografijos islaike')




# 3. Sukurkite žodyną su kliento informacija ir patikrinkite ar jo sąskaitoje yra pakankamai lėšų tam tikram pirkiniui.


# Linos pavyzdys:
#
# Klientas = {
#     "Vardas": "Jonas",
#     "Amzius": 40,
#     "Miestas": "Vilnius",
#     "Telefonas": "+37063025252",
#     "Sask.likutis": 10000
# }
# # print(Klientas)
#
# Pirkinys = 500
# # 10000 < 500 = False
# if Klientas["Sask.likutis"] < Pirkinys:
#     print("lesu nepakanka")
# else:
#     print("galima pirkti")




# 4.Pagal nurodytą pajamų sumą, paskaičiuokite mokesčius, taikant šias taisykles: pajamoms iki 1000 - 10%, nuo 1001 iki 5000 - 15%, virš 5000 - 20%.

# pajamos = 100
#
# if pajamos > 5000:
#     print("Mokesciu suma", + pajamos * 0.2)
# elif pajamos > 1000:
#     print("Mokesciu suma", + pajamos * 0.15)
# elif pajamos > 0:
#     print("Mokesciu suma", + pajamos * 0.1)
# else:
#     print("Pajamu nera")





# MOKYMASIS:

#for raktas in seka:
#print(raktas)

# for i in range(5):
#     print("Skaicius", i)

# skaiciai = [1,2,3,4,5]
#
# for skaicius in skaiciai:
#     print("Mano saraso skaicius:", skaicius)

# tekstas = "Python data science"
# for raide in tekstas:
#     print(raide)

# zodynas = {"a":1, "b":2,"c":3}
#
# for raktas in zodynas:
#     print(raktas, zodynas[raktas])


# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         break
#     print(skaicius)
#
# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         continue
#     print(skaicius)

# skaiciai = [10,20,30,40,50]
#
# suma = sum(skaiciai)
#
# vidurkis = suma / len(skaiciai)
# #print("Gautas vidurkis", vidurkis)
#
# for skaicius in skaiciai:
#     if skaicius > vidurkis:
#         print(skaicius)

# sarasas = ["jonas", "PEtras", "Antanas", "ona"]
# print('\n'.join(sarasas))
#
# for vardas in sarasas:
#     print(vardas)
#     print(vardas+'\n') #kitas budas spausdinti

#printina zodi atvirskciai pythion


# tekstas = 'python'
# kintamasis = ""
# for raide in tekstas:
#     kintamasis = raide+kintamasis
#     print(kintamasis)

#atspausdinti visa daugybe lentele

# max_skaicius = 10
# for i in range(1,max_skaicius + 1):
#     for j in range(1, max_skaicius + 1):
#         print(i*j, end ="\t") #end ir t reiskia kad bus stulpeliais???
#     print()


#listas(sarasas) kuriame butu tekstas, zodziai yra isskirti i atskirus indeksus (panaikinti kabutes tekste is listo)

# sarasas = ["Labas", "rytas", "mieli", "mokiniai"]
# kintamasis = ""
# for zodis in sarasas:
#     kintamasis += zodis + " "
#     sujungtas_tekstas = kintamasis.rstrip()
# print(sujungtas_tekstas)

# end ="\t"
# '\t'

# trumpa versija:
#
# sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
# for i in sarasas:
#     print(i, end=" ")

#WHILE loop'as

# skaicius = 1
#
# while skaicius <= 20:
#     print(skaicius)
#     skaicius += 1

# ivestis = int(input("Iveskite teigiama skaiciu_>"))
#
# while ivestis <0:
#     print("Jusu skaicius neigiamas")
#     ivestis = int(input("Bandykite dar karta"))
# print("Ivedete teigiama skaicius")


# MAZO ZAIIDIMO KODAS

# atsakymas = 5
# spejimas = int(input("Spekite skaiciu nuo 1 iki 10_>"))
#
# while spejimas != atsakymas:
#     spejimas = int(input("Neteisingas atsakymas! Bandykite dar karta_>"))
#
# print("Sveikiname, atspejote")

#galima parasyti:
# ar_veikia = True
# while ar_veikia:
# while True:
#     print("-----Meniu-----")
#     print("1. Atspausdinti pasisveikinima")
#     print("2. Iveskite nauja varda")
#     print("3. Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3_>")
#     if pasirinkimas == "1":
#         print(f'Labas!')
#     elif pasirinkimas == "2":
#         vardas = input("Iveskite nauja varda_>")
#
#         print("Sekmingai ivedete nauja varda")
#         print(f'Jusu vardas pakeistas i {vardas}')
#     elif pasirinkimas == "3":
#         print("Aciu, kad naudojates programa. IKI")
#         break #galima parasyti ir ar_veikia = False
#     else:
#         print("Neteisingas pasirinkimas! Bandykite dar karta")



# parasyti programa kurioje nurodytas paslaptingas zodis, jei neatspeja, programa turi is naujo pasileisti, tol kol atpses ta zodi

# paslaptingas_zodis = "batas"
# spejimas = input("Spekite paslaptingaji zodi: ")
#
# while spejimas != paslaptingas_zodis:
#     spejimas = input("Spekite paslaptingaji zodi DAR KARTA: ")
# print("Norime pasveikinti, laimejote!")


# programa, kurioj irasau skaiciu ir man turi ismesti to skaiicaus daugybos lentele. pvz, 5*1 yra 5, 5*2 yra 10 ir t.t iki 5*10

# pasirinkimas = int(input("Pasirinkite skaiciu nuo 1 iki 10: "))
# max_skaicius = 1
# while max_skaicius <= 10:
#     rezultatas = max_skaicius * pasirinkimas
#     print(f'{pasirinkimas} x {max_skaicius} = {rezultatas}')
#     max_skaicius += 1


# sintakse funkcijose: def funkcijosPavadinimas(argumentai):
#Jusu koda

# def pasisveikinti():
#     print("Hello Python")
#
#
# pasisveikinti()

# sita funkcija mums iskviecia funkcija is kito .py failo:
# if __name__ == '__main__':
#     pasisveikinti()


# def pasisveikinti(vardas):
#     print(f'Hello {vardas}')
#
#
# pasiveikinti("Martynas")

# def suma(a,b):
#     return a + b
#
# atsakymas = suma(5,3)
# print(atsakymas)

# def rodyti_meniu():
#     print("-----Meniu-----")
#     print("1. Prideti knyga")
#     print("2. Perziureti visas knygas")
#     print("3. Ieskoti knygos pagla pavadinima")
#     print("4. Iseiti")
#
#
# def prideti_knyga(knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima_>")
#     autorius = input("Iveskie knygos autoriu_>")
#     knygu_sarasas.append({"pavadinimas": pavadinimas,"autorius": autorius})
#     print(f"Knyga '{pavadinimas}' prideta!")
#
# def perziureti_knygas (knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius:{knyga['autorius']}")
#
#
# def ieskoti_knygos(knygu_sarasas):
#     ieskomas_pavadinimas = input("Ivekiste knygos pavadnima kurios ieskote_>")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius:{knyga['autorius']}")
#     else:
#         print(f" Knyga su pavadinimu: '{ieskomas_pavadinimas}' nerasta")
#
#
# def main():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma(1-4)_>")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             ieskoti_knygos(knygu_sarasas)
#         elif pasirinkimas == "4":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 4")
#
# if __name__ == '__main__':
#     main()


#bankine sistema. mes galime atidaryti sas, inesti pin, nusiimti pin, perziureti liktui, uzdaryti sas, iseiti is sistemos:

# banko_saskaitos = {
#
#
# }
# def rodyti_meniu():
#     print("\n=== Mini Banko sistema ===")
#     print("1. Atidaryti naują saskaitą")
#     print("2. Įnešti pinigus")
#     print("3. Nusiimti pinigus")
#     print("4. Peržiūrėti sąskaitos likutį")
#     print("5. Uždaryti sąskaitą")
#     print("6. Išeiti")
#
# def prideti_saskaita(paslaugos):
#     saskaitos_turetojas = input("Iveskite vardą: ")
#     pradinis_likutis = int(input("Įveskite pradinį pinigų likutį: "))
#     saskaitos_nr = len(banko_saskaitos) + 1
#     banko_saskaitos[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja sąskaita '{saskaitos_nr}' sekmingai prideta!")
#
# def inesti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite įnešamų pinigų sumą: "))
#     banko_saskaitos[saskaitos_nr]["pradinis_likutis"] += suma
#     print(f"Į sąskaitą nr.: '{saskaitos_nr}' sėkmingai įnešta '{suma}' eurai")
#
# def nusiimti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.: "))
#     suma = int(input("Įveskite nusiimamų pinigų sumą: "))
#     if suma <= banko_saskaitos[saskaitos_nr]["pradinis_likutis"]:
#         banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f"Iš sąskaitos nr.: '{saskaitos_nr}' sėkmingai nusiimta '{suma}' eurai")
#     else:
#         print(f"Jūsų pradinis likutis yra per mazas. Jis yra: '{banko_saskaitos[saskaitos_nr]['pradinis_likutis']}' eurai")
#
# def perziureti_likuti(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
#     print(f"Sąskaitos nr.: '{saskaitos_nr}' likutis yra '{likutis}' eurai")
#
# def istrinti_saskaita(paslaugos):
#     saskaitos_nr = int(input("Įveskite sąskaitos nr.:"))
#     del banko_saskaitos[saskaitos_nr]
#     print(f"Banko sąskaita nr.: '{saskaitos_nr}' buvo ištrinta")
#
#
# def main():
#     paslaugos = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksmą(1-4): ")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4":
#             perziureti_likuti(banko_saskaitos)
#         elif pasirinkimas == "5":
#             istrinti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "6":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 6")
#
# main()


#lokalus ir globalus kintamieji. globalu galima naudoit visur, o lokalu galima naudoti tik toje funkcijoje. kitoje funkcijoje lokalus nebus pasiekiamas.

# Sukurkite funkciją pvm_skaiciuokle(), kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.

# def pvm_skaiciuokle(kaina):
#     print(f"Kaina su PVM yra {kaina * 1.21} eurai")
#
# kaina_be_pvm = float(input("Įveskite NET sumą: "))
# pvm_skaiciuokle(kaina_be_pvm)
#
# Rosvaldo pvz.:
# def be_pvm(kaina):
#     return kaina * 1.21
#
# kaina_su_pvm = be_pvm(int(input("Iveskite kaina be PVM: ")))
# print("Kaina su PVM", + kaina_su_pvm)

class Uzduotis:
    def __init__(self, pavadinimas, aprasymas):
        self.pavadinimas = pavadinimas
        self.aprasymas = aprasymas
        self.atlikta = False

    def atlikimas(self):
        self.atlikta = True
        print(f"Uzduotis '{self.pavadinimas}' buvo atlikta")

    def info(self):
        return f" Pavadinimas: {self.pavadinimas}\n Aprasymas:{self.aprasymas}"


class TodoSarasas:
    def __init__(self):
        self.uzduociu_sarasas = []

    def prideti_uzduoti(self, pavadinimas, aprasymas):
        uzduotis = Uzduotis(pavadinimas, aprasymas)
        self.uzduociu_sarasas.append(uzduotis)

    def visos_uzduotys(self):
        if not self.uzduociu_sarasas:
            print("Uzduociu sarasas yra tuscias")
        for uzduotis in self.uzduociu_sarasas:
            print(uzduotis.info())

    def pazymeti_kaip_atlikta(self, pavadinimas):
        for uzduotis in self.uzduociu_sarasas:
            if uzduotis.pavadinimas == pavadinimas:
                uzduotis.atlikimas()
                return
        print(f"Uzduotis pavadinimu: '{pavadinimas}' nerasta")

todo_sarasas = TodoSarasas()

while True:
    print("\nPasirinkite veiksma:")
    print("1. Prideti uzduoti")
    print("2. Perziureti uzduotis")
    print("3. Pazymeti uzduoti kaip atlikta")
    print("4. Iseiti is uzduociu saraso")
    pasirinkimas = input("Prasome pasirinkti veiksma_>")

    if pasirinkimas == "1":
        pavadinimas = input("Iveskite uzduoties pavadinima_>")
        aprasymas = input("Iveskite uzduoties aprasyma_>")
        todo_sarasas.prideti_uzduoti(pavadinimas, aprasymas)
        print("Uzduotis prideta sekmingai!")
    elif pasirinkimas == "2":
        todo_sarasas.visos_uzduotys()
    elif pasirinkimas == "3":
        pavadinimas = input("Iveskite uzduoties pavadinima, kuria norite pazymeti kaip atlikta_>")
        todo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
    elif pasirinkimas == "4":
        print("Iseinama...")
        break
    else:
        print("Neteisingas pasirinkimas! Prasome bandyti dar karta!")