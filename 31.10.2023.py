import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import psycopg2

###############PANDAS################
# import requests
# from bs4 import BeautifulSoup
# import psycopg2
#
# # flats_data = []
# # def create_and_insert_flats():
# #     #kuriam connectiona prie duomenu bezes:
# #     connection = psycopg2.connect(
# #         host = "localhost",
# #         port = 5432,
# #         database = "aruodas_informacija",
# #         user="postgres",
# #         password = "dangeliukas183729"
# #     )
# #
# #     cursor = connection.cursor()
# #
# #     create_table_query = """
# #         CREATE TABLE IF NOT EXISTS lemora_gipsas(
# #             id SERIAL primary key,
# #             flat_title VARCHAR(300),
# #             flat_price DECIMAL(10,2)
# #         )
# #     """
# #
# #     cursor.execute(create_table_query)
# #     print("Table created Successfully!")
# #
# #
# #     url = "https://lemora.lt/gipso-kartonas-profiliai/gipso-kartono-plokstes/813-impregnuota-plokste-knauf-green-gkbi#/1879-ilgis_mm-2000/1886-matmenys_gipso_sistemoms-125_x_1200"
# #     response = requests.get(url)
# #     soup = BeautifulSoup(response.content,"html.parser")
# #     content_block = soup.select('desktop-only')
# #
# #
# #
# #
# #         flat_title = content.find("h1", class_="name").text.strip()
# #         # flat_price = content.find("h3", class_="col-md-6").text.strip()\
# #         #     .split(sep="vnt.")[1].replace(" ", "").replace("€", "")
# #         print(flat_title)
# #         flats_data.append(flat_title)
# #         insert_query = "INSERT INTO aruodas_uzsienis (flat_title) VALUES (%s, %s)"
# #         cursor.execute(insert_query, (flat_title)
# #
# #
# #     print("Flats inserted successfully!")
# #
# #
# #     connection.commit()
# #
# # create_and_insert_flats()
#

############kodas be duombazes, tiesiog reiksme spausdina:############

# url = "https://lemora.lt/gipso-kartonas-profiliai/gipso-kartono-plokstes/813-impregnuota-plokste-knauf-green-gkbi#/1879-ilgis_mm-2000/1886-matmenys_gipso_sistemoms-125_x_1200"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
# #apacioje esanti eilute parodys tik teksta, be jokiu kodu, taip sakant nukopinam informacija is aruodo
# content_block = soup.find('div', class_= "pb-center-column pb-right-column col-xs-12 col-sm-12 col-md-6 product-main-right")
# # for content in content_block:
#
#
# # flat_title = content_block.select('div''"h1", class_="name").text.strip()
# flat_title = content_block.select_one("div.desktop-only h1").text.strip()
# # flat_title = content_block.select_one("div#desktop-only h1").text.strip() ## turi buti grotazymes, jeigu ID
# print(flat_title)



# data = {
#     "Vardas": ["Jonas", "Arturas", "Ignas", "Migle"],
#     "Amzius": [25, 28, 29, 30],
#     "Miestas": ["Vilnius","Klaipeda","Anyksciai","Plunge"]
# }
#
# df = pd.DataFrame(data)
#
# # vyresni_nei_25 = df[df["Amzius"] > 25]
# # grupavimas_pagal_miesta = df.groupby('Miestas').size()
# # df = df.sort_values(by='Amzius', ascending=False)
# # #naujo stulpelio pridejimas prie esancio
# # df["darbo stazas"] = [2,1,5,9]
# # #stulpelio istrinimas
# # df.drop(columns=['darbo stazas'], inplace=True)
# eiluciu_sk = df.shape[0]
# stulpeliu_sk = df.shape[1]
# print(f'Eiluciu skaicius {eiluciu_sk}, stulpeliu skaicius {stulpeliu_sk}')

# df = pd.read_csv("Sales_Records.csv")
# # #
# # df["Profit"] = df["Total Revenue"] - df["Total Cost"]
# #
# # df["Profit"] = df["Profit"].round(2)
# #
# # ##sukuria nauja faila:
# #
# # df.to_csv("Naujas Failas Sales Revenue.csv", index = False)
#
# #print("Bendras pelnas:", df["Profit"].sum(), df["Total Revenue"].sum(), df["Total Cost"].sum())
# #konvertuojam i kita duomenu tipa, i data ar skaiciu
# df["Order Date"] = pd.to_datetime(df["Order Date"])
# df["Ship Date"] = pd.to_datetime(df["Ship Date"])
# ##dt yra date time
# df["Dienu skirtumas:"] = (df["Order Date"] - df["Ship Date"]).dt.days
#
#
# print(df)


#### naujas kodas

# df = pd.read_csv("Sales_Records.csv")


# df["Order Date"] = pd.to_datetime(df["Order Date"])
# df["Ship Date"] = pd.to_datetime(df["Ship Date"])
# df["Units Sold"] = df["Units Sold"].astype(int) #formatvavimas is teksto i skaicius
# ##dt yra date time
# df["Dienu skirtumas:"] = (df["Order Date"] - df["Ship Date"]).dt.days


# print(df.isnull().sum()) #tikrinti tusicus laukelius
# print(df.isnull())

