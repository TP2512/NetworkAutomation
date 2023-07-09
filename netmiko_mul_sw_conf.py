from netmiko import ConnectHandler

ip_list=['192.168.122.202','192.168.122.203']

for ip_add in ip_list:
    net_connect=ConnectHandler(device_type='cisco_ios',username='tarkesh',password='tarkesh',ip=ip_add)
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

