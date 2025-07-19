from easy_exchange_rates import API
from datetime import date
from datetime import date, timedelta
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
import requests

url = "https://www.investing.com/currencies/eur-usd-news"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

headlines = soup.findAll("a", attrs={"class":"block text-base font-bold leading-5 hover:underline sm:text-base sm:leading-6 md:text-lg md:leading-7"})
time = soup.findAll("time", attrs={"class":"ml-2"})

sender_email = "4einexchange@gmail.com"
sender_password = "khhp psic nkxq owab"
receiver_email = "rjdonato528@gmail.com"
subject = "Foreign Exchange Rate for EUR to USD"

msg = EmailMessage()

today = date.today()
yesterday = today - timedelta(days=5)

api = API()
df = api.get_exchange_rates(
  base_currency="EUR", 
  start_date=yesterday,
  end_date=today,
  targets=["USD","EUR"]
)

print("Latest News: \n")

for i in (headlines):
    print(f'{i.text}')
    print(f'{i['href']}\n')

rate = df.head(5)
text = f"Subject: {subject} {rate} \n Latest News: \n"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, receiver_email, text)

print("Email has been sent to " + receiver_email)
