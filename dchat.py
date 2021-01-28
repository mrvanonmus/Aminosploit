comId="241758681"
import os
os.system("clear")
print (" _____   _____       ___ \n/  ___/ | ____|     /   | \n| |___  | |__      / /| | \n\___  \ |  __|    / /_| | \n ___| | | |___   / /__| |\n/_____/ |_____| /_/   |_|")
sid=input("\033[1;31m\n# ur sid : \033[1;0m")
import aminos
import amino
client=aminos.ClientSid()                          
'''
login
'''
ss=0
sz=25
nuum=0
tst=False
while tst==False:
	try:
		client.sssid(sid=sid)
		tst=True
	except:
		tst=False
		print("\033[1;33m\n# Verify ur account! \n")
		exx=input("# continue?\033[1;32m y/n : ")
		if exx=='N' or exx=='n' or exx=='no':
				os._exit(1)
				
os.system("clear")
print (" _____   _____       ___ \n/  ___/ | ____|     /   | \n| |___  | |__      / /| | \n\___  \ |  __|    / /_| | \n ___| | | |___   / /__| |\n/_____/ |_____| /_/   |_|")

u=input("Host Link: ")
us=client.get_from_code(u)
p=us.objectId
comId=us.path[1:us.path.index('/')]
chatl=input("Chat Link: ")
chatId=client.get_from_code(chatl).objectId
subclient=amino.SubClient(comId=comId, profile=client.profile)

subclient.kick(userId=p ,chatId=chatId, allowRejoin=True)
print ("Done ")
os._exit(1)
