# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 01:34:45 2023

@author: Alex
"""
from my_gdal_bib import *
import pymannkendall as mk
from sklearn.cluster import KMeans

def sen_slope(vals, confidence = 0.95):
    # https://github.com/manaruchi/MannKendall_Sen_Rainfall/blob/master/mann_sen.py
    alpha = 1 - confidence
    n = len(vals)
    
    box = np.ones((len(vals), len(vals)))
    box = box * 5
    boxlist = []
    
    for r in range(len(vals)):
        for c in range(len(vals)):
            if(r > c):
                box[r,c] = (vals[r] - vals[c]) / (r-c)
                boxlist.append((vals[r] - vals[c]) / (r-c))
    slope = np.median(boxlist)
    return slope

array,gdalData = read_geotiff(f"C:/Users/Alex/Desktop/Geo/data_for_geoportal_v2/Trend2016_2021_Water/W_Trend2016_clip.tif")
dataset = np.array([array])
AllData = np.array([gdalData])
for a in range(17,23):
    array,gdalData = read_geotiff(f"C:/Users/Alex/Desktop/Geo/data_for_geoportal_v2/Trend2016_2021_Water/W_Trend20{a}_clip.tif")
    dataset = np.append(dataset,[array], axis=0)
    AllData = np.append(AllData,[gdalData], axis=0)
print(dataset.shape,AllData.shape)
print(np.transpose(dataset,(1,2,0)).shape,AllData.shape)
size1,size2,size3 = np.transpose(dataset,(1,2,0)).shape
data_for_calculation = np.transpose(dataset,(1,2,0))
print(data_for_calculation[1500,4000])
print(mk.original_test(data_for_calculation[1500,4000])[3])
print(sen_slope(data_for_calculation[1500,4000]))
output = np.zeros((size1,size2))
for i in range (size1):
    for j in range (size2):
        output [i,j]= sen_slope(data_for_calculation[i,j])
    p = round((i*j)/(size1*size2)*100,3)
    print(p,"%",end=' ')
print("END")  

witout_w = lambda array: np.where((array != 39) & (~np.isnan(array)) & (array != -32768) & (array != array[0][0]));     
Maximum = np.nanmax(output[array_without_w]);
Minimum = np.nanmin(output[array_without_w]);
print (Maximum, Minimum)
array = output.copy()
array_without_w = witout_w (array)
array[np.isnan(array)]=-32768
array[np.where(array == array[0][0])]=-32768
print("Start K means")
n = 3
kmeans = KMeans(n_clusters=n)
kmeans.fit(array[array_without_w].reshape(-1, 1))
c=np.array(kmeans.labels_)
print(np.unique(c)-n//2)
#array = array[]
array[array_without_w] = c-n//2
#print(map(mk.original_test,data_for_calculation))
#array2 = output.copy()
#array2[array_without_w] = c-n//2
#from tempfile import TemporaryFile
#outfile = TemporaryFile()

with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Poductivity_Trend_our_2016_2022_{n}_array.npy', 'wb') as f:
    np.save(f, output)
with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Poductivity_Trend_our_2016_2022_{n}_array.npy', 'rb') as f:
    array = np.load(f)
    print (array)   
    #b = np.load(f)
    #print (b) 
    

array[np.isnan(array)]=-32768
array[np.where(array == 39)]=-32768
array[np.where(array == array[0][0])]=-32768
array_without_w = witout_w (array)
print(array[array_without_w].size)
Maximum = np.nanmax(array[array_without_w]); Minimum = np.nanmin(array[array_without_w])
print(f"Max:{Maximum} Min:{Minimum}")
    
array[np.where((0 <= array) & (array <= Maximum))] /= Maximum
array[np.where((Minimum <= array) & (array <= 0))] /= -Minimum
Maximum = np.nanmax(array[array_without_w]); Minimum = np.nanmin(array[array_without_w])
print(f"Max:{Maximum} Min:{Minimum}")
print(array)
c = 0.0075
array[np.where((-1 <= array) & (array <= -c))] = -1
array[np.where((-c < array) & (array < c))] = 0
array[np.where((c < array) & (array <= 1))] = 1

write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Poductivity_Trend_our_2016_2022_{n}_{c}.tif", array, gdalData)
def Productivity_Trajectory (array3):
    size1,size2 = array3.shape
    array3 = np.array (array3)    
    #output=np.zeros(shape=(size1,size2),dtype='uint8')
    result = mk.original_test(array3.reshape(-1, 1))
    print(result)
#Productivity_Trajectory (array3)