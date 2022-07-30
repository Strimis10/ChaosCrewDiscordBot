import requests
import datetime
import os
from dotenv import load_dotenv
import json
import random
import praw


load_dotenv()
TOKEN = os.getenv("TOKEN") #get_token()
BASE = "https://discord.com/api/v9/"
secret = os.getenv("secret") 
Bm_api_key = os.getenv("Bm_api_key")

#get a map view from latitude and longitude coordinates
def get_map_view(lat:float,lon:float,fname:str):
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    import numpy as np

    m = Basemap(width=12000000,height=9000000,projection='lcc', 
                resolution='c',lat_1=lat,lat_2=lat+10,lat_0=lat+5,lon_0=lon, )#location of camera
    
    

    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral',lake_color='aqua')

    parallels = np.arange(0.,81,10.)
    m.drawparallels(parallels,labels=[False,True,True,False])

    meridians = np.arange(10.,351.,20.)
    m.drawmeridians(meridians,labels=[True,False,False,True])


    xpt,ypt = m(lon,lat) #location of point
    lonpt, latpt = m(xpt,ypt,inverse=True)
    m.plot(xpt,ypt,'bo')


    #makes a request to get the country the location is in
    url = f"http://dev.virtualearth.net/REST/v1/Locations/{lat},{lon}?"

    params = {
        "o":"JSON",
        "key":Bm_api_key,
    }

    response = requests.get(url,params=params)
    response.raise_for_status()
    try:
        country = response.json()["resourceSets"][0]["resources"][0]["address"]["countryRegion"]
        country = f" ({country})"
    except IndexError:
        country = ""    

    plt.text(xpt+100000,ypt+100000,f'ISS{country}')
    #saves the image
    plt.savefig(fname=fname)
    plt.close()
    
     


#get_map_view(56.992883,88.866512,fname="ISS_map_view")


def get_ISS_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude




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

    with open("jsons/clips.json") as f:
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

        with open("jsons/clips.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2)) 

