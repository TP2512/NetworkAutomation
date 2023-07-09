from netmiko import ConnectHandler
import logging

logging.basicConfig(filename="mul_sw_conf.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

ip_list=['192.168.122.201','192.168.122.202','192.168.122.203']
logger.info(f'list of IPs: {ip_list}')
logger.info(f'starting configrution')

class Switch_Configurtion:
    def __init__(self,ip_add,username,password):
        self.ip_add=ip_add
        self.username=username
        self.password=password

    def connect_switch(self):
        net_connect=ConnectHandler(device_type='cisco_ios',username=self.username,password=self.password,ip=self.ip_add)
        return net_connect

    def execute_conf_get_result(self,obj,commands):
        output=obj.send_config_set(config_commands)
        return output


sw_conf_obj=Switch_Configurtion(username='tarkesh',password='tarkesh',ip_add='192.168.122.201')
sw_conn_obj=sw_conf_obj.connect_switch()
logger.info(f'object has been created')
config_commands=['vlan 2','name Python_Vlan_2']
output=sw_conf_obj.execute_conf_get_result(sw_conn_obj,config_commands)
logger.info(f'commands execution starts')
print(output)
