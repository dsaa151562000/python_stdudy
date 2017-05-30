# #-*- coding: utf-8 -*-

array = [100,50,25,4,1]

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if array[j] < array[j-1]:
                tmp = array[j]
                array[j] = array[j-1]
                array[j-1] = tmp
                print(array)
                
bubble_sort(array)