import requests, json, csv
import mistmodule


def offlineAps(orgId): #Function call writes offline access point names to csv file
    orgInventoryUrl = "https://api.mist.com/api/v1/orgs/" + orgId + "/inventory"
    orgInventoryCall = requests.request("GET", orgInventoryUrl , headers=headers)  #API call performed 
    orgInventory = orgInventoryCall.json()
    with open('offlineAPs.csv','w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar= '|', quoting=csv.QUOTE_MINIMAL)
        for device in orgInventory:
            if device['connected'] is False:
                filewriter.writerow([device['name']])
                

token,orgId = mistmodule.getVar() #Function call to get token and OrgID information from mistmodule
headers = {
    'Authorization': "Token {}".format(token), # Token with read write acccess required
    'Content-Type': "application/json",
        }
offlineAps(orgId)