from bs4 import BeautifulSoup
import requests


#headers = {'User-Agent': 'Mozilla/5.0'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#headers = {'User-Agent':'Chrome/66.0.3359.181'}
#headers = {'User-Agent':'Mozilla/5.0', 'referer' : 'http://www.naver.com'}

url = 'https://www.yanolja.com/hotel'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else : 
    print(response.status_code)
