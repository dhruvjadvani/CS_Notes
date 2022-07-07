import schedule
import time
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
page = requests.get(url)
data = page.json()

def fetch_bitcoin():
    print("Getting Bitcoin Price...")
    result = data['bpi']['USD']
    print(result)

def fetch_bitcoin_by_currency(x):
    print("Getting Bitcoin Price...", x)
    result = data['bpi'][x]
    print(result)

schedule.every(5).seconds.do(fetch_bitcoin)
schedule.every(5).seconds.do(fetch_bitcoin_by_currency,'GBP')
schedule.every(5).seconds.do(fetch_bitcoin_by_currency,'EUR')

while True:
    schedule.run_pending()
    time.sleep(1)



