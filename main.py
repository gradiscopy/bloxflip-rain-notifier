# modules
import http.client, json, requests, time
from datetime import datetime, timezone, timedelta
from colorama import Fore, Style
import cloudscraper
import logging

# logs config DONT CHANGE
logging.basicConfig(filename='logs.txt', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

s = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})

scraper = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})

thing = "────────────────────────────────"  # thing for faster code
webhook_thing = "────────────────────────"  # webhook thing for faster code
credits = "kellyhated,coxy.57"
tiktok_user = "@kellysqw"
discord_server = "discord.gg/SDZac8mSXd"
discord_username = "kellyhate"
version = "V1.55"
github = "https://github.com/kellyhated/bloxflip-rain-notifier"

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# config settings
ping_low_prize = config["ping_low_prize"]
ping_high_prize = config["ping_high_prize"]
webhook = config["webhook"]
time_sleep_every_loop = config["time_sleep_every_loop"]

print(Fore.RED, ">> [Started!]", Style.RESET_ALL, flush=True)
print(Fore.LIGHTWHITE_EX, f"{thing}")
print(Fore.RED, ">> Main", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Version: {version}", Style.RESET_ALL, flush=True)
print(Fore.RED, f">> Webhook: {webhook}", Style.RESET_ALL, flush=True)
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
print(Fore.RED, f">> Our GitHub {github}", Style.RESET_ALL, flush=True)

kiev_timezone = timezone(timedelta(hours=3))  # UTC+3
current_time = datetime.now(kiev_timezone)
adjusted_time = current_time - timedelta(hours=1)
current_time_kiev = adjusted_time.strftime("%H:%M")

# rain finder
def active():
    conn = http.client.HTTPSConnection("api.bloxflip.com")
    made_by = "kellyhated,coxy.57"
    headers = {
        "Referer": "https://bloxflip.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    conn.request("GET", url="/chat/history", headers=headers)
    return json.loads(conn.getresponse().read().decode())['rain']

# duration check
while True:
    scraper = cloudscraper.create_scraper()
    try:
        r = scraper.get('https://api.bloxflip.com/chat/history').json()
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
            
            # rain pings / rain amount
            prize = int(rain_['prize'])
            if prize >= 501:
                ping = ping_high_prize
                data = {
                    "content": f"{ping}",
                    "username": "Big Rain Notifier"
                }
                data["embeds"] = [
                    {
                        "description": f"- 🌧 New big rain started!\n- 👥 **Host**: {rain_['host']}\n- 📜 **User ID**: {usdid}\n- 💸 **Rain Amount**: {rain_['prize']} R$\n- ⌚ **Expiration**: <t:{duration}:R>\n- 🍂 **Hop on [BloxFlip](https://bloxflip.com) to participate in this chat rain!**",
                        "title": "Good news!",
                        "color": 0xFFFF00,
                        "thumbnail": {
                            "url": scraper.get(
                                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={usdid}&size=50x50&format=Png&isCircular=false").json()['data'][0][
                                'imageUrl']
                        },
                        "footer": {
                            "text": f"{version} | {current_time_kiev}",
                            "icon_url": "https://cdn.discordapp.com/avatars/1206213607881445397/7205c6a9b70fbb9dd696d98603189b1e.webp?size=80"
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
                        "description": f"- 🌧 New low rain started!\n- 👥 **Host**: {rain_['host']}\n- 📜 **User ID**: {usdid}\n- 💸 **Rain Amount**: {rain_['prize']} R$\n- ⌚ **Expiration**: <t:{duration}:R>\n- 🍂 **Hop on [BloxFlip](https://bloxflip.com) to participate in this chat rain!**",
                        "title": "Good news!",
                        "color": 0x00008B,
                        "thumbnail": {
                            "url": scraper.get(
                                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={usdid}&size=50x50&format=Png&isCircular=false").json()['data'][0][
                                'imageUrl']
                        },
                        "footer": {
                            "text": f"{version} | {current_time_kiev}",
                            "icon_url": "https://cdn.discordapp.com/avatars/1206213607881445397/7205c6a9b70fbb9dd696d98603189b1e.webp?size=80"
                        }
                    }
                ]

            # log info abt rains idk xd
            logging.info(f"Detected new rain\nHost: {rain_['host']}\nUser ID: {usdid}\nAmount: {rain_['prize']}\nPing: {ping}\nLast time rain detected: {current_time_kiev}\n────")
            print(f"Detected new rain\nHost: {rain_['host']}\nUser ID: {usdid}\nAmount: {rain_['prize']}\nPing: {ping}\nLast time rain detected: {current_time_kiev}")

            r = scraper.post(webhook, json=data)
            time.sleep(time_to_slp)
        time.sleep(time_sleep_every_loop)
    except Exception as e:
        # log exceptions
        logging.error(f"Error occurred: {str(e)}")
        time.sleep(time_sleep_every_loop)

# dm kellyhate in dc for contact
