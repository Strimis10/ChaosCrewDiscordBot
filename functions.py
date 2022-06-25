import requests
import datetime
import os
from dotenv import load_dotenv
import json
import random
import praw
load_dotenv()
TOKEN = ""
TOKEN = os.getenv("TOKEN") #get_token()
BASE = "https://discord.com/api/v9/"
secret = ""
secret = os.getenv("secret") 



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



#returns info about a twitch user, rightnow used for twitch ids but you can also get other info.
def get_info(username):
    # ================================================================
    # your twitch client id
    client_id = 'tf0tlb5p4j8wcblpgw2dit3fnrywqx' 
    # your twitch secret       
    client_secret = secret
    # twitch username you want to check if it is streaming online
    twitch_user = username                           
    # ================================================================
    #getting auth token
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id':client_id,
        'client_secret':client_secret,
        'grant_type':'client_credentials'}
    req = requests.post(url=url,params=params)
    token = req.json()['access_token']
    #token = "gxx9wl9zts77lma5lmybjszfxh0t3y"
    # print(f'{token}')
    # ================================================================
    #getting user data (user id for example)
    url = f'https://api.twitch.tv/helix/users?login={twitch_user}'
    headers = {
        'Authorization':f'Bearer {token}',
        'Client-Id':f'{client_id}'}
    req = requests.get(url=url,headers=headers)
    userdata = req.json()
    userid = userdata['data'][0]['id']
    print(f'{userid=}')
    #print(userdata)
    # ================================================================
    #getting stream info (by user id for example)
    url = f'https://api.twitch.tv/helix/streams?user_id={userid}'
    headers = {
        'Authorization':f'Bearer {token}',
        'Client-Id':f'{client_id}'}
    req = requests.get(url=url,headers=headers)
    streaminfo = req.json()
    #print(f'{streaminfo=}')
    #print(bool(streaminfo['data']))
    # ================================================================
    return(userid)




#returns a boolean, True = Kenny is live, False = Kenny is not live
def kenny_live():
    
    client_id = 'tf0tlb5p4j8wcblpgw2dit3fnrywqx' 
         
    client_secret = secret
    
    twitch_user = 'Kennevo'                           
    
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id':client_id,
        'client_secret':client_secret,
        'grant_type':'client_credentials'}
    req = requests.post(url=url,params=params)
    token = req.json()['access_token']
    
    url = f'https://api.twitch.tv/helix/users?login={twitch_user}'
    headers = {
        'Authorization':f'Bearer {token}',
        'Client-Id':f'{client_id}'}
    req = requests.get(url=url,headers=headers)
    userdata = req.json()
    userid = userdata['data'][0]['id']

    url = f'https://api.twitch.tv/helix/streams?user_id={userid}'
    headers = {
        'Authorization':f'Bearer {token}',
        'Client-Id':f'{client_id}'}
    req = requests.get(url=url,headers=headers)
    streaminfo = req.json()

    is_streaming = bool(streaminfo['data'])
    return is_streaming




#post a random clip to the r/Kennevo subreddit 
def post_todays_clip():
    load_dotenv()

    token = ""
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    user_agent = "DAVE_0000000001"
    redirect_uri = "http://localhost:8080"
    refresh_token = os.getenv("refresh_token")

    with open("clips.json") as f:
        feeds = json.load(f)
        
    if feeds != {}:
        title = random.choice(list(feeds))
        todays_clip = feeds[title]

        subr = 'Kennevo'
        

        reddit = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            user_agent=user_agent,
                            redirect_uri=redirect_uri,
                            refresh_token=refresh_token)

        subreddit = reddit.subreddit(subr)

        

        flairs = list(subreddit.flair.link_templates.user_selectable())

        flair_id = None
        for flair in flairs:
            if flair['flair_text'] == "twitch clips":
                flair_id = flair['flair_template_id']
                break

        subreddit.submit(title,url=todays_clip,flair_id=flair_id)

        del feeds[title]

        with open("clips.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2)) 

