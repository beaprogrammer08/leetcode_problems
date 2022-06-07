# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 22:23:07 2022

@author: hp
"""
# searching 
# linear search
def search(list3,n):
    for i in range(0,len(list3)):
        if list3[i]==n:
            return True
        else:
            return False

list3=[1,2,21,23,122,34]

n=1

if search(list3, n):
    print("found")
else:
    print("not found")






list1=[1,2,21,23,122,34]

x=2
for i in range(0,len(list1)):
    if list1[i]==n:
        print("found")
        break
else:
    print("not found")



#binary search

num=int(input("enter no"))
my_list=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,18]
r=len(my_list)-1
l=0
for a in my_list:
    m=(l+r)//2
    if my_list[m]==num:
        print(m)
        print("found")
        break
    elif my_list[m]>num:
        r=m-1
    

    elif my_list[m]<num:
        l=m+1
else:
    print("sorry")




def search1(list2,a):
    l=0
    u=len(list2)-1
    while l<=u:
        mid=(l+u)//2
        if list2[mid]==a:
            return True
    
        elif list2[mid]<a:
                l=mid
        elif list2[mid]>a:
                u=mid
    else:
            False

list2=[1,2,3,4,5,6,7,8,9,10]


a=int(input("enter the number"))
if search1(list2,a):
    print("found")
else:
    print("not found")

        
        
        