# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from my_gdal_bib import *


test_copy_create()
  
array1,gdalData1 = read_geotiff("C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Land_cover/Land_cover_2021.tif")
array2,gdalData2 = read_geotiff("C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Land_cover/Land_cover_2022.tif")
bands = ['0 Forest','1 Grassland','2 Cropland', '3 Wetland', '4 Artificial', '5 Bareland','6 Damaged areas/Not cultivated','7 Water']
def Land_Cover_Change (array1,gdalData1,array2,gdalData2):
    size1,size2 = array1.shape
    array1 = np.array (array1, np.int32)
    array2 = np.array (array2, np.int32)
    coefficients = np.array([
      [ 0,-1,-1,-1,-1,-1,-1, 0],#1
      [ 1, 0, 1,-1,-1,-1,-1, 0],#2
      [ 1,-1, 0,-1,-1,-1,-1, 0],#3
      [-1,-1,-1, 0,-1,-1,-1, 0],#4
      [ 1, 1, 1, 1, 0,-1,-1, 0],#5
      [ 1, 1, 1, 1, 1, 0, 1, 0],#6
      [ 1, 1, 1, 1, 1,-1, 0, 0],#7
      [ 0, 0, 0, 0, 0,-0, 0, 0],#8
      ])
        #1 #2 #3 #4 #5 #6 #7 #8
    output=array1.copy()
    output [np.where((0 == array1) | (0 == array2))] = -32768
    for i in range(0,len(coefficients)):
        for j in range(0,len(coefficients[0])):
            a = coefficients[i][j]
            output [np.where((i+1 == array1) & (j+1 == array2))] = a
        p = round((i*j)/(len(coefficients)*len(coefficients[0]))*100,3)
        print(p,"%",end=' ')
    return output
print ("Start calculation")
output = Land_Cover_Change (array1,gdalData1,array2,gdalData2)
write_geotiff("C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Land Cover Change/LCC_2022.tif", output, gdalData1)
print ("END of LCC")



    