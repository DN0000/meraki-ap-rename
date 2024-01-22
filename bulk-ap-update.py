import csv
import meraki
from tkinter import filedialog
from tkinter import *

merakiapi = "API KEY HERE"

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select CSV file to import",filetypes = (("CSV","*.CSV"),("All Files","*.*")))
filename = str(root.filename)


with open(filename, encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    dashbord = meraki.DashboardAPI(merakiapi,suppress_logging=TRUE,wait_on_rate_limit=TRUE)
    for row in reader:                
                    # Build strings for creating object

                    ip = (str(row['IP']))
                    serial = (str(row['Serial']))
                    name = (str(row['Name']))
                    location = (str(row["Location"]))

                    deviceupdate = dashbord.devices.updateDevice(serial=serial,name=name,notes=location)
                    
                    response = dashbord.devices.updateDeviceManagementInterface(
                        serial, 
                        wan1={'wanEnabled': 'enabled', 'usingStaticIp': True, 'staticIp': ip, 'staticSubnetMask': '255.255.255.0', 'staticGatewayIp': "10.223.144.1", 'staticDns': ['10.223.145.24','10.224.150.10']}, 
                    )

                    print(serial + " Complete")