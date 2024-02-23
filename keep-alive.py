# RESTARTER BY Revive#8798
# WEBHOOK AND JSON SUPPORT BY Moonly#7996 | kellyhate

import requests
import subprocess
import json
import logging
import pytz
import os
import colorama
from datetime import datetime

colorama.init()

logging.basicConfig(
    level=logging.INFO,
    filename="restart_log.txt",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

kiev_timezone = pytz.timezone("Europe/Kiev")

with open('restarter-config.json', 'r') as f:
    data = json.load(f)

webhook_config = data.get("webhook", {})
webhook_enabled = webhook_config.get("enabled", False)
webhook_url = webhook_config.get("url", "")
minutes_per_restart = data["minutes"]
webhook_msg = data["webhookMsg"]
send_msg = data["sendMsg"]

embed_data = {
    "color": 0x000000,
    "author": {
        "name": f"{webhook_msg}"
    },
    "footer": {
        "text": "Kelly Restarter | V2.0.0",
        "icon_url": "https://cdn.discordapp.com/attachments/1142580852644122795/1145400953047093248/e496fd15afc37f773f3f2f6ddf5006ca.jpg"
    }
}

log_file = "restart_log.txt"
max_log_size_bytes = 35 * 1024

def cleanup_logs(log_file):
    if os.path.exists(log_file) and os.path.getsize(log_file) >= max_log_size_bytes:
        print(colorama.Fore.YELLOW + "cleaning restarter logs...")
        with open(log_file, 'w'):
            pass

while True:
    cleanup_logs(log_file)
    
    process = subprocess.Popen(['python', 'main.py'])

    current_time = datetime.now(kiev_timezone).strftime("%Y-%m-%d %H:%M:%S")

    if send_msg and data["webhook"]["enabled"]:
        embed_data["description"] = f"*restarted at* ``{current_time} (Kyiv/Moscow time)``"
        response = requests.post(webhook_url, json={"content": None, "embeds": [embed_data]})
        if response.status_code == 200:
            logging.info("Message sent successfully to webhook")
        else:
            logging.error(f"(FakeError) Message sent successfully to webhook. Status code: {response.status_code}")

    try:
        process.wait(minutes_per_restart * 60)
    except KeyboardInterrupt:
        print(colorama.Fore.RED + "exiting...")
        break
    except Exception as e:
        logging.error(f"(FakeError) Your bot has been rebooted after: {e}")

    process.kill()
    print(colorama.Fore.YELLOW + "restarting...")
    continue
