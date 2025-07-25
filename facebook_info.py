#!/usr/bin/env python3

# Author: Emon
# GitHub: https://github.com/YourUsername (replace with your actual GitHub)
# Tool: fbinf - Facebook Username Checker (no login required)

import requests

def check_facebook_user(username):
    url = f"https://www.facebook.com/{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile)'
    }

    print(f"\n🔍 Checking Facebook profile for username: {username}")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"✅ Profile found: {url}")
    elif response.status_code == 404:
        print(f"❌ Profile not found or deleted: {username}")
    else:
        print(f"⚠️ Unexpected status code: {response.status_code}")

if __name__ == "__main__":
    print("=== fbinf: Facebook Profile Checker by Emon ===")
    user = input("Enter Facebook Username: ").strip()
    check_facebook_user(user)
    
