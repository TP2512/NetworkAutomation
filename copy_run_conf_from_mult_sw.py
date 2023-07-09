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
   #df=pd.read_excel(r"user_pass_serdetials.xlsx")
   df=pd.read_csv(r"sw_ip_user_passwd.csv")
   logger.info("data read successful")
   logger.info(f"user details is {df}")
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

       #tn.write(b"enable\n")
       #tn.write(b"tarkesh\n")
       #tn.write(b"conf t\n")
       tn.write(b"terminal length 0\n")
       tn.write(b'show run\n')
       logger.info(f'getting running conf')
       tn.write(b"exit\n")

       logger.info(tn.read_all().decode('ascii'))
except TypeError as te:
   logging.exception("Exception occurred: %s", str(te))
except OSError as oe:
   logging.exception(f"Exception occurred: %s.Plz check IP connection {HOST}",str(oe))
finally:
   logger.info("execution completed")
