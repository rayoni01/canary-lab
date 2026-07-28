# canary_slack.py - Parses Thinkst Canarytoken webhook and sends to Slack
import json

def handle_canary_alert(webhook_data):
    data = json.loads(webhook_data)
    token = data.get('memo', 'Unknown token')
    src_ip = data.get('src_ip', 'Unknown IP')
    user_agent = data.get('useragent', '')
    
    message = f"🚨 CANARY TRIGGERED: {token}\nIP: {src_ip}\nUA: {user_agent}\nAction: Isolate host in SentinelOne"
    print(message)

# Test with sample
sample = '{"memo":"Passwords_2024.docx", "src_ip":"192.168.56.101", "useragent":"Microsoft Office"}'
handle_canary_alert(sample)