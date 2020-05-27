import subprocess
import re

class mac_changer:
    def __init__(self):
        self.mac=""
    
    def get_mac(self,iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)
        result=output.stdout.decode()

        pattern=r'ether\s[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}'
        regex=re.compile(pattern)
        answer=regex.search(result)
        mac_address=answer.group().split()[1]
        self.mac=mac_address
        return mac_address