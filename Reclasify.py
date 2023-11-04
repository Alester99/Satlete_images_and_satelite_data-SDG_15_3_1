# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:23:48 2023

@author: Alex
"""

from my_gdal_bib import *
bands = ['1 Forest','2 Grassland','3 Cropland', '4 Wetland', '5 Artificial', '6 Bareland','7 Damaged areas/Not cultivated','8 Water'] 
a = 21
print ("START")
array,gdalData = read_geotiff(f"C:/Users/Alex/Desktop/Geo/data_for_geoportal_v2/maps/20{a}_major_50m_comp.tif")
size1,size2 = array.shape
output = array.copy()
output [np.where(array == 1)] = 5
output [np.where((2 <= array) & (array <= 9))] = 3
output [np.where(array == 10)] = 1
output [np.where(array == 11)] = 2
output [np.where(array == 12)] = 6
output [np.where(array == 13)] = 8
output [np.where(array == 14)] = 4
output [np.where(array == 18)] = 1
output [np.where((19 <= array) & (array <= 21))] = 3
output [np.where((22 <= array) & (array <= 23))] = 7
write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Land_cover/Land_cover_20{a}.tif", output, gdalData)
print ("END")
#print(output[int(size1/2)][int(size2/2)])
#print(write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Land_cover/Land_cover_20{a}", output, gdalData))
