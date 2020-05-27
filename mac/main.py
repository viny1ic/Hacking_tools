from mac import mac_changer

if __name__=="__main__":
    print("Please enter your interface: ")
    interface=input()
    m=mac_changer()
    ans=m.get_mac(interface)
    print(ans)