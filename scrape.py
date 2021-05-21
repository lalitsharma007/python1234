import requests
from bs4 import  BeautifulSoup
import smtplib
url='https://www.amazon.in/Rustic-Art-Concentrate-Anti-Bacterial-Anti-Fungal/dp/B07R5KB8PM/ref=sr_1_5?crid=S8GLQLSJGN3X&dchild=1&keywords=rustic+art+facewash+neem+basil&qid=1591432511&sprefix=rusti%2Caps%2C483&sr=8-5'
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
def Price_change():
    page = requests.get(url, headers=headers)
    soup =BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    convertte_price = float(price[2:6])


    if (convertte_price <  300):
            send_mail()


    print(convertte_price)
    # print(price)
    print(title.strip())

    if(price > 300):
            send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("lalits429@gmail.com", 'ouvmlxdmhbhazjde')
    subject = " price girr gya ja ke order kr "
    body = 'https://www.amazon.in/Rustic-Art-Concentrate-Anti-Bacterial-Anti-Fungal/dp/B07R5KB8PM/ref=sr_1_5?crid=S8GLQLSJGN3X&dchild=1&keywords=rustic+art+facewash+neem+basil&qid=1591432511&sprefix=rusti%2Caps%2C483&sr=8-5'
    msg= f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'lalits429@gmail.com',
        'collageid1128@gmail.com',
        msg
    )
    print("hey email have been send")
    server.quit()
Price_change()










