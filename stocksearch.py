import requests
from bs4 import BeautifulSoup

def bolsa(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    name_box = soup.find('h1', attrs={'class': 'name'})
    nome = name_box.text.strip()
    print(nome)
    price_box = soup.find('div', attrs={'class':'price'})
    preco = price_box.text
    print(preco)
bolsa("https://www.bloomberg.com/quote/CCMP:IND")
bolsa("https://www.bloomberg.com/quote/NYA:IND")
bolsa("https://www.bloomberg.com/quote/INDU:IND")
bolsa("https://www.bloomberg.com/quote/NKY:IND")
bolsa("https://www.bloomberg.com/quote/HSI:IND")
