  
#!/usr/bin/env python
"""
rfthermtest.py 1.00 PrivateEyePi RF Temperature Test Program
---------------------------------------------------------------------------------
 Works conjunction with host at www.privateeyepi.com                              
 Visit projects.privateeyepi.com for full details                                 
                                                                                  
 J. Evans October 2013       
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 

 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                                       
                                                                                  
 Revision History                                                                  
 V1.00 - Release                                                             
 -----------------------------------------------------------------------------------
"""
import datetime
import os
import serial
import time
import sys
from time import sleep
now = datetime.datetime.now()
def main():
        # declare to variables, holding the com port we wish to talk to and the speed
   while True:
        port = '/dev/ttyAMA0'
        baud = 9600
        
        # open a serial connection using the variables above
        ser = serial.Serial(port=port, baudrate=baud)
        
        # wait for a moment before doing anything else
        sleep(0.2)    
        llapMsglast =''
        #print "Please wait max 5 mins for the temperature transmitter to transmit..."
        start_time = time.time()
        while True:
             #try:
                elapsed_time = time.time()-start_time
                    # Poll for changes to RF settings
                if (elapsed_time > 1):
                   start_time = time.time()
                  
                        
                while ser.inWaiting():
                        # read a single character
                        char = ser.read()
                        # check we have the start of a LLAP message
                        if char == 'a':
                                # start building the full llap message by adding the 'a' we have
                                llapMsg = 'a'
                                
                                # read in the next 11 characters form the serial buffer
                                # into the llap message
                                llapMsg += ser.read(11)
                                if llapMsg != llapMsglast:
                                   llapMsglast = llapMsg
                                # now we split the llap message apart into devID and data
                                   devID = llapMsg[1:3]
                                   data = llapMsg[3:]
                                   now = datetime.datetime.now()
                                   open("/etc/doorswitch.log","a+b").write("Device Number : " +str( devID) )
                                   open("/etc/doorswitch.log","a+b").write(data+'  ')
                                   open("/etc/doorswitch.log","a+b").write(str(now)+'\n')
                                   print 'jedi track'
                                   os.system("sudo rm /etc/tmp.log")

                                   os.system("sudo rm /etc/dummy.log")
                                   os.system("sudo touch /etc/"+str(devID)+".log")
   				   open("/etc/" + "dummy" + ".log","a+b").write(str(devID)+' '+data +' ')
                                   open("/etc/" + "dummy" + ".log","a+b").write(str(now)+'\n')
                                   
				   if os.path.isfile("/etc/armed"):
				   	open("/etc/dummy.log", "a+b").write("alarm\n\n")           

                                   os.system("sudo cat /etc/dummy.log /etc/" + str(devID) + ".log >/etc/tmp.log")
                                   os.system("sudo rm /etc/" + str(devID) + ".log")
			           os.system("sudo mv /etc/tmp.log /etc/" + str(devID) + ".log")
                                   os.system("sudo rm /etc/tmp.log")

                                   os.system("sudo cat /etc/dummy.log /etc/doorswitch.log >/etc/tmp.log")
                                   os.system("sudo rm /etc/doorswitch.log")
         		           os.system("sudo mv /etc/tmp.log /etc/doorswitch.log")
                                   os.system("sudo rm /etc/tmp.log")

				   os.system("sudo rm /etc/dummy.log")
				   if os.path.isfile("/etc/armed"):
                                      os.system("sudo python /etc/mailalert.py")
                                  
                                      
                                      
				      open("/etc/doorswitch.log","a+b").write("Alarm!!!!!!!!!!!!!!!!!\n\n")     
                                      i=0
                                      while i<50:
                                         i=i+1
                                         #os.system("aplay /home/police_s.wav>tmp.out")
                                      if data.startswith("START"):
                                         print 'Start error'
                                   #ser.write('aAAWAKE-----' )
                                   #ser.write('aAAINTVL000x' )
                                   #ser.write('aAA REBOOT--' )
                                   ser.write('a81WAKE-----' )
				   sys.exit(0)
				#print "Device Number : " + devID
                                #print "Temperature data : " + data

if __name__=="__main__":
    main()                              

	 



   
   

