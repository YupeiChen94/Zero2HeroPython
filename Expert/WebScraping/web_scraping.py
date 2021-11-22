import requests
import bs4

result = requests.get('https://www.example.com/')
print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup)
site_title = soup.select('title')[0].getText()
site_paragrphs = soup.select('p')


