
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:52:06 2020

@author: Harsh
"""
import smtplib
import config
import random

def send_email(subject,msg):
    email = input("enter sender's email")
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(config.email_address,config.password)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(config.email_address,email, message)
        server.quit()
        print("success")
    except :
        print("email failed")


m=random.randint(1000,10000)        
subject = "test2 subject"
msg = str(m) 

send_email(subject, msg)        
        
        
        
        