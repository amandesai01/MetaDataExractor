#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image
from PIL.ExifTags import TAGS


# In[30]:


def getMetaData(imgname):
    print("Requesting Img file")
    try:
        imgFile = Image.open(imgname)
        print("Image Found")
    except:
        print("File Not found")
    print("Requesting Meta Data")
#     try:
    metaData = {}
    info = imgFile._getexif()
    if info:
        print("Found MetaData\n************\n\n")
        for(tag, value) in info.items():
            tagname = TAGS.get(tag, tag)
            metaData[tagname] = value
            
        return metaData
#     except:
#         print("Failed")


# In[33]:


imgname = input()
metadata = getMetaData(imgname)
# now, complete metadata of an image is stored in "metadata" array.


# In[ ]:




