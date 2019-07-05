#---- Function to read device information from file -------------------
def read_device_info(devices_file):

    devices = [] # Create a list for all devices

    # Read in the devices from the file
    file = open(devices_file,'r')
    for line in file:

        device_info = line.strip().split(',') # Get device info into list
        print(device_info)
        # Create a device object with this data
        device = NetworkDevice(device_info[0],device_info[1])
                            

        devices.append(device) # add this device object to list


    file.close() # Close the file since we are done with it
    return devices


class NetworkDevice():
    
    
    def __init__(self,host='Router',ip='169.169.169.169'):
        self.hostname = host
        self.ip_addr = ip
        self.username = 'noname'
        self.password = 'no password'

    # Attribute : hostname, ip_addr, username, password
    def set_info(self,host,ip,user="cisco",password="cisco"):
        # host, ip, cisco, password method variable
        self.hostname = host
        self.ip_addr = ip
        self.username = user
        self.password = password


cihazlar = read_device_info('inputs/envanter.txt')
for item in cihazlar:
    print(item.hostname,item.ip_addr,item.username,item.password)


'''
dev1 = NetworkDevice()
print(dev1.hostname,dev1.ip_addr,dev1.username,dev1.password)
dev1.set_info('R1','10.1.1.1')
print(dev1.hostname,dev1.ip_addr,dev1.username,dev1.password)



dev2 = NetworkDevice()
dev2.set_info('R2','10.1.1.2','bulent','morten')
print(dev2.hostname,dev2.ip_addr,dev2.username,dev2.password)

dev3 = NetworkDevice('R3','10.2.2.2')
print(dev3.hostname,dev3.ip_addr,dev3.username,dev3.password)

'''







