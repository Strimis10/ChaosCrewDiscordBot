import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = ""
TOKEN = os.getenv("TOKEN") #get_token()
BASE = "https://discord.com/api/v9/"

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


        

#guild_id = 932684556572700773
#user_id = 914149753460236289
#time_in_mins = 1
#timeout_user(user_id=user_id, guild_id=guild_id,until=time_in_mins)




