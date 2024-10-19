import socket
import sys
import time

########################################################################
DELAY = 0.3
########################################################################

if len(sys.argv) == 1 :
	print('[!] Please enter a valid tenant name')
	print('Usage: python3 reconazure.py [DOMAIN]')
	print('')
	print('> python3 reconazure.py mytenant')
	sys.exit()
else :
	DOMAIN = sys.argv[-1]

SUBDOMAINS = {'YOURTENANTDOMAINHERE.onmicrosoft.com':'Microsoft Hosted Domain',
'YOURTENANTDOMAINHERE.scm.azurewebsites.net':'App Services - Management',
'YOURTENANTDOMAINHERE.azurewebsites.net':'App Services',
'YOURTENANTDOMAINHERE.p.azurewebsites.net':'App Services',
'YOURTENANTDOMAINHERE.cloudapp.net':'App Services',
'YOURTENANTDOMAINHERE.file.core.windows.net':'Storage Accounts - Files',
'YOURTENANTDOMAINHERE.blob.core.windows.net':'Storage Accounts - Blobs',
'YOURTENANTDOMAINHERE.queue.core.windows.net':'Storage Accounts - Queues',
'YOURTENANTDOMAINHERE.table.core.windows.net':'Storage Accounts - Tables',
'YOURTENANTDOMAINHERE.mail.protection.outlook.com':'Email',
'YOURTENANTDOMAINHERE.sharepoint.com':'SharePoint',
'YOURTENANTDOMAINHERE-my.sharepoint.com':'SharePoint',
'YOURTENANTDOMAINHERE.redis.cache.windows.net':'Databases-Redis',
'YOURTENANTDOMAINHERE.documents.azure.com':'Databases-Cosmos DB',
'YOURTENANTDOMAINHERE.database.windows.net':'Databases-MSSQL',
'YOURTENANTDOMAINHERE.vault.azure.net':'Key Vaults',
'YOURTENANTDOMAINHERE.azureedge.net':'CDN',
'YOURTENANTDOMAINHERE.search.windows.net':'Search Appliance',
'YOURTENANTDOMAINHERE.azure-api.net':'API Services',
'YOURTENANTDOMAINHERE.azurecr.io':'Azure Container Registry'}

def scanAzureTenant(dom):
	try:
		IP = getIPof(dom)
		return True
	except Exception as e:
		if ' getaddrinfo failed' in str(e) :
			return False
		elif 'No address associated with hostname' in str(e) :
			return True
		else:
			return False
	finally:
		time.sleep(DELAY)

def getIPof(hostname):
	return socket.gethostbyname(hostname)

def main():
	for key in SUBDOMAINS:
		dom = key.replace("YOURTENANTDOMAINHERE",DOMAIN)
		if scanAzureTenant(dom):
			print("[+] " + dom + "	(" + SUBDOMAINS[key] + ")")

print("Existing services for Azure tenant " + DOMAIN)
print("__________________________________" + "_"*len(DOMAIN))

main()
