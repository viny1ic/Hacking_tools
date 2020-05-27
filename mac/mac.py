import subprocess

class mac_changer:
    def __init__(self):
        self.mac=""
    
    def get_mac(self,iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)
        result=output.stdout.decode()
        print(result)