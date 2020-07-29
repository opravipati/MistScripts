import requests, json
import mistmodule


def siteUpgrade(siteId):  # Function Upgrades access points at a site.
    payload = {
        "version": "0.5.1944", #Version to upgrade to
        "enable_p2p": True #Enabling peer to peer upgrade
    }
    payload=json.dumps(payload)     #Converts the payload to JSON format
    upgradeUrl = "https://api.mist.com/api/v1/sites/" + siteId + "/devices/upgrade" #API URL To upgrade the devices
    upgradeCall = requests.request("POST", upgradeUrl , data=payload, headers=headers)  #API call performed with the payload
    return upgradeCall.status_code,upgradeCall.text.encode('utf8')   #Returns the HTTP Response code for the API call.


token,orgId = mistmodule.getVar() #Function call to get token and OrgID information from mistmodule
siteDict = mistmodule.getSiteDict(token,orgId) #Function call to get siteDict from mistmodule

headers = {
    'Authorization': "Token {}".format(token), # Token with read write acccess required
    'Content-Type': "application/json",
        }

for siteName,siteId in siteDict.items():  #Loops through the Dictionary to make API calls for each site.
    try:
        upgradeStatus,upgradeMessage = siteUpgrade(siteId)
        if upgradeStatus == 200: #HTTP Response is 200 for successful API calls.
            print("Upgrade API call Successful for site " , siteName)
        else:
            print("Error Occurred ", upgradeStatus, upgradeMessage) 
    except Exception as e:
            print(e)  


