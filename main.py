thing = "────────────────────────────────" # thing for faster code
webhook_thing = "────────────────────────" # webhook thing for faster code

# modules
import http.client, json, requests, time
from datetime import datetime, timezone, timedelta
from colorama import Fore, Style
from termcolor import colored
import cloudscraper

s = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})

scraper = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# config settings
version = config["version"]
credits = config["credits"]
tiktok_user = config["tiktok_user"]
discord_server = config["discord_server"]
discord_username = config["discord_username"]
ping_low_prize = config["ping_low_prize"]
ping_high_prize = config["ping_high_prize"]
webhook = config["webhook"]
time_sleep_every_loop = config["time_sleep_every_loop"]

print(Fore.RED, ">> [Started!]", Style.RESET_ALL, flush=True)
print(Fore.LIGHTWHITE_EX, f"{thing}")
print(Fore.RED, ">> Main", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Version: {version}", Style.RESET_ALL, flush=True)
print(Fore.LIGHTWHITE_EX, f"{thing}")
print(Fore.RED, ">> Pings", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> High rains: {ping_high_prize}", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Low rains: {ping_low_prize}", Style.RESET_ALL, flush=True)
print(Fore.LIGHTWHITE_EX, f"{thing}")
print(Fore.RED, ">> Info", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Powered by: {credits}", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Follow us on TikTok {tiktok_user}", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Join our community discord server {discord_server}", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Dm {discord_username} on discord to report bugs/other issues", Style.RESET_ALL, flush=True)

kiev_timezone = timezone(timedelta(hours=3))  # UTC+3
current_time = datetime.now(kiev_timezone)
adjusted_time = current_time - timedelta(hours=1)
current_time_kiev = adjusted_time.strftime("%H:%M")

# rain finder
def active():
    conn = http.client.HTTPSConnection("api.bloxflip.com")
    made_by = "kellyhated,coxy57"
    headers = {
        "Referer": "https://bloxflip.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.5938.108 Mobile/15E148 Safari/604.1"
    }
    conn.request("GET", url="/chat/history", headers=headers)
    return json.loads(conn.getresponse().read().decode())['rain']
# duration check
while True:
    rain_ = active()
    if rain_['active']:
        getd = rain_['duration']
        c = rain_['created']
        addx = getd + c
        dur = addx / 1000
        duration = round(dur)
        conv = (duration / (1000 * 60)) % 60
        time_to_slp = (conv * 60 + 10)
        usdid = scraper.post(f"https://users.roblox.com/v1/usernames/users",
                              json={"usernames": [rain_['host']]}).json()['data'][0]['id']
        # rain pings
        prize = int(rain_['prize'])
        if prize >= 501:
            ping = ping_high_prize
            data = {
                "content": f"{ping}",
                "username": "Big Rain Notifier"
            }
            data["embeds"] = [
                {
                    "description": f"- 🌧 New big rain started!\n- 👥 **Host**: {rain_['host']}\n- 💸 **Rain Amount**: {rain_['prize']}\n- ⌚ **Expiration**: <t:{duration}:R>\n- 🍂 **Hop on [BloxFlip](https://bloxflip.com) to participate in this chat rain!**\n{webhook_thing}\n- **Last time rain detected: {current_time_kiev} (UTC+3)**\n- **Version: {version} | made by {credits}**",
                    "title": "Good News!",
                    "thumbnail": {
                        "url": scraper.get(
                            f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={usdid}&size=50x50&format=Png&isCircular=false").json()['data'][0][
                            'imageUrl']
                    }
                }
            ]
        else:
            ping = ping_low_prize
            data = {
                "content": f"{ping}",
                "username": "Low Rain Notifier"
            }
            data["embeds"] = [
                {
                    "description": f"- 🌧 New low rain started!\n- 👥 **Host**: {rain_['host']}\n- 💸 **Rain Amount**: {rain_['prize']}\n- ⌚ **Expiration**: <t:{duration}:R>\n- 🍂 **Hop on [BloxFlip](https://bloxflip.com) to participate in this chat rain!**\n{webhook_thing}\n- **Last time rain detected: {current_time_kiev} (UTC+3)**\n- **Version: {version} | made by {credits}**",
                    "title": "Good News!",
                    "thumbnail": {
                        "url": scraper.get(
                            f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={usdid}&size=50x50&format=Png&isCircular=false").json()['data'][0][
                            'imageUrl']
                    }
                }
            ]

        r = scraper.post(webhook, json=data)
        time.sleep(time_to_slp)
    time.sleep(time_sleep_every_loop)

# CONTACT kellyhate IN DISCORD FOR SUPPORT
