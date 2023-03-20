#!/usr/bin/env python
# coding: utf-8

# In[269]:


#cartesian coordinate
import numpy as np
import math
from sympy import *


# In[270]:


# origin=np.array(
#     [[0.025018771, -0.666666491, -0.069178623],
# [-0.333333219, -0.025018581, -0.930821805],
# [0.308314611, -0.666666771, -0.930821805]])
# tran=origin.T
# print(tran)
# normal1=tran
# print(normal1)


# In[271]:


normal1 = np.array(
 [[1.266096729,-1.88673908,1.591099143],
  [2.267013917,-0.153102575,-1.591107369],
[5.800123299,-1.886739809,-1.591107369]])


# In[272]:


a1=normal1[0]
a2=np.array([1, 0, 0])
l_a1=np.sqrt(a1.dot(a1))
l_a2=np.sqrt(a2.dot(a2))
print(a1)
print(l_a1)
print(l_a2)


# In[273]:


basis1 = np.array(
    [[1, 0, 0],
[0, 1, 0],
[0, 0, 1]])


# In[274]:


#求normal1的模长
data_M = np.sqrt(np.sum(normal1*normal1,axis=1))
a1_=data_M[0]
a1__=data_M[1]
a1___=data_M[2]
print(data_M)
print(a1_)
# norm_datam=a1/data_M
# print(norm_datam)


# In[275]:


#求normal2的模长
data_N = np.sqrt(np.sum(normal2*normal2,axis=1))
print(data_N)


# In[276]:


#对整个normal1进行正交化，并求出新的Z方向轴
nor_a1_=normal1[0]/a1_
nor_a1__=normal1[1]/a1__
nor_a1___=normal1[2]/a1___
print(nor_a1_)
#print(nor_a1__)
#print(nor_a1___) #不需要这个
#验证x和y方向是不是单位向量
x=np.sqrt(np.sum(nor_a1_.dot(nor_a1_)))
y=np.sqrt(np.sum(nor_a1__.dot(nor_a1__)))
print(x)
print(y)
#在x基础上得到与x垂直的y向量
a2=nor_a1__-nor_a1_.dot(nor_a1__)/(nor_a1_.dot(nor_a1_))*nor_a1_
print(a2)
#得到新的z向量
z=np.cross(nor_a1_,a2)
print(z)
#计算z向量的模长和新的y向量的模长
z_z=np.sqrt(np.sum(z.dot(z)))
a2_a2=np.sqrt(np.sum(a2.dot(a2)))
print(z_z)
print(a2_a2)
#test验证是否xyz互相垂直
xy=nor_a1_.dot(a2)
xz=nor_a1_.dot(z)
yz=a2.dot(z)
print(xy)
print(xz)
print(yz)


# In[277]:


#以自己定的三个轴为新的坐标系basis2, 新的i,j,k
basis2=np.array([nor_a1_,a2,z])
print(basis2)


# In[278]:


#RA=B
basis1_inver=np.linalg.inv(basis1)
print(basis1)
R=np.matmul(basis2.T,basis1_inver)
print(R)
#Rzxy,Zphi,Ytheta,xposi,求出来的角度需要按XYZ轴开始绕
theta1=np.degrees(-np.arcsin(R[2,0]))
theta2=180-theta1
posi1=np.degrees(math.atan2(R[2,1]/np.cos(np.deg2rad(theta1)),R[2,2]/np.cos(np.deg2rad(theta1))))
posi2=np.degrees(math.atan2(R[2,1]/np.cos(np.deg2rad(theta2)),R[2,2]/np.cos(np.deg2rad(theta2))))
phi1=np.degrees(math.atan2(R[1,0]/np.cos(np.deg2rad(theta1)),R[0,0]/np.cos(np.deg2rad(theta1))))
phi2=np.degrees(math.atan2(R[1,0]/np.cos(np.deg2rad(theta2)),R[0,0]/np.cos(np.deg2rad(theta2))))
print('第1组绕ZYX角度为,phi1,theta1,posi1:',phi1,theta1,posi1)
print('第2组绕ZYX角度为,phi2,theta2,posi2:',phi2,theta2,posi2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




