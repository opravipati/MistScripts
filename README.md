# Mist API Scripts for Operational Automation
The repository is intended to provide scripts based on the Mist APIs that will enable automation of operational tasks. 

## Save this repository to your computer
Be sure you have [git](https://git-scm.com/downloads) installed  
then run the command 
```git clone https://github.com/opravipati/MistScripts.git```


### Install Dependencies
The first step required to run the scripts is install the dependencies.

In the directory that you have the script
```
pip3 install -r requirements.txt 
```
### Generate Token
Once you have the packages installed, the next requirement is to populate your token and OrID information in the mistmodule.py file. For steps to create your token and also identify your OrgID please please visit https://www.mist.com/documentation/using-postman/


### Mist API Documentation
Home Page https://api.mist.com/api/v1/docs/Home


Repository currently contains five files. 
1. mistmodule.py contains the functions that will be used from other scripts. This will also be the file where you store your token and Organization ID information
To start using these scripts , please add your token and Org Id to mistmodule.py file
```
def getVar():
    token = "#Token Here"  
    orgId= "#ORGID Here" 
    return token,orgId
```
2. orgUpgrades.py can be used to upgrade infrastructure at all sites in the organization
To upgrade access points at all sites in your Organization, please set the version in orgUpgrades script in the function shown below
```
def siteUpgrade(siteId):  # Function Upgrades access points at a site.
    payload = {
        "version": "0.5.1944", #Version to upgrade to
        "enable_p2p": True #Enabling peer to peer upgrade
    }
 ```
If you want to upgrade only specific model of APs, the payload can be modified accordingly.
```
{
    "version": "3.1.5",
    "enable_p2p": false,
    "models": [
        "AP41"   
    ]
}
```
3. siteUpgrade.py can be used to upgrade infrastructure at any one site in the organization. This will prompt you to enter a site name. The version on the payload needs to be updated in this file similar to orgUpgrades.py. 
4. orgOfflineAPs.py can be used to provide a list of offline APs in the organization. Running this script will result in a CSV file with the list of APs. Please note the APs need to have a name in order to appear in the list. Mist APs by default display the mac address under the name on UI. Such APs will not be included in the csv file.
5. trackClients.py can be used to track client details every 60 seconds. When this script is execute, it prompts you to enter a mac address of the client and the site name to track. Mist updates its client information every 60 seconds and so the default frequency to track client has been set to the same value.


Scripts for more operational tasks will be added in the future. 
