#RENAME
import os
path = 'D:/EVA/Assignment19/Images'
files = os.listdir(path)
i = 1

for file in files:
    print(file)
    if (i<10):
        os.rename(file,"img_00" + str(i) +'.jpg')
    else:
        os.rename(file,"img_0" + str(i) +'.jpg')
    i = i+1    

#RESIZE    
from PIL import Image    
files = os.listdir(path)

for file in files:
    print(file)
    img = Image.open(file)
    img = img.resize((400,400))
    img.save(file)


#RETRIEVING HEIGHT AND WIDTH VALUES FROM JSON    
import pandas as pd
data = pd.read_json("via_project_final.json")
img_data = data['_via_img_metadata']
width_list = []
height_list = []

for key,value in img_data.items():
    if('img' in key):
        for i,j in value.items():
            if(isinstance(value[i],list)):
                for i in value[i]:
                    for a,b in i.items():
                        for c,d in b.items():
                            if('width' in c):
                                width_list.append(d)
                            elif('height' in c):
                                height_list.append(d)

#NORMALIZING DATASET
height_new_list = [x / 400 for x in height_list]
width_new_list = [x / 400 for x in width_list]

#CONVERTING LIST INTO DATAFRAME
hw = pd.DataFrame()
hw['height'] = height_new_list
hw['width'] = width_new_list

#APPLYING K-MEANS
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(hw)

#FINDING CLUSTER CENTERS
centers = kmeans.cluster_centers_
centers_upscaled = [x * 400 for x in centers]
print(centers_upscaled)