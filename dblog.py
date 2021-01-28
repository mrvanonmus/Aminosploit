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
userlink=input("Your Profile Link: ")
user=client.get_from_code(userlink)
userId=user.objectId
comId=user.path[1:user.path.index('/')]
subclient=amino.SubClient(comId=comId, profile=client.profile)

def Bot(data):
    listusers=[]
    for userId ,status in zip(data.blogId,data.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers

while True:
	blogs=subclient.get_user_blogs(userId=userId, start=0, size=25)
	for blogId in Bot(blogs):
		try:
			subclient.delete_blog(blogId=blogId)
			print ("tm")
		except:
			pass
			print ("w.t.f")