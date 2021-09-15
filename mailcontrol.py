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

def get_latest_photo(files):
    lt = operator.lt
    if not files:
        return None
    now = time.time()
    latest = files[0], now - os.path.getctime(files[0])
    for f in files[1:]:
        age = now - os.path.getctime(f)
        if lt(age, latest[1]):
            latest = f, age
    return latest[0]

def BuildMessage(SensorNumber):
        # Routine to fetch the location and zone descriptions from the server  
        messagestr =''        
        #RecordSet = GetDataFromHost(6,[SensorNumber])
        #if PrintToScreen: print RecordSet
        #if RecordSet==False:
            #return  
        #zonedesc=RecordSet[0][0]
        #locationdesc = RecordSet[0][1]
        #messagestr="This is your requested picture"
        return messagestr


smtp_server="smtp.gmail.com"    # usually something like smtp.yourisp.com or smtp.gmail.com or smtp.mail.yahoo.com
smtp_user="cheesie67@gmail.com"      # usually the main email address of the account holder
smtp_pass="IluvSandy1996"
IMAP_SERVER='imap.gmail.com'
IMAP_PORT=993

emailr = []

try:
 M1=imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
 M=imaplib.IMAP4_SSL(IMAP_SERVER )
 M.login('cheesie67@gmail.com','IluvSandy1996')
 M.select()








 emailr=[]

 type, data = M.search(None, '(SUBJECT "statusb")' )

 Status = "b not armed"
 if os.path.isfile ("/etc/armed"):
    Status = "b armed"

 j = 0
 num=0
 for num in data[0].split():
    type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
    M.store( num, '+FLAGS', '\\Deleted' )
    message = data[0][1]
    i = 0
    while message[i]!='<':
       i=i+1

    
    message = message[i+1:]

    i = 0
    while message[i]!='>':
       i=i+1

    
    message = message[:i]
    emailr.append(message)
    
    
 i = 0
 while i < len(emailr):
                # Define email addresses to use
                addr_to   = emailr[i]
                addr_from = smtp_user
      
                photopath = '/tmp/*.jpg'
                files = glob.glob(photopath)
                latestphoto = get_latest_photo(files)
                msgtext = BuildMessage(SensorNumber);
                
                msg = MIMEMultipart() 
            
                addr_to   = emailr[i]
                addr_from = smtp_user
                msg['To']   = addr_to 
                msg['From'] = addr_from
                msg['Subject'] = Status 
                msg.preamble = 'Multipart message.\n'  
                part = MIMEText(msgtext) 
                msg.attach(part)
               
               


                s = smtplib.SMTP()#_SSL(smtp_server, 465)
                s.connect("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login(smtp_user,smtp_pass)
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
                #if PrintToScreen: print msg;
                i = i+1



                print "middle 1" 

                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                M.store( num, '+FLAGS', '\\Deleted' )






 emailr=[]

 type, data = M.search(None, '(SUBJECT "disarmb")' )


 j = 0
 num=0
 for num in data[0].split():
    
    os.system("sudo rm /etc/armed")

    type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
    M.store( num, '+FLAGS', '\\Deleted' )
    message = data[0][1]
    i = 0
    while message[i]!='<':
       i=i+1

    
    message = message[i+1:]

    i = 0
    while message[i]!='>':
       i=i+1

    
    message = message[:i]
    emailr.append(message)
    
    
 i = 0
 while i < len(emailr):
                # Define email addresses to use
                addr_to   = emailr[i]
                addr_from = smtp_user
      
                photopath = '/tmp/*.jpg'
                files = glob.glob(photopath)
                latestphoto = get_latest_photo(files)
                msgtext = BuildMessage(SensorNumber);
                
                msg = MIMEMultipart() 
            
                addr_to   = emailr[i]
                addr_from = smtp_user
                msg['To']   = addr_to 
                msg['From'] = addr_from
                msg['Subject'] = "b disarmed   " 
                msg.preamble = 'Multipart message.\n'  
                part = MIMEText(msgtext) 
                msg.attach(part)
               
               


                s = smtplib.SMTP()#_SSL(smtp_server, 465)
                s.connect("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login(smtp_user,smtp_pass)
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
                #if PrintToScreen: print msg;
                i = i+1



                print "middle 1" 

                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                M.store( num, '+FLAGS', '\\Deleted' )




 emailr=[]

 type, data = M.search(None, '(SUBJECT "armb")' )




 j = 0
 num=0
 for num in data[0].split():
    os.system("sudo touch /etc/armed")
    type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
    M.store( num, '+FLAGS', '\\Deleted' )
    message = data[0][1]
    i = 0
    while message[i]!='<':
       i=i+1

    
    message = message[i+1:]

    i = 0
    while message[i]!='>':
       i=i+1

    
    message = message[:i]
    emailr.append(message)
    
    
 i = 0
 while i < len(emailr):
                # Define email addresses to use
                addr_to   = emailr[i]
                addr_from = smtp_user
      
                photopath = '/tmp/*.jpg'
                files = glob.glob(photopath)
                latestphoto = get_latest_photo(files)
                msgtext = BuildMessage(SensorNumber);
                
                msg = MIMEMultipart() 
            
                addr_to   = emailr[i]
                addr_from = smtp_user
                msg['To']   = addr_to 
                msg['From'] = addr_from
                msg['Subject'] = "b armed   " 
                msg.preamble = 'Multipart message.\n'  
                part = MIMEText(msgtext) 
                msg.attach(part)
               
               


                s = smtplib.SMTP()#_SSL(smtp_server, 465)
                s.connect("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login(smtp_user,smtp_pass)
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
                #if PrintToScreen: print msg;
                i = i+1



                print "middle 1" 

                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                M.store( num, '+FLAGS', '\\Deleted' )





 print "middle"


 emailr=[]
 type, data = M.search(None, '(SUBJECT "snapb")' )

 j = 0
 for num in data[0].split():
    type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
    M.store( num, '+FLAGS', '\\Deleted' )
    message = data[0][1]
    i = 0
    while message[i]!='<':
       i=i+1

    print 'hello'    
    message = message[i+1:]

    i = 0
    while message[i]!='>':
       i=i+1

    
    message = message[:i]
    emailr.append(message)
    
   
 i = 0
 while i < len(emailr):
                # Define email addresses to use
                addr_to   = emailr[i]
                addr_from = smtp_user
      
                photopath = '/tmp/*.jpg'
                files = glob.glob(photopath)
                latestphoto = get_latest_photo(files)
                msgtext = BuildMessage(SensorNumber);
                
                msg = MIMEMultipart() 
            
                addr_to   = emailr[i]
                addr_from = smtp_user
                msg['To']   = addr_to 
                msg['From'] = addr_from
                msg['Subject'] = "Jedi Check" 
                msg.preamble = 'Multipart message.\n'  
                part = MIMEText(msgtext) 
                msg.attach(part)
                part = MIMEApplication(open(latestphoto,"rb").read())
                part.add_header('Content-Disposition', 'attachment', filename=latestphoto)
                msg.attach(part)


                s = smtplib.SMTP()#_SSL(smtp_server, 465)
                s.connect("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login(smtp_user,smtp_pass)
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
                #if PrintToScreen: print msg;
                i = i+1





                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                M.store( num, '+FLAGS', '\\Deleted' )
               



























 emailr=[]

 type, data = M.search(None, '(SUBJECT "dellogb")' )




 j = 0
 num=0
 for num in data[0].split():
    os.system("sudo rm /etc/doorswitch.log")
    type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
    M.store( num, '+FLAGS', '\\Deleted' )
    message = data[0][1]
    i = 0
    while message[i]!='<':
       i=i+1

    
    message = message[i+1:]

    i = 0
    while message[i]!='>':
       i=i+1

    
    message = message[:i]
    emailr.append(message)
    
    
 i = 0
 while i < len(emailr):
                # Define email addresses to use
                addr_to   = emailr[i]
                addr_from = smtp_user
      
                photopath = '/tmp/*.jpg'
                files = glob.glob(photopath)
                latestphoto = get_latest_photo(files)
                msgtext = BuildMessage(SensorNumber);
                
                msg = MIMEMultipart() 
            
                addr_to   = emailr[i]
                addr_from = smtp_user
                msg['To']   = addr_to 
                msg['From'] = addr_from
                msg['Subject'] = "doorswitch log deleted   " 
                msg.preamble = 'Multipart message.\n'  
                part = MIMEText(msgtext) 
                msg.attach(part)
               
               


                s = smtplib.SMTP()#_SSL(smtp_server, 465)
                s.connect("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login(smtp_user,smtp_pass)
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
                #if PrintToScreen: print msg;
                i = i+1



                print "middle 1" 

                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                M.store( num, '+FLAGS', '\\Deleted' )










 emailr=[]

 type, data = M.search(None, '(SUBJECT "getlogb")' )




 j = 0
 num=0
 for num in data[0].split():
    #os.system("sudo touch /etc/armed")
    type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
    M.store( num, '+FLAGS', '\\Deleted' )
    message = data[0][1]
    i = 0
    while message[i]!='<':
       i=i+1

    
    message = message[i+1:]

    i = 0
    while message[i]!='>':
       i=i+1

    
    message = message[:i]
    emailr.append(message)
    
    
 i = 0
 while i < len(emailr):
                # Define email addresses to use
                addr_to   = emailr[i]
                addr_from = smtp_user
      
                photopath = '/tmp/*.jpg'
                files = glob.glob(photopath)
                latestphoto = get_latest_photo(files)
                msgtext = BuildMessage(SensorNumber);
                
                msg = MIMEMultipart() 
            
                addr_to   = emailr[i]
                addr_from = smtp_user
                msg['To']   = addr_to 
                msg['From'] = addr_from
                msg['Subject'] = "door log report   "
                f = open ( '/etc/doorswitch.log', 'r')
                log = f.read()
                f.close()
                msgtext = log
 
                msg.preamble = 'Multipart message.\n'  
                part = MIMEText(msgtext) 
                msg.attach(part)
               
               


                s = smtplib.SMTP()#_SSL(smtp_server, 465)
                s.connect("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login(smtp_user,smtp_pass)
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
                #if PrintToScreen: print msg;
                i = i+1



                print "middle 1" 

                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                M.store( num, '+FLAGS', '\\Deleted' )





















 M.expunge()
 M.logout()



except Exception, e:
 print e
