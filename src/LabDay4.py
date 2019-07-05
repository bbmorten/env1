from netmiko import Netmiko
import json

#---- Function to read device information from file -------------------
def read_device_info(devices_file):

    devices = [] # Create a list for all devices

    # Read in the devices from the file
    file = open(devices_file,'r')
    for line in file:

        device_info = line.strip().split(',') # Get device info into list
        print(device_info)
        # Create a device object with this data
        device = NetworkDevice(device_info[0],device_info[1],device_info[2],device_info[3],device_info[4])
                            

        devices.append(device) # add this device object to list


    file.close() # Close the file since we are done with it
    return devices


class NetworkDevice():
    
    
    def __init__(self,host,ip,username,password,deviceType):
        self.hostname = host
        self.ip_addr = ip
        self.username = username
        self.password = password
        self.deviceType = deviceType

    # Attribute : hostname, ip_addr, username, password, deviceType
    def set_info(self,host,ip,user="cisco",password="cisco",deviceType="ios"):
        # host, ip, cisco, password method variable
        self.hostname = host
        self.ip_addr = ip
        self.username = user
        self.password = password
        self.deviceType = deviceType

    def sendCommand(self,commandStr,fileName="noname"):
        
        my_device = {}
        my_device.update({"host":self.ip_addr})
        my_device.update({"username":self.username})
        my_device.update({"password":self.password})
        my_device.update({"device_type":self.deviceType})

        print(my_device)
        net_connect = Netmiko(**my_device)
        output = net_connect.send_command(commandStr) 

        # f = open(...)

        if fileName == "noname":
            fileName = "outputs/"+ self.hostname + ".cfg"
        with open(fileName,"w",encoding="utf-8") as f:
            f.write(output)

    def sendCommandJSONDict(self,commandStr):
        
        my_device = {}
        my_device.update({"host":self.ip_addr})
        my_device.update({"username":self.username})
        my_device.update({"password":self.password})
        my_device.update({"device_type":self.deviceType})

        print(my_device)
        net_connect = Netmiko(**my_device)
        output = net_connect.send_command(commandStr) 

        # f = open(...)
        return json.loads(output)
        

cihazlar = read_device_info('inputs/envanter.txt')

dict1 = cihazlar[1].sendCommandJSONDict("show interface | json")

print('{0:18}{1:8}{2:15}'.format("Interface Name","Status","IP Address"))

for k in dict1["TABLE_interface"]["ROW_interface"]:
    '''
    {
                "interface": "mgmt0", 
                "state": "up", 
                "admin_state": "up", 
                "eth_hw_desc": "GigabitEthernet", 
                "eth_hw_addr": "fc5b.394f.5b58", 
                "eth_bia_addr": "fc5b.394f.5b58", 
                "eth_ip_addr": "192.168.64.21", 
                ...
            }
    '''
    '''
    try: 
        print(k["interface"],k["state"],k["eth_ip_addr"])
    except Exception as errmsg:
        print(k["interface"],k["state"],"none")
    '''
    #print(k["interface"],k["state"],k.get("eth_ip_addr"))
    print('{0:18}{1:8}{2:15}'.format(k["interface"],k["state"],str(k.get("eth_ip_addr"))))
