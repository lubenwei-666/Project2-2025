import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
from date time import datetime

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# email configuration
from_email_addr = "1120828833@qq.com"
from_email_pass = "cexxoeygxwxiiiee"
to_email_addr = "1120828833@qq.com"

# check and reading the plant
for _ in range(4):
    if GPIO.input(channel):
        plant_status = "Water NOT needed"
    else:
        plant_status = "Please water your plant"

    # send the email
    msg = EmailMessage()
    msg.set_content(f"Plant status: {plant_status}")
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Plant Watering Status'

   
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print(f"Email sent: {plant_status}")
    server.quit()

    # send the time to check the plant
    time.sleep(6 * 60 * 60)
