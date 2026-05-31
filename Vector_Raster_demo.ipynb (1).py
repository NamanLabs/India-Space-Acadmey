#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("welcome to Python GIS Practical")


# In[2]:


5+10


# In[3]:


get_ipython().system('pip install geopandas matplotlib pandas')


# In[4]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


gdf = gpd.read_file(r"C:\Users\ASUS\Desktop\ISA\India_Districtboundary\2011_Dist.shp")


# In[6]:


gdf.head()


# In[7]:


gdf.columns


# In[8]:


gdf.crs


# In[9]:


gdf.plot()
plt.show()


# In[10]:


gdf.plot(color="lightgreen", edgecolor="black", figsize=(10,10))
plt.title("India District Boundary")
plt.show()


# In[11]:


jaipur = gdf[gdf["district"] == "Jaipur"]


# In[12]:


jaipur = gdf[gdf["DISTRICT"] == "Jaipur"]


# In[13]:


jaipur.plot(color="orange", edgecolor="black", figsize=(6,6))
plt.title("Jaipur District")
plt.show()


# In[14]:


gdf_utm = gdf.to_crs(epsg=32643)


# In[15]:


gdf_utm["area_sqkm"] = gdf_utm.geometry.area / 1000000


# In[16]:


gdf_utm[["area_sqkm"]].head()


# In[17]:


gdf_utm[["DISTRICT", "area_sqkm"]].head()


# In[18]:


gdf_utm[["DISTRICT", "area_sqkm"]].head()


# In[19]:


jaipur.to_file("Jaipur_District.shp")


# In[20]:


import os
os.getcwd()


# In[21]:


jaipur_buffer = jaipur.to_crs(epsg=32643)
jaipur_buffer["geometry"] = jaipur_buffer.buffer(10000)


# In[22]:


jaipur_buffer.plot(color="lightblue", edgecolor="black", figsize=(6,6))
plt.title("10 km Buffer Around Jaipur")
plt.show()


# In[23]:


import rasterio
import numpy as np
import matplotlib.pyplot as plt


# In[24]:


raster = rasterio.open(r"C:\ISA\lulc_ind_2023")


# In[25]:


raster = rasterio.open(r"C:\ISA\lulc_ind_2023")


# In[26]:


import rasterio

raster = rasterio.open(r"C:\ISA\lulc_ind_2023")


# In[27]:


import rasterio

raster = rasterio.open(r"C:\Users\ASUS\Desktop\ISA\lulc_ind_2023")


# In[28]:


raster = rasterio.open(r"C:\Users\ASUS\Desktop\ISA\2nd_Summer_Internship_Programme\lulc_ind_2023")


# In[29]:


print(raster)


# In[30]:


print(raster.meta)


# In[31]:


band1 = raster.read(1)


# In[32]:


read(1)


# In[33]:


print(band1)


# In[34]:


plt.imshow(band1)
plt.title("LULC Raster")
plt.colorbar()
plt.show()


# In[35]:


plt.figure(figsize=(8,8))
plt.imshow(band1, cmap="terrain")
plt.title("LULC Raster Map")
plt.colorbar(label="Land Cover Classes")
plt.show()


# In[36]:


np.unique(band1)


# In[ ]:




