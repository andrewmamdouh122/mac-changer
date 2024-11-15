import subprocess 
import re
GREEN = '\033[32m'
RED = '\033[31m'
Mac_Address= input("enter the Mac address(example>> 11:22:33:44:55:66): ")
Network_Interface= input(str("enter the interface: "))
print("")
subprocess.run("ifconfig "+Network_Interface+" down", shell=True)  
subprocess.run("ifconfig "+Network_Interface+" hw ether "+ Mac_Address, shell=True)  
subprocess.run("ifconfig "+Network_Interface+" up", shell=True)
ifconfig_result =subprocess.check_output("ifconfig "+Network_Interface, shell=True).decode("UTF-8")
New_MAC= re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
if New_MAC[0] == Mac_Address :
    print (f"{GREEN}[+]the Mac Address has been changed")
else:
    print (f"{RED}[-]there is something going wrong")
