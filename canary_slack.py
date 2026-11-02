# canary_slack.py — Parses Thinkst Canarytoken webhook and formats alert for 【entity-SOAR¦canonical_name=SOAR】
# No real credentials committed — Slack/SentinelOne calls are shown as commented examples

import json

def handle_canary_alert(webhook_data: str):
    try:
        data = json.loads(webhook_data)
    except json.JSONDecodeError:
        print("[!] Invalid webhook JSON")
        return

    token = data.get("memo", "Unknown token")
    src_ip = data.get("src_ip", "Unknown IP")
    user_agent = data.get("useragent", "Unknown")

    # Format message for Slack / 【entity-SOAR¦canonical_name=SOAR】 — this is what the current lab does
    message = (
        f"CANARY TRIGGERED: {token} | "
        f"IP: {src_ip} | UA: {user_agent} | "
        f"Action: Format alert for Slack and SentinelOne isolation workflow"
    )
    print(message)

    # Example Slack integration — replace XXXX locally, do NOT commit real webhook
    # import requests
    # requests.post("https://hooks.slack.com/services/XXXX", json={"text": message})

    # Example SentinelOne isolation — replace XXXX locally, do NOT commit real API key
    # import requests
    # requests.post("https://XXXX.sentinelone.net/web/api/v2.1/agents/actions/disconnect",
    #               headers={"ApiToken": "XXXX"}, json={"filter": {"ip": src_ip}})

# Test with sample
sample = '{"memo":"Passwords_2024.docx","src_ip":"192.168.56.101","useragent":"Microsoft Office"}'
handle_canary_alert(sample)
