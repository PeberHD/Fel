import requests, json, os

# 1: Bravery
# 2: Brilliance
# 3: Balance

class Exploit:

    def main(token,house):

        payload = json.dumps({
            'house_id': f'{house}'
        })

        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
        }
        url = 'https://discord.com/api/v9/hypesquad/online'
        r = requests.request("POST", url, headers=headers, data=payload)

if __name__ == '__main__':
    token = input('[+] Enter token -> ')
    print('''
1: Bravery
2: Brilliance
3: Balance    
    ''')
    house = input('[+] Number for house -> ')
    print(f'Successfully changed hypesquad house to {house}')
    Exploit.main(token,house)
    
    
os.system("py fel.py") 