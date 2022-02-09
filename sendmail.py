import smptlib
import os

sender = "anything@hotmail.com"
recevier = ""
pass = ""

message = """\
            Subject : Lets Start 

            This is sagar, welcome!!
          """

server = smptlib.SMPT('smpt.office365.com', 587)
server.starttls()
server.login(sender, pass)
server.sendmail(sender, recevier, message)
server.quit()