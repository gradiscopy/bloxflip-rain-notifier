# WARNING
That code was made by coxy.57 i took it and added things, fixed the bug with bot not sending webhook, added better designs, more messages in webhook, pings for big rains and low rains, visuals in code, and other things

# BloxFlip Rain Notifier

## Overview

BloxFlip Rain Notifier is a Python script designed to notify users about rain events on the BloxFlip platform. It can be configured to send different notifications based on the rain amount.

## Features

- **Pings:** Notifies users with different pings based on the rain amount.
- **Webhook Integration:** Sends notifications to a specified Discord webhook.
- **Logging:** Records rain events and errors in a log file.

   ## Requirements

- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`):
  - `http.client`
  - `json`
  - `requests`
  - `time`
  - `datetime`
  - `timezone`
  - `timedelta`
  - `colorama`
  - `cloudscraper`
  - `logging`

## Tutorial

### Step 1: Install Python

1. Download and install Python 3.x from the official website: [Python Downloads](https://www.python.org/downloads/)
2. During installation, make sure to check the box that says "Add Python to PATH."

### Step 2: Set up the config

The `config.json` file is used to customize the behavior of the BloxFlip Rain Notifier. Here's a step-by-step guide on how to use and configure the settings:

**Ping Settings:**

   - `ping_low_prize`: Set the default ping for rain amounts below 1000 R$.
   - `ping_high_prize`: Set the default ping for rain amounts 1000 R$ and above.
   - `webhook`: Provide the Discord webhook URL where you want to receive notifications. Setting up Discord Webhook:

### Setting up Discord Webhook:
    In your Discord server, navigate to the channel where you want to receive notifications.
    Click on the gear icon next to the channel name and select "Edit Channel."
    Go to the "Integrations" tab and click "Create Webhook."
    Customize the name and avatar of your webhook and click "Copy Webhook URL."
    Replace the webhook value in your config.json file with the copied URL.

   ```json
   ```"ping_low_prize": "your_default_ping_below_1k",```
   "ping_high_prize": "your_default_ping_1k_and_above",
   "webhook": "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN",
