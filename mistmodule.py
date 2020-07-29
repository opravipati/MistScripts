import requests, json

def getVar():
    token = "" #Token Here 
    orgId= "" #ORGID Here
    return token,orgId

def getSiteDict(token,orgId):       #Function returns a dictionary containing site name and site IDs
    headers = {
    'Authorization': "Token {}".format(token), # Token with read write acccess required
    'Content-Type': "application/json",
        }
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

def getSiteId(siteDict,siteName):  #Function Returns a site ID
    if siteName in siteDict.keys():
        siteId = siteDict['{}'.format(siteName)]
        return siteId
    else:
        siteName = input("Site not in Org , Please input the correct site name: ")
        return getSiteId(siteDict,siteName)
        