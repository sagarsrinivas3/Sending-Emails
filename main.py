import os
import yagmail
import time

sender   = "sample.00.email@gmail.com"
recevier = "bigtvindia@gmail.com" #bigtvindia@gmail.com
password = os.environ['GMAILPASS']

subject = "This is the subject"

content = """
Here is the content of the email!!
How are you!!?
Thanks
Your Bot1
"""

def getMailObj(sndr, passwrd):
  mailObj = yagmail.SMTP(user=sndr, password=passwrd)
  return mailObj

def sendMessage(mailObj, recvr, sub, cont):
  mailObj.send(to=recevier, subject=subject, contents=content)
  print("EMAIL SENT!")

def sendMessageWithInterval(mailObj, recvr, sub, cont, interval):
  while True:
      mailObj.send(to=recevier, subject=subject, contents=content)
      time.sleep(interval)
      print("EMAIL SENT!")
    
  


mailObj = getMailObj(sender, password)
sendMessage(mailObj, recevier, subject, content)
interval = 3
sendMessageWithInterval(mailObj, recevier, subject, content, interval)









