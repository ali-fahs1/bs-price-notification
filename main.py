import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import time


url = requests.get("https://books.toscrape.com/catalogue/higherselfie-wake-up-your-life-free-your-soul-find-your-tribe_957/index.html")
soup = BeautifulSoup(url.content,"html.parser")
results = soup.find('div',class_="col-sm-6 product_main").find('p',class_='price_color').text[1:]
result = float(results)
print(result)

if result < 100:
  print("start")
  smt = smtplib.SMTP('smtp.gmail.com',587)
  smt.ehlo()
  smt.starttls()
  smt.login("devlop313@gmail.com",'pass')
  smt.sendmail("devlop313@gmail.com",'aliahmadfahs17@gmail.com',
              f"subject:price notification\n\n the drop to {result}")
  
  

