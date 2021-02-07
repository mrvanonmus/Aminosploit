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

prfile=input("\033[1;93m\n\n# ur profile url : \033[1;0m")

prfile=client.get_from_code(prfile)

comId=prfile.path[1:prfile.path.index("/")]

subclient=amino.SubClient(comId=comId,profile=client.profile)

prfile=prfile.objectId

os.system("clear")

print (" _____   _____       ___ \n/  ___/ | ____|     /   | \n| |___  | |__      / /| | \n\___  \ |  __|    / /_| | \n ___| | | |___   / /__| |\n/_____/ |_____| /_/   |_|")

prfile2=input("\n\n\033[1;93m# url of the person : \033[1;0m")

prfile2=client.get_from_code(prfile2)

prfile2=prfile2.objectId

os.system("clear")

print (" _____   _____       ___ \n/  ___/ | ____|     /   | \n| |___  | |__      / /| | \n\___  \ |  __|    / /_| | \n ___| | | |___   / /__| |\n/_____/ |_____| /_/   |_|")

msg=input("\n\n\033[1;93m# message : \033[1;0m")

subclient.start_chat(userId=[prfile,prfile2],message=msg)
