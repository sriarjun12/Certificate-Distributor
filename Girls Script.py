import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageDraw, ImageFont

def sendMail(Na,M,S,P):
    font = ImageFont.truetype('ProductSans.ttf', size=100)
    color = 'rgb(54, 54, 54)'
    W, H = (2000, 1500)
    N=Na
    image = Image.open('tempte.png')
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(N, font=font)
    draw.text(((W - w) / 2, (H - h) / 2), N, fill=color, font=font)
    image.save(N + ' GSC.png')
    FileName = N+' GSC.png'
    img_data = open(FileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Embedded Machine Learning'
    msg['From'] = S
    msg['To'] = M
    text = MIMEText('''Hello,
Hope you and your loved ones are safe and doing well. Thank you for registering to #Embedded machine learning webinar by Navaneeth Malingan. On behalf of Girlscript coimbatore, we thank all participants for showing interest in learning new things.


Please , find your certificate of participation attached with this mail.
Expecting your presence in all our upcoming events. 

Upcoming Event Details :
Bootcamp on Machine Learning for 7 days from the basics - https://bit.ly/gscbe27

Do register and enjoy learning with us !

Regards,
Girlscript Coimbatore.''')
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(FileName))
    msg.attach(image)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(S, P)
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.quit()

Send=input("Enter Email : ")
passw=input("Enter Password : ")
name=open("Name", "r").read().splitlines()
mail=open("Mailid","r").read().splitlines()

for i,j in zip(name,mail):
    sendMail(i,j,Send,passw)