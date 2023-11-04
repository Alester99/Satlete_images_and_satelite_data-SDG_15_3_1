# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:00:37 2023

@author: Alex
"""

from my_gdal_bib import *

start1,start2 = 16,20
end1,end2 = 22,22
#witout_w = lambda array: np.where((array != 39) & (~np.isnan(array)) & (array != array[0][0]));  
def data_for_period (start,end):
    array,gdalData = read_geotiff(f"C:/Users/Alex/Desktop/Geo/data_for_geoportal_v2/Trend2016_2021_Water/W_Trend20{start}_clip.tif")
    array[np.isnan(array)]=-32768
    array[np.where(array == array[0][0])]=-32768
    array[np.where(array == 39)]=-32768
    dataset = np.array([array])
    AllData = np.array([gdalData])
    for a in range(start,end+1):
        array,gdalData = read_geotiff(f"C:/Users/Alex/Desktop/Geo/data_for_geoportal_v2/Trend2016_2021_Water/W_Trend20{a}_clip.tif")
        dataset = np.append(dataset,[array], axis=0)
        AllData = np.append(AllData,[gdalData], axis=0)
        print(a)
    #print(dataset.shape,AllData.shape)
    #print(np.transpose(dataset,(1,2,0)).shape,AllData.shape)
    size1,size2,size3 = np.transpose(dataset,(1,2,0)).shape
    data_for_calculation = np.transpose(dataset,(1,2,0))
    #output = np.zeros((size1,size2))
    return data_for_calculation, AllData, size1,size2,size3
print("DATA_1")
data_for_calculation1, AllData1, size11,size12,size13 = data_for_period (start1,end1)
print("DATA_2")
data_for_calculation2, AllData2, size21,size22,size23 = data_for_period (start2,end2)

def mu (array): return np.sum(array)/(array.size)
def sigma (array,mu): return np.sqrt(np.sum(np.square(array-mu))/array.size) 
def x_m (array): return np.sum(array)/(array.size)

def Z (array1,array2): 
    m = mu (array1)
    s = sigma (array1,m)
    x = x_m (array2)
    return (x - m)/(s/np.sqrt(array2.size))

print(data_for_calculation1[0][0].size)
output = np.zeros((size11,size12))
for i in range(size11):
    for j in range(size12):
        d1 = data_for_calculation1[i,j];d2 = data_for_calculation2[i,j]
        if -32768 not in d1: output[i,j] = Z(data_for_calculation1[i,j],data_for_calculation2[i,j])
        else: output[i,j] = -32768
    p = round((i*j)/(size11*size12)*100,3)
    print(p,"%",end=' ')
print("END")  


with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Productivity_State_{start1}_{end1}_{start2}_{end2}_array_1.npy', 'wb') as f:
    np.save(f, output)
with open(f'C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/arrays/Productivity_State_{start1}_{end1}_{start2}_{end2}_array_1.npy', 'rb') as f:
    output = np.load(f)
    print (output) 
c = 0.0075
output[np.where(output<=-32768)] = -32768  
output[np.where((2 <= output) & (output <= 2))] = 0 
output[np.where((2 < output) & (output <= 3))] = 1
output[np.where((-3 <= output) & (output < -2))] = -1      
write_geotiff(f"C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Productivity/Productivity_State_{start1}_{end1}_{start2}_{end2}_{c}.tif", output, AllData1[0])
    #b = np.load(f)
    #print (b) 
#m = mu(data_for_calculation1[1500,4000])
#s = sigma (data_for_calculation1[1500,4000],m)
#x = x_m (data_for_calculation2[1500,4000])
#print(m,s,x)
#print(data_for_calculation1[1500,4000],data_for_calculation2[1500,4000])
#print(Z(data_for_calculation1[1500,4000],data_for_calculation2[1500,4000]))

