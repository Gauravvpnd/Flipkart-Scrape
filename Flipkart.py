import  pandas as pd
import  requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Description = []

url = "https://www.flipkart.com/search?q=laptop+under+40000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_8_na_na_na&as-pos=3&as-type=RECENT&suggestionId=laptop+under+40000&requestId=ace1ef4f-c37d-4426-8784-9f3d943b8990&as-backfill=on"
r = requests.get(url)


soup = BeautifulSoup(r.text, "lxml")
# print(soup)

np = soup.find("a", class_ = "ge-49M _2Kfbh8").get('href')
# print(np)
cnp = "https://www.flipkart.com" + np
# print(cnp)

url = cnp
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all('div', class_ = "_4rR01T")

for i in names:
    names = i.text
    Product_name.append(names)

# print(Product_name)

prices = soup.find_all("div", class_ = "_30jeq3 _1_WHN1")

for i in prices:
    name = i.text
    Prices.append(name)
# print(Prices)

des = soup.find_all('ul', "_1xgFaf")

for i in des:
    name = i.text
    Description.append(name)
# print(Description)

df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description})
print(df)

df.to_csv("E:/Scrapy/Prac/Flipkart Laptop under 40k.csv")