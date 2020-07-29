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


Repository currently contains four files. 
1. mistmodule.py contains the functions that will be used from other scripts. This will also be the file where you store your token and Organization ID information
2. orgUpgrades.py can be used to upgrade infrastructure at all sites in the organization
3. siteUpgrade.py can be used to upgrade infrastructure at any one site in the organization
4. orgOfflineAPs.py can be used to provide a list of offline APs in the organization and write it to a csv file.

Scripts for more operational tasks will be added in the future. 