from geopy import geocoders # $ pip  install geopy

g = geocoders.GoogleV3()
place, (lat, lng) = g.geocode('Tokyo')
timezone = g.timezone((lat, lng)) # return pytz timezone object
print(timezone.zone)