# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:34:07 2022

@author: hp
"""

#sorting 

#selection sort

my_list=[12,321,21,34,56,67,675,53]



for n in range(0,len(my_list)):
    for i in range(n,len(my_list)):
        if my_list[n]>my_list[i]:
            my_list[i],my_list[n]=my_list[n],my_list[i]

print(my_list) 
              
my_list1=[1,4,35,56,542,57,587,567,7876,565]

for n in range(0,len(my_list1)):
    for i in range(n,len(my_list1)):
        if my_list1[n]>my_list1[i]:
            my_list1[i],my_list1[n]=my_list1[n],my_list1[i]
print(my_list1)

# bubble sort 

my_list2=[1,9,3,8,23,97,4,35,56,542,57,587,567,7876,565]

for i in range(0,len(my_list2)-1):
    for j in range(0,len(my_list2)-i-1):
         if my_list2[j]>my_list2[j+1]:
               my_list2[j],my_list2[j+1]=my_list2[j+1],my_list2[j]
print(my_list2)