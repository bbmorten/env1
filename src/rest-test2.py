import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('btegitim', '112233on2@18!')
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_conf",
            "chunk": "0",
            "sid": "1",
            "input": "interface ethernet1/16 ; no switchport ; ip address 1.15.1.1 255.255.255.0",
            "output_format": "json"
        }

    }
    url = 'http://31.206.33.141:8443/ins'

    response = requests.post(url, data=json.dumps(payload),
                             headers=headers, auth=auth)

    print(response.status_code)

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show interface ethernet1/16 ",
            "output_format": "json"
        }
    }

    response = requests.post(url, data=json.dumps(payload),
                             headers=headers, auth=auth)

    print(response.text)