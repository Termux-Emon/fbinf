#!/usr/bin/env python3

import requests

def fetch_info(uid):
    url = f"https://graph.facebook.com/{uid}?fields=name,link,picture.width(400).height(400),about&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print("\n[!] ইউজার খুঁজে পাওয়া যায়নি বা প্রাইভেট প্রোফাইল!")
            print("    ➤ Message:", data["error"]["message"])
        else:
            print("\n📄 প্রোফাইল তথ্য:")
            print(f"    🔹 নাম     : {data.get('name')}")
            print(f"    🔗 প্রোফাইল: {data.get('link')}")
            print(f"    🖼️ প্রোফাইল পিক: {data['picture']['data']['url']}")
            print(f"    📋 Bio/About: {data.get('about', 'নেই')}")

    except Exception as e:
        print("[!] সমস্যা:", str(e))


if __name__ == "__main__":
    print("=== Facebook Public Info Fetcher ===")
    user_id = input("👤 Facebook UID / Username দিন: ").strip()
    fetch_info(user_id)
          
