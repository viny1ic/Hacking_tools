from mac import mac_changer

if __name__=="__main__":
    print("Please enter your interface: ", end="")
    interface=input()
    print("please enter new mac address: ", end="")
    newmac=input()
    m=mac_changer()
    currmac=m.get_mac(interface)
    changemac=m.change_mac(interface,newmac)
    