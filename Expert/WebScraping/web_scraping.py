import requests
import bs4

result = requests.get('https://www.example.com/')
print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup)
site_title = soup.select('title')[0].getText()
site_paragrphs = soup.select('p')

# Grabbing text from table of contents
result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(result.text, 'lxml')
toc_text = soup.select('.toctext')
# print(toc_text)
for item in toc_text:
    # print(item.text)
    pass

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')

computer = soup.select('.thumbimage')[0]['src']
print(computer)
image_link = requests.get(f"https:{computer}")
# print(image_link.content)
with open('my_computer_image.jpg', mode='wb') as f:
    f.write(image_link.content)




