'''trip={
    "trip_id":"ub12345",
    "pickup":"chennai central",
    "drop":["airport","hotel"],
     "fare":430.75,
    "trip_id":"ub12345",
}

"""print (trip)
print(trip["pickup"])   
print(trip.get("airport"))
 
print(trip.keys())
print(trip.values()) """

#for key,value in trip.items():
#    print(key, ":", value)

trip.update({"car-model":"suzuki"})
print(trip)
 
 
print(trip["drop"][1])

for location in trip["drop"]:
    print(location)
   ''' 

trips={
    "123":{"trip_id":123,"pickup":"chennai central","drop":"airport"},
    "456":{"trip_id":456,"pickup":"trichy","drop":"airport"},
}    

'''for trip in trips:
    print(trip["trip_id"])'''
    
    
for trip_id,details in trips.items():
    print(trip_id)
    print(details["pickup"],"->",details["drop"])    