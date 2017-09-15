#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("vvrms2215@gmail.com ","maha0203")
message = "hello"
server.sendmail("vvrms2215@gmail.com", "vvrms2215@gmail.com",message)
print("success")
server.quit()




	
