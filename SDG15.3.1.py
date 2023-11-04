# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 05:16:50 2023

@author: Alex
"""
import skimage.transform as st
from my_gdal_bib import *
start1,start2 = 16,20
end1,end2 = 22,22
c = 0.0075
a = 22
n = 3
array1,gdalData1 = read_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Poductivity_our_20{a}_Interval_{c}.tif")
array2,gdalData2 = read_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Land Cover Change/LCC_2022.tif")

array1 = st.resize(array1, array2.shape, mode='constant')
print(array1.shape,array2.shape)
size11,size12 = array2.shape
output = np.zeros((size11,size12))
output[np.where(output == 0)] = -32768
print("Output -32768")
output[np.where((output == -32768) & ((array1 == -1) | (array2 == -1)))] = -1
output[np.where((output == -32768) & ((array1 == 1) | (array2 == 1)))] = 1
output[np.where((output == -32768) & ((array1 == 0) | (array2 == 0)))] = 0
print("Save array")
with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/SDG_{c}_array.npy', 'wb') as f:
    np.save(f, output)
with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/SDG_{c}_array.npy', 'rb') as f:
    output = np.load(f)
    print (array)  
print("Saved array and downloaded")    
write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/SDG/SDG_{c}.tif", output, gdalData2)
 
