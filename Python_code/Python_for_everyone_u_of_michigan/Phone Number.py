import phonenumbers

import opencage

import folium

from aa import number

from phonenumbers import geocoder

key = 'e8d391b6be7c4bad9ea0c4b8082d427b'

ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")

yourlocation = geocoder.description_for_number(service_nmber, "en")

print(carrier.name_for_number(service_nmber, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourlocation)

results = geocoder.geocode(query)

#print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup= yourlocation).add_to((myMap))

myMap.save("myLocation.html")
