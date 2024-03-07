from bs4 import BeautifulSoup
import requests
def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span",    class_='ccOutputRslt') 
  if rate is not None:
    rate = rate.get_text()
    print(rate)
  else:
    print("Currency not found")

get_currency('CAD', 'USD')