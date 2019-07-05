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
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show version",
            "output_format": "json"
        }
    }
    url = 'http://31.206.33.141:8443/ins'

    response = requests.post(url, data=json.dumps(payload),
                         headers=headers, auth=auth)

    print(response.status_code)
    print(response.text)
    dict1 = json.loads(response.text)
    print(dict1["ins_api"]["outputs"]["output"]["body"]["rr_sys_ver"])