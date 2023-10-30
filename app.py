import os
import shutil
# F = float(input("First number: "))
# S = float(input("Second number: "))
# sum = F + S
# print("Sum: " + str(sum));

#
# vardas = "Jonas"
# amzius = 30
# ar_jonas_moka_programuot = False
# ar_registruotas = False
# jono_pirkiniu_suma = 34.5
# print(type(amzius)) ###66
# print("Mano draugo vardas yra " + vardas + " jo amzius ", amzius, ar_jonas_moka_programuot, jono_pirkiniu_suma)

# susikuriam lista. listas(array) masyvas = []
# vaisiai = ["Obuolys0", "Arbuzas1", "Bananas2", "Kriause3"]
# print(type(vaisiai))
# print(vaisiai[0])
# ilgis = len(vaisiai)
# print(ilgis)
# print(vaisiai[1:2]) #pirmas elementas nepatenka, antras patenka, dar yra du dvitaskiai :: bus kas antra, trecias. yra dar prie skaiciuko minusas -
# pridedame_vaisiu = vaisiai.append("Melionas4") #pridedam nauja pavadinima i list'a 'vaisiai'. i saraso gala, o insert i nurodyta indeksa
# print(vaisiai)
# vaisiai.insert(0,"Melionas")
# keiciam_reiksme = vaisiai[1] = "Kivis"
# indeksas = vaisiai.index("Arbuzas1") #parasom, koks indeksas yra tam tikro elemento
# vaisiai.remove("Bananas2") #istrina reiksme is saraso
# vaisiai.pop(2) #ismeta reiksme is listo pagal indeksa
#taip pat i tuscia sarasa galime rpideti reiksmes
# print(vaisiai[2])
# print(vaisiai)


#dictionary - strukture = my_dict = {key1:value1, key2:value2}
# zodynas = {
#     "Vardas": "Jonas",
#     "Amzius": 30,
#     "Miestas": "Vilnius"
# }
# print(zodynas["Vardas"])
# zodynas["ar_studentas"] = True #pridejimas naujos kategorijos ir jos reiksmes
# del zodynas["Miestas"] #iraso pasalinimas
# print(zodynas)

# cia zodynas, kai indeksu nera, o tik pagla vardus galima printi'inti reiksme'
#
# studentai = {
# "Jonas":{
#     "Amzius": 32,
#     "Miestas": "Kaunas",
#     "Profesija": "Inzinierius"
#
# },
# "Ona":{
#     "Amzius": 25,
#     "Miestas": "Klaipeda",
#     "Profesija": "Gydytoja"
# },
# "Antanas":{
#     "Amzius": 46,
#     "Miestas": "Vilnius",
#     "Profesija": "Mokytojas"
# }
#
# }
# print(studentai["Jonas"]) #kai norim konkrecia reiksme pamatyt

#sarasas: apacioje bus blokai su indeksu, issaukinesim blokus su indeksu

# studentai = [
# {
#     "Vardas": "Jonas",
#     "Amzius": 32,
#     "Miestas": "Kaunas",
#     "Profesija": "Inzinierius"
#
# },
# {
#     "Vardas": "Ona",
#     "Amzius": 25,
#     "Miestas": "Klaipeda",
#     "Profesija": "Gydytoja"
# },
# {
#     "Vardas": "Antanas",
#     "Amzius": 46,
#     "Miestas": "Vilnius",
#     "Profesija": "Mokytojas"
# }
#
# ]
#
# # naujo studento pridejimas:
#
# naujas_studentas = {
#     "Vardas": "Antanas",
#     "Amzius": 100,
#     "Miestas": "Taurage",
#     "Profesija": "Stalius"
# }
# studentai.append(naujas_studentas)
#
# print(studentai[3]) #kai norim konkrecia reiksme pamatyt, bet jau su indeksu


# if salyga: jusu veiksmai; jeigu norim priesingos reiksmes, tai tada rasom else lygiai taip pat, kaip ir if;

