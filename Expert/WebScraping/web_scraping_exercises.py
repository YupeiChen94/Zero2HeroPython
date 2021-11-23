import requests
import bs4

base_link = 'https://quotes.toscrape.com/page/{}/'

# Get HTML text
res = requests.get(base_link.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)

# Get list of authors on first page
authors = set()
for name in soup.select('.author'):
    authors.add(name.text)
# print(authors)

# Get list of all quotes on first page
quotes = set()
for quote in soup.select('.text'):
    quotes.add(quote.text)
# print(quotes)

# Extract top 10 tags shown on the top right of the homepage
tags = set()
for tag in soup.select('.tag-item'):
    tags.add(tag.select('a')[0].text)
# print(tags)

# Get all unique quthors on the website
u_authors = set()
page = 1
while True:
    print(f'Getting page {page}')
    res = requests.get(base_link.format(page))
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    authors = soup.select('.author')
    if not authors:
        print('No Authors')
        break
    else:
        page += 1
        for name in soup.select('.author'):
            u_authors.add(name.text)
print(u_authors)
