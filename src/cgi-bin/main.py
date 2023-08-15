import os
import requests
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_GRP_ID = os.getenv("TELEGRAM_GRP_ID")
url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TELEGRAM_GRP_ID}&text=SAATANA"

def main():
    print("Hello")
    try:
        res = requests.get(url, timeout=8, allow_redirects=True)
        print(res)
    except requests.exceptions.Timeout as err: 
        print(err)

if __name__ == "__main__":
    main()