# amzius = 8 #and arba or galima naudoti
# if amzius >= 18:
#     print("Asmuo yra pilnametis")
# elif amzius > 13:
#     print("Asmuo yra paauglys")
# else:
#     print("Asmuo yra vaikas")
#

# vaisiai = ["bananas", "kivis", "obuolys"]
#
# if "kivis" in vaisiai:
#     print("Vaisius kivis")
# elif not "kivis" in vaisiai:
#     print("Vaisius nerastas")
# else:
#     print("Vaisiu sarasas tuscias")


# vaisiai = ["aaa"]
#
# if not vaisiai: #tikrina ar yra sarase elementu, siuo atveju bus False reiksme, nes nera sarase elementu.
#     print("Vaisiu sarasas tuscias")
# elif "kivis" in vaisiai:
#     print("Vaisius kivis")
# else:
#     print("Vaisiu kivis nerastas, taciau sarase yra elementu")


# if'as if'e:

# age = 18
# has_id = True
#
# if age >= 18:
#     if has_id:
#         print("Gali balsuoti")
#     else:
#         print("Jums reikia asmens tapatybes korteles")
# else:
#     print("Jums dar negalima balsuoti")


# print(f'Mano parduotuves prekiu kategorijos "{prekiu_tipai}" is kuriu galite rinktis') # formatavimas

# prekiu_kategorijos = ['Vaisiai', 'Mesa', 'Darzoves']
#
# prekes = {
#     'Vaisiai':['Obuoliai', 'Bananai'],
#     'Mesa':['Kiauliena', 'Vistiena'],
#     'Darzoves':['Bulves', 'Pomidorai']
# }
# # norime rasti prekes kategorija 'Mesa' ir prekes 'Vistiena';
# norima_kategorija = 'Mesa'
# norima_preke = 'Vistiena'
#
#
# if norima_kategorija in prekiu_kategorijos:
#     if norima_preke in prekes[norima_kategorija]:
#         print(f"Parduotuveje yra {norima_preke}")
#     else:
#         print(f"Parduotuveje nera {norima_preke}")
# else:
#         print(f"Parduotuveje nera prekiu kategorijos: {norima_kategorija}")

# if norima_kategorija in prekiu_kategorijos:
#             if norima_preke in prekes[norima_kategorija]:
#                 print(f"Parduotuveje yra {norima_preke}")
#             if needed_item not in items{needed_category}
#
#             else:
#                 print(f"Parduotuveje nera {norima_preke}")
# #         else:
# #             print(f"Parduotuveje nera prekiu kategorijos: {norima_kategorija}")
#
# # 1. dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi:
#
# #
# sarasas = [
# {
#     "Vardas": "Antanas",
#     "Amzius": 5
# },
# {
#     "Vardas": "Petras",
#     "Amzius": 20
# },
# {
#     "Vardas": "Gediminas",
#     "Amzius": 14,
# }
#
# ]
#
# # print(type(zmones))
#
# # 2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi: "nepilnametis", "suaugęs" arba "vaikas" (jei amžius yra 18).
#
# zmogus = sarasas[0]
#
# if zmogus['Amzius'] > 18:
#     print(f' Sis zmogus {zmogus["Vardas"]} yra suauges')
# if zmogus['Amzius'] == 18:
#     print(f'Sis zmogus {zmogus["Vardas"]} yra paauglys')
# if zmogus['Amzius'] < 18:
#     print(f' Sis zmogus {zmogus["Vardas"]} yra nepilnametis');
#
# # print(f' Sis zmogus {zmones[0]['Vardas']}


# 2 užduotis:
# 1 dalis: Sukurkite žodyną su darbuotojo informacija(Vardas, atlyginimas,pareigos);
# 2.dalis: Pagal darbuotojo pareigas (jei jis yra "inžinierius"), padidinkite jo atlyginimą 10%. Jei jis nėra "inžinierius", palikite atlyginimą nepakeistą.

