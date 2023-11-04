# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:07:46 2023

@author: Alex
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from osgeo import ogr
#from osgeo import osr
#from osgeo import gdal_array
#from osgeo import gdalconst

def read_geotiff(filename):
    gdalData = gdal.Open(filename)
    if gdalData is None:
      print ("ERROR: can't open raster")
    band = gdalData.GetRasterBand(1)
    array = band.ReadAsArray()
    return array, gdalData
      
def write_geotiff(filename, arr, in_ds):
    if arr.dtype == np.float32:
        arr_type = gdal.GDT_Float32
    else:
        arr_type = gdal.GDT_Int32
    driver = gdal.GetDriverByName("GTiff")
    out_ds = driver.Create(filename, arr.shape[1], arr.shape[0], 1, arr_type)
    out_ds.SetProjection(in_ds.GetProjection())
    out_ds.SetGeoTransform(in_ds.GetGeoTransform()) 
    band = out_ds.GetRasterBand(1)
    band.WriteArray(arr)
    band.FlushCache()
    band.ComputeStatistics(False)
    
def show_info (array,gdalData):
    array = gdalData.GetRasterBand(1).ReadAsArray()
    print(array.shape)
    print(gdalData.RasterCount)
    print(gdalData.GetProjection())
    print(gdalData.GetGeoTransform())
    print(gdalData.GetDriver().ShortName)
    print(gdalData.GetDriver().LongName)
    
def test_copy_create():
    format = "GTiff"
    driver = gdal.GetDriverByName( format )
    metadata = driver.GetMetadata()
    #print(metadata)
    #print(gdal.DCAP_CREATE)
    if gdal.DCAP_CREATE in metadata and metadata[ gdal.DCAP_CREATE ] == "YES":
      print ("Pass")
      pass
    else:
      print ("Driver %s does not support Create() method." % format)
      sys.exit( 1 )
    # аналогично выполняется проверка для CreateCopy
    if  gdal.DCAP_CREATECOPY in metadata and metadata[ gdal.DCAP_CREATECOPY ] == "YES":
      print ("Pass")  
      pass
    else:
      print ("Driver %s does not support CreateCopy() method." % format)
      sys.exit( 1 )
      
 #gdalData = gdal.Open( "C:/Users/Alex/Desktop/SDG 15.3.1_2020_2021/Land_cover/Land_cover_2019_no_degradation_areas.tif", gdal.GA_ReadOnly)
 #if gdalData is None:
 #  print ("ERROR: can't open raster")

 #print (gdal.__file__)
 #print (ogr.__file__)
 #GT_input = gdalData.GetGeoTransform()
 #array = gdalData.GetRasterBand(1).ReadAsArray()    