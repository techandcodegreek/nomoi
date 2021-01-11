import json

with open('server_info.json') as config_file:
    config = json.load(config_file)
    
print(config['host'])
print(config['username'])
print(config['password'])
print(config['port'])