# if salyga: jusu veiksmai; jeigu norim priesingos reiksmes, tai tada rasom else lygiai taip pat, kaip ir if;
#
# darbuotojas = {
#     "Vardas": "Tomas",
#     "Atlyginimas": 2200,
#     "Pareigos": "inzinierius"
# }
#
# if darbuotojas["Pareigos"] == "inzinierius":
#     #padidinti 10 proc. atlyginima
#     #ilgesnis uzrasymas
#     # darbuotojas["Atlyginimas"] = darbuotojas["Atlyginimas"] * 1.10
#     #trumpesnis uzrasymas
#     # darbuotojas["Atlyginimas"] *= 1.10
#
# # du lygu == lyginimas, o = yra priskyrimas
#
# print(darbuotojas)

# 3 užduotis:
# 1 dalis: Sukurkite sąrašą su knygų informacija(Pavadinimas, išleidimo metai);
# 2 dalis: Suraskite norimos knygos metus pagal vartotojo įvesti;


# knygos = [
#     {"pavadinimas": "Haris Poteris", "isleidimo metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo metai": 1851},
#     {"pavadinimas": "Metai", "isleidimo metai": 2002}
# ]
#
# knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))
#
#
# knyga = knygos[2]
#
# if knyga["isleidimo metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knyga['pavadinimas']}")
# if knyga["isleidimo metai"] != knyga_pagal_ieskomus_metus:
#     print("Tokia knyga nerasta")
#

# knygos = [
#     {"pavadinimas": "Haris Poteris", "isleidimo_metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo_metai": 1851},
#     {"pavadinimas": "Metai", "isleidimo_metai": 2002}
# ]
#
#
#
# try:
#     knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))
#
#     if knygos[0]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
#     elif knygos[1]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[1]['pavadinimas']}.")
#     elif knygos[2]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[2]['pavadinimas']}.")
#     else:
#         print(f"Deja, knygų išleistų {knyga_pagal_ieskomus_metus} metais nėra.")
# except ValueError:
#     print("Blogas ivesties formatas")


# Importuojamos bibliotekos VISADA rasomos pirmose eilutese
# Patarimas: kiekviena diena, kai dirbsim su pythonu, nedirbkim ant to paties failo.

# dabartinis_katalogas = os.getcwd()
# # print(dabartinis_katalogas)
#
# # norimas_aplankas = input("Iveskite aplanko pavadinima, kurio turini norite matyti_> ")
# naujas_katalogas = input("Prasom nurodyti katalogo lokacija_>")
#
#
# try:
#     keiciam_kataloga = os.chdir(naujas_katalogas)
#     if os.getcwd() == naujas_katalogas:
#         print(f"Darbinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     #bandome gauti aplanko turini;
#     turinys = os.listdir(naujas_katalogas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print(f"Deja aplankas '{naujas_katalogas}' nerastas")


# EXTENSION_MAP ={
#     '.jpg': "Images",
#     '.jpeg': "Images",
#     '.png': "Images",
#     '.gif': "Images",
#     '.pdf': "Documents",
#     ".txt": "Documents",
#     '.json': "Json files",
#     '.py': "Python scripts"
# }
#
# filename = input("Please insert the name of the file you want to organize_> ")
#
# file_extension = os.path.splitext(filename)[1]
#
#
#
# try:
#     if os.path.exists(filename) and file_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[file_extension]
#
#         # create directory if it doesn't exist
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#
#         # move the file
#         shutil.move(filename, os.path.join(directory_name, filename))
#         print(f"{filename} has been moved to {directory_name}")
#     else:
#         print("The file does not exist or its extension is not recognized")
# except FileNotFoundError:
#     print(f"Error: {filename} was not found")
# except PermissionError:
#     print(f"Error: You don't have permissions to move '{filename}'")




