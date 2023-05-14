
from geopy.geocoders import Nominatim
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Saralai")#Saralai(vijayamangalam) | Mavelipalaiyam (Sankagiri)
a=getLoc.latitude
b=getLoc.longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)

locname = loc.reverse("{},{}".format(a,b)) #"{},{}".format(a,b)
print(locname.address)
string = locname.address
res=[]
for i in string.split(','):
    res.append(i)
#res= string.split(',')
print(res[1].strip())
def loc():
    return res[1].strip()
