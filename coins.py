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

tId=client.get_wallet_history(start=0,size=1).transanctionId

os.system("clear")
print (" _____   _____       ___ \n/  ___/ | ____|     /   | \n| |___  | |__      / /| | \n\___  \ |  __|    / /_| | \n ___| | | |___   / /__| |\n/_____/ |_____| /_/   |_|")

cht=input("\n\n\033[1;33m# Give Me The Chat url : \033[1;0m")
cht=client.get_from_code(cht)

comId=cht.path[1:cht.path.index("/")]
subclient=amino.SubClient(comId=comId,profile=client.profile)

cht=cht.objectId

print("\n\n\033[1;33mThe TransactionId : \033[1;0m"+tId.pop())

os.system("clear")
print (" _____   _____       ___ \n/  ___/ | ____|     /   | \n| |___  | |__      / /| | \n\___  \ |  __|    / /_| | \n ___| | | |___   / /__| |\n/_____/ |_____| /_/   |_|")

tran=input("\n\n\033[1;33m# Give Me The TransactionId :\033[1;0m ")

while True:
	coins=input("\n\n\033[1;33m# How Much Coins ? :\033[1;0m ")
	subclient.send_coins(chatId=cht,coins="1",transactionId=tran)
	subclient.send_coins(chatId=cht,coins=coins,transactionId=tran)
	subclient.send_coins(chatId=cht,coins=coins,transactionId=tran)
	subclient.send_coins(chatId=cht,coins=coins,transactionId=tran)
	print("\n\033[1;36mDone...")
