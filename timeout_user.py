import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = ""
TOKEN = os.getenv("TOKEN") #get_token()
BASE = "https://discord.com/api/v9/"


#function that makes a request to the discord api to timeout a user as discord.py does not currently support this
def timeout_user(*, user_id: int, guild_id: int, until: int):
    endpoint = f'guilds/{guild_id}/members/{user_id}'
    headers = {"Authorization": f"Bot {TOKEN}"}
    url = BASE + endpoint
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    session = requests.patch(url, json=json, headers=headers)
    if session.status_code in range(200, 299):
        return session.json()
    else: 
        return print("Did not find any\n", session.status_code)