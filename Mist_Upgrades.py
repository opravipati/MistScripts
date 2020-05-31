import requests, json

headers = {
    'Authorization': "Token #here", # Token with read write acccess required
    'Content-Type': "application/json",
        }
def getSiteDict(orgId):
    sitesUrl = "https://api.mist.com/api/v1/orgs/" + orgId + "/sites"   #API to get list of sites in your Ogranization
    getSiteIds = requests.request("GET", sitesUrl , headers=headers) #API call performed
    getSiteIds_json = getSiteIds.json() #Decodes the JSON data from API Request into a list
    siteDict={}
    for site in getSiteIds_json:    #Loops through the list and appends site names and site IDs to the siteDict
        try:
            siteDict.update({site['name']:site['id']})
        except Exception as e:
            print(e)
    return siteDict

def siteUpgrade(siteId):
    payload = {
        "version": "0.5.17360", #Version to upgrade to
        "enable_p2p": True #Enabling peer to peer upgrade
    }
    payload=json.dumps(payload)     #Converts the payload to JSON format
    upgradeUrl = "https://api.mist.com/api/v1/sites/" + siteId + "/devices/upgrade" #API URL To upgrade the devices
    upgradeCall = requests.request("POST", upgradeUrl , data=payload, headers=headers)    #API call performed with the payload
    return upgradeCall.status_code    #Returns the HTTP Response code for the API call.

orgId= "#Enter Org ID Here"  

siteDict=getSiteDict(orgId) #Function call to get siteDict
for siteName,siteId in siteDict.items():  #Loops through the Dictionary to make API calls for each site.
    try:
        upgradeStatus=siteUpgrade(siteId)
        if upgradeStatus == 200: #HTTP Response is 200 for successful API calls.
            print("Upgrade API call Successful for site " , siteName)
        else:
            print("Error Occurred ", upgradeStatus) 
    except Exception as e:
            print(e)  


