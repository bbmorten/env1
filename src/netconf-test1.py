'''
N9K-1(xmlin)# show interface 
<?xml version="1.0"?>
<nf:rpc xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:7.0.3.I7.3.:if_manager" message-id="1">
  <nf:get>
    <nf:filter type="subtree">
      <show>
        <interface/>
      </show>
    </nf:filter>
  </nf:get>
</nf:rpc>
]]>]]>

% Success
'''
# pip install ncclient
# https://pubhub.devnetcloud.com/media/netdevops-live/site/files/s01t03.pdf?0.5791515979650677

from ncclient import manager

host = "31.206.33.141"
port = 22
user = "btegitim"
pwd = "112233on2@18!"

device = manager.connect(host=host, port=port, username=user, password=pwd,
                         hostkey_verify=False, device_params={'name': 'nexus'},
                         allow_agent=False, look_for_keys=False)
get_filter = """
               <show>
               <hostname>
               </hostname>
               </show>
               """
nc_get_reply = device.get(('subtree', get_filter))
print(nc_get_reply.xml)
ns_map = {'mod': 'http://www.cisco.com/nxos:1.0:vdc_mgr'}
xml_rsp = nc_get_reply.data_ele.find('.//mod:hostname', ns_map)
value = xml_rsp.text
print(value)



device.close_session()
