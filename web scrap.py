import requests
from bs4 import BeautifulSoup
url="https://www.zyte.com/learn/what-is-web-scraping/"
response=requests.get(url)
if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.praser');
    page_text =soup.get_text()
    links=[a['href']for a in soup.find_all('a',href=True)]
    images=[img['src']for img in soup.find_all('src',src=True)]

print('page text:')
print(page_text)
print('\nlinks')
for link in links:
    print(link)
print('\nimages')
for image in images:
    print(image)
else:
    print(f"Failed to retrive the web page.status code('response.status_code')")

