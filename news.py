from bs4 import BeautifulSoup
import requests

url = "https://www.investing.com/currencies/eur-usd-news"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

headlines = soup.findAll("a", attrs={"class":"block text-base font-bold leading-5 hover:underline sm:text-base sm:leading-6 md:text-lg md:leading-7"})
time = soup.findAll("time", attrs={"class":"ml-2"})

print("Latest News: \n")
for i in (headlines):
    print(f'{i.text}')
    print(f'{i['href']}\n')

