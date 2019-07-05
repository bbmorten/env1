import json

if __name__ == "__main__":
    facts = {
        'hostname': 'nxosv',
        'os': '7.3',
        'location': 'San_Jose'
    }
    # print facts dictionary
    print(facts)
    # print facts as a JSON string
    print(json.dumps(facts, indent=4))
    # print a specific value of key
    print(facts['os'])


    factsStr = '{"hostname": "nxosv", "os": "7.3", "location": "San_Jose"}'
    factDict = json.loads(factsStr)
    print(factsStr)
    print(factDict)