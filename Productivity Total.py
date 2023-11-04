# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 04:18:01 2023

@author: Alex
"""
from my_gdal_bib import *
start1,start2 = 16,20
end1,end2 = 22,22
c = 0.0075
a = 22
n = 3
array1,gdalData1 = read_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Poductivity_our_20{a}_Interval_{c}.tif")
array2,gdalData2 = read_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Productivity_State_{start1}_{end1}_{start2}_{end2}_{c}.tif")
array3,gdalData3 = read_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Poductivity_Trend_our_2016_2022_{n}_{c}.tif")

size11,size12 = array1.shape
output = np.zeros((size11,size12))
output[np.where(output == 0)] = -32768

output[np.where((output == -32768) & ((array1 == -1) | (array2 == -1) | (array2 == -1)))] = -1
output[np.where((output == -32768) & ((array1 == 1) | (array2 == 1) | (array2 == 1)))] = 1
output[np.where((output == -32768) & ((array1 == 0) | (array2 == 0) | (array2 == 0)))] = 0


with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Poductivity_Total_{c}_array.npy', 'wb') as f:
    np.save(f, output)
with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Poductivity_Total_{c}_array.npy', 'rb') as f:
    array = np.load(f)
    print (array)  
    
write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity//Poductivity_Total_{c}.tif", output, gdalData1)
