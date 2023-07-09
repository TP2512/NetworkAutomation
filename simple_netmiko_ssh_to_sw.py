from netmiko import ConnectHandler

isov_l2={
'device_type':'cisco_ios',
'ip':'192.168.122.201',
'username':'tarkesh',
'password':'tarkesh'
}

net_connect=ConnectHandler(**isov_l2)

output=net_connect.send_command('show vlan')
output=net_connect.send_command('show ip int br')
print(output)
config_commands = ['int loop 0','ip address 1.1.1.1 255.255.255.0']
output=net_connect.send_config_set(config_commands)
print(output)

for vlan_no in range(2,4):
   config_commands=['vlan '+str(vlan_no),'name Python_VLAN_'+str(vlan_no)]
   output=net_connect.send_config_set(config_commands)
   print(output)

output=net_connect.send_command('show vlan')
print(output)

