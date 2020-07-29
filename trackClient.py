import requests, json, time
import mistmodule


def trackClient(mac,siteId):
    while True:
        clientUrl="https://api.mist.com/api/v1/sites/" + siteId + "/stats/clients/" + mac
        getClientDetails=requests.request("GET", clientUrl , headers=header)
        getClientDetails_json = getClientDetails.json()
        if getClientDetails.status_code == 404:
            print("Client Not Found")
            trackClient(input("Please enter a valid MAC address: "),siteId)
        elif getClientDetails.status_code == 200:
            apUrl = "https://api.mist.com/api/v1/sites/" + siteId + "/devices/"+ getClientDetails_json['ap_id']
            getApDetails = requests.request("GET", apUrl , headers=header)
            getApDetails_json=getApDetails.json()
            print("Client MAC Address".ljust(35,'.') ,getClientDetails_json['mac'])
            print("AP Name".ljust(35,'.'), getApDetails_json['name'])
            print("Client IP Address".ljust(35,'.'), getClientDetails_json['ip'])
            print("Client Vendor".ljust(35,'.'), getClientDetails_json['manufacture'])
            print("Radio Signal Strength Indicator".ljust(35,'.'), getClientDetails_json['rssi'])
            print("Signal to Noise Ratio".ljust(35,'.'), getClientDetails_json['snr'])
            print("Wireless LAN Network Name".ljust(35,'.'), getClientDetails_json['ssid'])
            print("Channel".ljust(35,'.'), getClientDetails_json['channel'])
            print("Connected For".ljust(35,'.'), getClientDetails_json['uptime'], "Seconds")
            print('Next Update in 60 seconds')
            print(f'####### ctrl+c to quit##############')
            print()
            time.sleep(60)
        else:
            print("API Error Occured, Response Code: ", getClientDetails.status_code)

token,orgId = mistmodule.getVar() #Function call to get token and OrgID information from mistmodule
siteDict = mistmodule.getSiteDict(token,orgId) #Function call to get siteDict from mistmodule
clientMac = input("Please input the MAC address of the client in aa:bb:cc:dd:ee:ff format: ")
siteName = input("Please input the site name: ")
siteDict=mistmodule.getSiteDict(token,orgId) #Function call to get SiteDict
siteId = mistmodule.getSiteId(siteDict,siteName) #Function call to get SiteID from siteDict

header = {
    'Authorization': "Token {}".format(token), # Token with read write acccess required
    'Content-Type': "application/json",
        }

trackClient(clientMac,siteId)