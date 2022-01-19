#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:42:27 2022

@author: nguyennich
"""

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

a = [1, 2, 4, 7, 8, 12, 15]

b = naive_search(a, 4)
print("the location of 4 is ", b)
# 4 parameters, a is the array, target, low is bottom index, high it top inddex
def binary_search(a, target, low=None, high=None):
    #sets top and bottom limits for array index if None
    if low is None:
        low = 0    
    if high is None:
        high = len(a) - 1
    #when target is not in array, -1 will be returned
    if high < low:
        return -1
    #finds midpoint of array, if odd number of items uses bottom limit
    mid = (low + high)//2
    #returns midpoint if it is target otherwise changes to greater or lesser half of list
    if a[mid] == target:
        return mid
    elif target < a[mid]:
        return binary_search(a, target, low, mid -1)
    else:
        return binary_search(a, target, mid+1, high)

print("the location of 4 is ", binary_search(a, 4))
    
    
    