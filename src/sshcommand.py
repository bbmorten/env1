from netmiko import Netmiko
#from getpass import getpass

my_device = {
    "host": "31.206.33.141",
    "username": "btegitim",
    "password": "112233on2@18!",
    "device_type": "cisco_nxos",
}

net_connect = Netmiko(**my_device)

output = net_connect.send_command("show interface | json-pretty")
print(output)
print(type(output))
net_connect.disconnect()

with open(my_device['host']+'.cfg',"w",encoding="utf-8") as f:
    f.write(output)