from dotenv import load_dotenv
import os
import sys


from notam_fetcher import NotamFetcher

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if CLIENT_ID is None:
    print("Set CLIENT_ID in .env file")
    sys.exit()
if CLIENT_SECRET is None:
    print("Set CLIENT_SECRET in .env file")
    sys.exit()

notam_fetcher = NotamFetcher(CLIENT_ID, CLIENT_SECRET)

notams = notam_fetcher.fetchNotamsByLatLong(22, -78, 100)  

