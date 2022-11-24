import numpy as np
import pandas as pd
import googlemaps

data = pd.read_csv("./final_data.csv")
distData = pd.DataFrame(columns=['id', 'address', 'currLat', 'currLong', 'near1Lat', 'near1Long', 'near2Lat', 'near2Long', 'near3Lat', 'near3Long', 'dist1', 'dist2', 'dist3'])
client = googlemaps.Client("AIzaSyAGc43A4dpybKPOQeslXHrXJNNu8I0fYFA")
id = 0
for idx, row in data.iterrows():
    currLat, currLong = row["lat_address;long_address"].split(";")
    near1Lat, near1Long = row["lat_nearby1;long_nearby1"].split(";")
    near2Lat, near2Long = row["lat_nearby2;long_nearby2"].split(";")
    near3Lat, near3Long = row["lat_nearby3;long_nearby3"].split(";")
    
    
    # print(currLat, currLong)
    
    matrix = client.distance_matrix((currLat, currLong), (near1Lat, near1Long), mode="driving", units="imperial")
    dist1 = float(matrix['rows'][0]['elements'][0]['distance']['text'].split(" ")[0])
    matrix = client.distance_matrix((currLat, currLong), (near2Lat, near2Long), mode="driving", units="imperial")
    dist2 = float(matrix['rows'][0]['elements'][0]['distance']['text'].split(" ")[0])
    matrix = client.distance_matrix((currLat, currLong), (near3Lat, near3Long), mode="driving", units="imperial")
    dist3 = float(matrix['rows'][0]['elements'][0]['distance']['text'].split(" ")[0])
    
    distData.loc[len(distData.index)] = [id, row["address"], currLat, currLong, near1Lat, near1Long, near2Lat, near2Long, near3Lat, near3Long, dist1, dist2, dist3]
    # tempdf = pd.DataFrame(dict({'id': id, 'address': row["address"], 'currLat': currLat, 'currLong': currLong, 'near1Id': 0, 'near2Id': 0, 'near3Id': 0, 'dist1': dist1, 'dist2': dist2, 'dist3': dist3}))
    # newData = pd.concat([newData, tempdf], ignore_index=True)
    id += 1
    # if id == 20: break
    
id = 0
finalData = pd.DataFrame(columns=['id', 'address', 'currLat', 'currLong', 'near1Id', 'near2Id', 'near3Id', 'dist1', 'dist2', 'dist3'])
for idx, row in distData.iterrows():
    near1Id = list(distData.loc[(distData['currLat'] == row["near1Lat"]) & (distData['currLong'] == row["near1Long"])]["id"])
    near2Id = list(distData.loc[(distData['currLat'] == row["near2Lat"]) & (distData['currLong'] == row["near2Long"])]["id"])
    near3Id = list(distData.loc[(distData['currLat'] == row["near3Lat"]) & (distData['currLong'] == row["near3Long"])]["id"])
    
    if len(near1Id) == 0: near1Id = [-1]
    if len(near2Id) == 0: near2Id = [-1]
    if len(near3Id) == 0: near3Id = [-1]
    finalData.loc[len(finalData.index)] = [id, row["address"], row["currLat"], row["currLong"], near1Id[0], near2Id[0], near3Id[0], row["dist1"], row["dist2"], row["dist3"]]
    id += 1
   
print(finalData)
finalData.to_csv("final_data_dist.csv", encoding="utf-8", index="false")