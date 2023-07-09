from netmiko import ConnectHandler

ip_list=['192.168.122.201','192.168.122.202','192.168.122.203']

for ip_add in ip_list:
    net_connect=ConnectHandler(device_type='cisco_ios',username='tarkesh',password='tarkesh',ip=ip_add)

    for vlan_no in range(2,4):
       config_commands=['no vlan '+str(vlan_no)]
       output=net_connect.send_config_set(config_commands)
       print(output)

    output=net_connect.send_command('show vlan')
    print(output)

