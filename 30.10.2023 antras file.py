import requests
from bs4 import BeautifulSoup
import psycopg2

#200 OK
#301 -302 - File found / redirect http https:
# 403 Forbidden
# 404
# 500 Server error

# url = "https://aruodas.lt"
# response = requests.get(url)
#statusas turi buti 200 visad, reiskia galima kopint is puslapio info
# print(response.status_code)
# visa puslapi grazina
# print(response.content)

#selectinsim elementus

# url = "https://aruodas.lt"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
#
# #apacioje esanti eilute parodys tik teksta, be jokiu kodu, taip sakant nukopinam informacija is aruodo
# content_block = soup.find('div', class_= "top-three-adverts__wrapper").text.strip()
#
# print(content_block)

#reikai rasti keikvieno elemtno teksta, kaina ir pan
# def create_and_insert_flats():
#     #kuriam connectiona prie duomenu bezes:
#     connection = psycopg2.connect(
#         host = "localhost",
#         port = 5432,
#         database = "aruodas_informacija",
#         user="postgres",
#         password = "dangeliukas183729"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS aruodas_top(
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#     """
#
#     cursor.execute(create_table_query)
#     print("TAble created Successfully!")
#
#
#     url = "https://aruodas.lt"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content,"html.parser")
#     content_block = soup.select('div.top-three-adverts__wrapper div')
#
#     flats_data = []
#
#     for content in content_block:
#         try:
#             flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
#             flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()
#             print(flat_title, flat_price)
#             flats_data.append((flat_title, flat_price))
#
#         except AttributeError:
#             continue
#
#
#     connection.commit()
#
# create_and_insert_flats()
#   # print(flats_data)



# pavyzdys ne su try, o su if irgi galima padaryti


#kitas kodas
#

# def create_and_insert_flats():
#     #kuriam connectiona prie duomenu bezes:
#     connection = psycopg2.connect(
#         host = "localhost",
#         port = 5432,
#         database = "aruodas_informacija",
#         user="postgres",
#         password = "dangeliukas183729"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS aruodas_top(
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#     """
#
#     cursor.execute(create_table_query)
#     print("TAble created Successfully!")
#
#
#     url = "https://aruodas.lt"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content,"html.parser")
#     content_block = soup.select('div.top-three-adverts__wrapper div')
#
#     flats_data = []
#
#     for content in content_block:
#         try:
#             flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
#             flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()\
#                 .replace("€", "").replace(" ", "").split(sep="-")[0]
#             # print(flat_title, flat_price)
#             # flats_data.append((flat_title, flat_price))
#             insert_query = "INSERT INTO aruodas_top(flat_title, flat_price) VALUES (%s, %s)"
#             cursor.execute(insert_query, (flat_title, flat_price))
#
#         except AttributeError:
#             continue
#     print("Flats inserted successfully!")
#
#
#     connection.commit()
#
# create_and_insert_flats()
    # print(flats_data)




# kuriame patys su kitais objektais:

flats_data = []
def create_and_insert_flats():
    #kuriam connectiona prie duomenu bezes:
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "aruodas_informacija",
        user="postgres",
        password = "dangeliukas183729"
    )

    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS aruodas_uzsienis(
            id SERIAL primary key,
            flat_title VARCHAR(300),
            flat_price DECIMAL(10,2)
        )
    """

    cursor.execute(create_table_query)
    print("Table created Successfully!")


    url = "https://www.aruodas.lt/uzsienio-objektai/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    content_block = soup.select('div.project-list-item div')



    for content in content_block:
        try:
            flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
            flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip()\
                .split(sep="Kaina:")[1].replace(" ", "").replace("€", "")
            # print(flat_title, flat_price)
            # flats_data.append((flat_title, flat_price))
            insert_query = "INSERT INTO aruodas_uzsienis (flat_title, flat_price) VALUES (%s, %s)"
            cursor.execute(insert_query, (flat_title, flat_price))

        except AttributeError:
            continue
    print("Flats inserted successfully!")


    connection.commit()

create_and_insert_flats()










