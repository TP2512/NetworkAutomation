import logging  
import getpass
import telnetlib
import pandas as pd

logging.basicConfig(filename="switch_conf.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 

logger.info("execution  strarts")
try:
   df=pd.read_excel(r"user_pass_serdetials.xlsx")
   logger.info("data data read successful")
except:
   logger.error("data loading failed")

logger.info("going into configrution")
try:
   for ind in df.index:
       HOST=df.serverip[ind]
       user=df.username[ind]
       password=df.password[ind]
       logger.info(f'Trying to connect switch IP: {HOST} with user:{user}')
       tn=telnetlib.Telnet(HOST)
       tn.read_until(b"Username:")
       tn.write(user.encode('ascii') +b"\n")
       if password:
          tn.read_until(b"Password: ")
          tn.write(password.encode('ascii') +b"\n")

       tn.write(b"enable\n")
       #tn.write(b"tarkesh\n")
       tn.write(b"conf t\n")
       for i in range(1,3):
           tn.write(b'vlan ' + str(i).encode() + b'\n')
           #tn.write(b'vlan '+str(i).encode()+'\n')
           tn.write(b'name Python_VLAN_'+str(i).encode()+ b'\n')
       tn.write(b"end\n")
       tn.write(b"exit\n")

       logger.info((tn.read_all().decode('ascii'))
except TypeError as te:
    logging.exception("Exception occurred: %s", str(te))

