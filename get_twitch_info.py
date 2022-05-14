import requests
from dotenv import load_dotenv
import os 
load_dotenv()





secret = ""
secret = os.getenv("secret") 


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
#get_info("Kennevo")



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
    #print(is_streaming)
    return is_streaming
   
#kenny_live()