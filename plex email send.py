import re 
import os
import smtplib
from pprint import pprint

try:
	def atoi(text):
		return int(text) if text.isdigit() else text

	def natural_keys(text):
		return [ atoi(c) for c in re.split('(\d+)', text) ]

	fileList = sorted(os.listdir('/ FILE PATH HERE /'), key=natural_keys)
	fileList = "\n\n".join(fileList)

	fromaddr = '/ SENDING EMAIL ADDRESS HERE /'
	toaddrs = ['/ LIST OF RECEIPTIENT EMAILS HERE / ']
	subject = '/ SUBJECT HERE /'
	msg = 'Subject: {}\n\n{}'.format(subject, fileList)

	username = '/ EMAIL USERNAME HERE /'
	password = '/ EMAIL PASSWORD HERE /'

	server = smtplib.SMTP('/ EMAIL SMTP HERE /')
	server.starttls()
	server.login(username, password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
except Exception as e:
	print(e)