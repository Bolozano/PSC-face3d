import datetime
import os
import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytorch
#data = pd.HDFStore('model2019_fullHead.h5','r')
#data.describe()
#print(data.__class__)
data= h5py.File('model2019_fullHead.h5','r')
def print_name(name):
    print(name)
data.visit(print_name)
'''print(list(data.keys()))'''
shape_data=data['shape']
#print(shape_data.__class__)
print(list(shape_data.keys()))
model_data=shape_data['model']
'''modelinfo=shape_data['modelinfo']
print(list(modelinfo.keys()))'''
representer=shape_data['representer']
print(list(representer.keys()))
cells=representer['cells']
cells=np.array(cells)
'''sdkmds=pd.DataFrame(cells)
print(sdkmds.describe())'''
print(cells.shape)
points=representer['points']
points=np.array(points)
print(points.shape)
'''sdmds=pd.DataFrame(points)
print(sdmds.describe())'''
'''version=shape_data['version']
print(list(version.keys()))
#print(model_data.__class__)'''
print(list(model_data.keys()))
mean=model_data['mean']
#print(mean.__class__)
#print(mean.shape)
mean=np.array(mean).reshape(-1,1)
print(mean.shape)
'''cslncs=pd.DataFrame(mean)
print(cslncs.describe())'''
noiseVariance=model_data['noiseVariance']
#print(noiseVariance[0])
noiseVariance=np.array(noiseVariance).reshape(-1,1)
#print(noiseVariance.shape)
pcaBasis=model_data['pcaBasis']
pcaBasis=np.array(pcaBasis)
print(pcaBasis.shape)
pcaVariance=model_data['pcaVariance']
pcaVariance=np.array(pcaVariance).reshape(1,-1)
print(pcaVariance.shape)
#data.   printname()
