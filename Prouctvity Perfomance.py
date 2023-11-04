# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:01:05 2023

@author: Alex
"""

from my_gdal_bib import *
from sklearn.cluster import KMeans

witout_w = lambda array: np.where((array != 39) & (~np.isnan(array)) & (array != array[0][0]));
a = 22
#array,gdalData = read_geotiff(f"C:/Users/Alex/Desktop/Geo/data_for_geoportal_v2/Trend2016_2021_Water/W_Trend2022_clip.tif")
array,gdalData = read_geotiff(f"C:/Users/Alex/Desktop/Geo/data_for_geoportal_v2/Trend2016_2021_Water/W_Trend2022_clip.tif")

array_without_w = witout_w (array)
array[np.isnan(array)]=-32768
array[np.where(array == array[0][0])]=-32768
array[np.where(array == 39)]=-32768

Maximum = np.nanmax(array[array_without_w]); Minimum = np.nanmin(array[array_without_w])
print(f"Max:{Maximum} Min:{Minimum}")

with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Productivity_Perfomance{a}.npy', 'wb') as f:
    np.save(f, array)
with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Productivity_Perfomance{a}.npy', 'rb') as f:
    array= np.load(f)
    print (array) 
    
array[np.where((0 <= array) & (array <= Maximum))] /= Maximum
array[np.where((Minimum <= array) & (array <= 0))] /= -Minimum
Maximum = np.nanmax(array[array_without_w]); Minimum = np.nanmin(array[array_without_w])
print(f"Max:{Maximum} Min:{Minimum}")
print(array)
c = 0.0075
array[np.where((-1 <= array) & (array <= -c))] = -1
array[np.where((-c < array) & (array < c))] = 0
array[np.where((c < array) & (array <= 1))] = 1
write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Poductivity_our_20{a}_Interval_{c}.tif", array, gdalData)
#x1 
#output = array(np.where(array ))
#print("Start K means")
#n = 7
#kmeans = KMeans(n_clusters=n)
#kmeans.fit(array[array_without_w].reshape(-1, 1))
#c=np.array(kmeans.labels_)
#print(np.unique(c)-n//2)
#array = array[]
#array[array_without_w] = c-n//2
#write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Poductivity_our_20{a}_{n}.tif", array, gdalData)
