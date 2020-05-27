import requests
import argparse
import json

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i", "--ipaddress", help="IP address of target")
    args=parser.parse_args()
    ip=args.ipaddress
    url="http://ip-api.com/json/"+ip
    
    response = requests.get(url)
    data = json.loads(response.content)
    print(data)