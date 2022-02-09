import os
import yagmail
import time
from datetime import datetime as dt
import pandas

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
  mailObj.send(to=recevier, subject=subject, contents=cont)
  print("EMAIL SENT!")

def sendMessageWithInterval(mailObj, recvr, sub, cont, interval):
  while True:
      mailObj.send(to=recevier, subject=subject, contents=cont)
      print("EMAIL SENT!")
      time.sleep(interval)


def sendMessageAtCertainTime(mailObj, recvr, sub, cont, hr, min):
  while True:
    now = dt.now()
    if str(now.hour) == hr and str(now.minute) == min:
        mailObj.send(to=recevier, subject=subject, contents=cont)
        print("EMAIL SENT!")
        time.sleep(60)


def sendMessageMultipleRecivers(mailObj, recvrs, sub, cont):
  for recr in recvrs:
      mailObj.send(to=recr, subject=subject, contents=cont)
      print("EMAIL SENT!")
      time.sleep(2)
    
  


mailObj = getMailObj(sender, password)

sendMessage(mailObj, recevier, subject, content)

interval = 3
sendMessageWithInterval(mailObj, recevier, subject, content, interval)

hour = "21"
minute = "8"
sendMessageAtCertainTime(mailObj, recevier, subject, content, hour, minute)

# send multiple same mail to multiple email
df = pandas.read_csv('contacts.csv')
email_list = []
for index, row in df.iterrows():
  email_list.append(row['email'])
sendMessageMultipleRecivers(mailObj, email_list, subject, content)

# send email with attachments
contentWithAttachment = ["""
Here is the content of the email!!
How are you!!?
Thanks
Your Bot1
""", 'attachment.txt']
sendMessage(mailObj, recevier, subject, contentWithAttachment)


#send an email with modified attachments
def generate_file(filename, content):
  with open(filename, 'w') as file:
    file.write(str(content))
df1 = pandas.read_csv('billdetail.csv')
for index,row in df1.iterrows():
  name = row['name']
  amount = row['amount']
  recevier = row['email']
  generate_file(name, amount)
  subject = "Bill details"
  contents = [ f""" hey { name }, you have to pay { amount }
               Bill is attached!""",
               name,
             ]
  sendMessage(mailObj, recevier, subject, contents)
  
  