# surusiutoi profita mazejancia tvarka


# df = pd.read_csv("Sales_Records.csv")
# # # #
# df["Profit"] = df["Total Revenue"] - df["Total Cost"]
# # #
# df["Profit"] = df["Profit"].round(2)
#
# df["Margin on revenue"] = (df["Profit"] / df["Total Revenue"]) * 100
# # df["Margin on revenue"] = df["Margin on revenue"].round(2).astype(str) + "%" # pvz kaip prideti procentus
# df["Margin on revenue"] = df["Margin on revenue"].apply(lambda x:f"{x:.2f}%")  #pvz kaip prideti procentas nr 2
#
#
# # surusiavimas = df.sort_values(by="Profit", ascending=False)
#
# print(df)

## historgrama

# df = pd.read_csv("Sales_Records.csv")
#
# df["Profit"] = df["Total Revenue"] - df["Total Cost"]
#
# df["Profit"] = df["Profit"].round(2)
#
# plt.figure(figsize=(10,7))
#
# plt.hist(df["Profit"],bins = 10, edgecolor = "red")
# plt.title("Pelno histograma")
# plt.xlabel("Pelnas")
# plt.ylabel("Daznis")
# plt.savefig("Diagrama Pelnas.jpg")
# plt.show()

## su bar'ais padarom grafika

# df = pd.read_csv("Sales_Records.csv")
#
# plt.bar(["Unit Price", "Units Sold"],[df["Unit Price"].mean(),df["Units Sold"].mean()])
# plt.title("Vidutine kaina")
# plt.ylabel("Kaina")
# plt.show()




# df = pd.read_csv("Sales_Records.csv")
#
#
# df["Order Date"] = pd.to_datetime(df["Order Date"])
# df["Ship Date"] = pd.to_datetime(df["Ship Date"])
#
# df['Dienu skirtumas'] = (df["Ship Date"] - df["Order Date"]).dt.days
#
# plt.figure(figsize=(6,8))
# plt.hist(df['Dienu skirtumas'], bins = 10, edgecolor="black")
# plt.title('Dienu skirtumas')
# plt.xlabel('Dienu skirtumas')
# plt.ylabel('Uzsakymu kiekis')
# plt.show()

# Uzdavinys su temperaturomis, vidutine temperatura kiekvienos dienos:

# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
#
# weekdays = soup.find_all('span', class_= "date")
# temperatures = soup.find_all('span', class_= "big up-from-zero")[1::2]
#
# filter_weekdays = [weekday.get_text().split(",")[0] for weekday in weekdays]
# day_temperatures = []
# for temperature in temperatures:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# interval = min(len(filter_weekdays), len(day_temperatures))
#
# data = {"weekday": filter_weekdays,
#         "temperatures": day_temperatures
# }
#
# df = pd.DataFrame(data)
#
# plt.figure(figsize=(10,7))
# plt.bar(df["weekday"], df["temperatures"])
# plt.title("Temperaturos kaita per savaite")
# plt.ylabel("Temperatura C")
# plt.show()



# print(df["temperatures"].mean().round(2))

######## Uzdavinys su temperaturomis, kartu su nakties temperaturom vidurkis:

# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
#
# weekdays = soup.find_all('span', class_= "date")
# day = soup.find_all('span', class_= "big up-from-zero")[1::2]
# night = soup.find_all('span', class_= "big up-from-zero")[0::2]
#
# filter_weekdays = [weekday.get_text().split(",")[0] for weekday in weekdays]
# d_temperatures = []
# n_temperatures = []
#
# for temperature in day:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     d_temperatures.append(temp_value)
#
# for temperature in night:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     n_temperatures.append(temp_value)
#
#
# data = {"weekday": filter_weekdays,
#         "dtemperatures": d_temperatures,
#         "ntemperatures": n_temperatures
#
# }
#
# df = pd.DataFrame(data)
#
#
#
# df["Temperaturu vidurkis"] = (df["dtemperatures"] + df["ntemperatures"])/2
# df.drop(columns=['dtemperatures', 'ntemperatures'], inplace=True)
#
# print(df)
#
# plt.figure(figsize=(10,7))
# plt.bar(df["weekday"], df["Temperaturu vidurkis"])
# plt.title("Vidutine dienos temperature")
# plt.ylabel("Temperatura C")
# plt.show()
#

# $#############Coinbase puslapiu isspausdinimas:


data = []
for i in range(6):

    headers = {
    "User-Agent": "Chrome/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }
    url = f"https://www.coinbase.com/explore?page={i}"
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.content,"html.parser")



    table = soup.find('table', class_="cds-table-top40r1")

    if table:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 8:
                player_data = [column.text.strip() for column in columns]
                data.append(player_data)

    columns = ["Name", "Price", "Charts", "Change", "Market cap", "Trade", "Volume (24h)", "Supply"]


df = pd.DataFrame(data, columns = columns)


df.to_csv("Coinbase.csv", index=False)
print(df)

######    N.D.:

#####   charta, supply dropint, euru zenklus ir panasiai pasalint, sutvarkyt duomenis, kad surast didziausia maziausia, sugrupuot didejancia mazejancia tvarka,. paziuret, kiek per para kartu pasikeite duomenys is coinbase tinklapio