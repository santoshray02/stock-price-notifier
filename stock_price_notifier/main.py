from bs4 import BeautifulSoup
import requests
import subprocess as s


def get_stock_price():
    url = "https://www.moneycontrol.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    bse_stock = requests.get(url, headers=headers)

    soup = BeautifulSoup(bse_stock.text, "html.parser")
    cp = soup.find('span', id='cp')
    chg = soup.find('span', id='chg')

    if cp:
        cp = cp.text
    else:
        cp = 0
    if chg:
        chg = chg.text
    else:
        chg = 0
    return (cp, chg)


def notify():
    result = get_stock_price()
    result = "Current Price\t:\t %s \nChange \t\t: \t%s %%" % result

    s.call(['notify-send', 'Stock Update for NIFTY 50', result])

notify()

