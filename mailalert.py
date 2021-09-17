import imaplib

import email

import time
import urllib2
import subprocess
global user
global password
global PrintToScreen 
global smtp_server
global smtp_user
global smtp_pass
global EmailPhoto
global SensorNumber
global SendEmails
import sys
import smtplib
import os, glob, time, operator
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from email.parser import HeaderParser

SensorNumber = 306



smtp_server="smtp.gmail.com"    # usually something like smtp.yourisp.com or smtp.gmail.com or smtp.mail.yahoo.com
smtp_user="cheesie67@gmail.com"      # usually the main email address of the account holder
smtp_pass="SubbyTubbies2016"
msg = MIMEMultipart() 
addr_to   = '4403155489@txt.att.net'
addr_from = smtp_user
msg['To']   = addr_to 
msg['From'] = addr_from
msg['Subject'] = 'JEDI ALERT!!!' 

s = smtplib.SMTP()#_SSL(smtp_server, 465)
s.connect("smtp.gmail.com",587)
s.ehlo()
s.starttls()
s.login(smtp_user,smtp_pass)
print 'mail 2'
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
#if PrintToScreen: print msg;



msg = MIMEMultipart()
addr_to   = '4403155488@txt.att.net'
addr_from = smtp_user
msg['To']   = addr_to
msg['From'] = addr_from
msg['Subject'] = 'JEDI ALERT!!!'

s = smtplib.SMTP()#_SSL(smtp_server, 465)
s.connect("smtp.gmail.com",587)
s.ehlo()
s.starttls()
s.login(smtp_user,smtp_pass)
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()

msg = MIMEMultipart()
addr_to   = 'cheesie67@gmail.com'
addr_from = smtp_user
msg['To']   = addr_to
msg['From'] = addr_from
msg['Subject'] = 'JEDI ALERT!!!'

s = smtplib.SMTP()#_SSL(smtp_server, 465)
s.connect("smtp.gmail.com",587)
s.ehlo()
s.starttls()
s.login(smtp_user,smtp_pass)
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()


