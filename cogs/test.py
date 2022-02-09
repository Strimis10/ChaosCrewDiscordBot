import requests

TWITCH_STREAM_API_ENDPOINT_V5 = "https://api.twitch.tv/kraken/streams/Kennevo"
API_HEADERS = {
'Client-ID' : 'myClientID',
'Accept' : 'application/vnd.twitchtv.v5+json',
}

reqSession = requests.Session()

def checkUser(userID): #returns true if online, false if not
    url = TWITCH_STREAM_API_ENDPOINT_V5.format(userID)

    try:
        req = reqSession.get(url, headers=API_HEADERS)
        jsondata = req.json()
        if 'stream' in jsondata:
            if jsondata['stream'] is not None: #stream is online
                #print('online')
                return True
            else:
                return False
            #print('offline')
    except Exception as e:
        print("Error checking user: ", e)
        return False
        print(checkUser("bikestreaming"))