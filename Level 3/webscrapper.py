from bs4 import BeautifulSoup
import requests

url = "https://www.aajtak.in/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')  

print(soup.title.text)
print('\n\n anchor tag title attributes \n\n')
data = soup.find_all('a')
for i in data:
    t = i.get('title')
    print(t)


