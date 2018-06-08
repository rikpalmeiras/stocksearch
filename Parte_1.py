import requests
from bs4 import BeautifulSoup

page_nasdaq = requests.get("https://www.bloomberg.com/quote/CCMP:IND")
soup = BeautifulSoup(page_nasdaq.content, 'html.parser')
name_box_nasdaq = soup.find('h1', attrs={'class': 'name'})
nome_nasdaq = name_box_nasdaq.text.strip()
print(nome_nasdaq)
price_box_nasdaq = soup.find('div', attrs={'class':'price'})
preco_nasdaq = price_box_nasdaq.text
print(preco_nasdaq)

page_ny = requests.get("https://www.bloomberg.com/quote/NYA:IND")
soup = BeautifulSoup(page_ny.content, 'html.parser')
name_box_ny = soup.find('h1', attrs={'class': 'name'})
nome_ny = name_box_ny.text.strip()
print(nome_ny)
price_box_ny = soup.find('div', attrs={'class':'price'})
preco_ny = price_box_ny.text
print(preco_ny)

page_dj = requests.get("https://www.bloomberg.com/quote/INDU:IND")
soup = BeautifulSoup(page_dj.content, 'html.parser')
name_box_dj = soup.find('h1', attrs={'class': 'name'})
nome_dj = name_box_dj.text.strip()
print(nome_dj)
price_box_dj = soup.find('div', attrs={'class':'price'})
preco_dj = price_box_dj.text
print(preco_dj)

page_nk = requests.get("https://www.bloomberg.com/quote/NKY:IND")
soup = BeautifulSoup(page_nk.content, 'html.parser')
name_box_nk = soup.find('h1', attrs={'class': 'name'})
nome_nk = name_box_nk.text.strip()
print(nome_nk)
price_box_nk = soup.find('div', attrs={'class':'price'})
preco_nk = price_box_nk.text
print(preco_nk)

page_hk = requests.get("https://www.bloomberg.com/quote/HSI:IND")
soup = BeautifulSoup(page_hk.content, 'html.parser')
name_box_hk = soup.find('h1', attrs={'class': 'name'})
nome_hk = name_box_hk.text.strip()
print(nome_hk)
price_box_hk = soup.find('div', attrs={'class':'price'})
preco_hk = price_box_hk.text
print(preco_hk)
