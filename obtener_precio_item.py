import bs4
import requests
from currency_converter import CurrencyConverter

fees = 0

converter = CurrencyConverter()

def get_precio(nombre_item):
    url = "https://csgoskins.gg/items/" + nombre_item

    r = r = requests.get(
        url,
        headers = {
            'User-Agent': 'Popular browser\'s user-agent',
        }
    )

    c = r.content.decode('utf-8')
    soup = bs4.BeautifulSoup(c, "html.parser")

    divs = soup.find_all( 'div' , {'class': "bg-gray-800 rounded shadow-md relative flex items-center flex-wrap my-4 border-2 border-blue-700 pt-8 pb-4"})

    precio = divs[0].text.replace("\n", "").replace(" ", "").replace("from", "/").split("/")[-1].replace("€", "").replace("ViewOffer", " ").replace("$", "")

    return converter.convert(float(precio)*(1-fees), "USD", "EUR")
