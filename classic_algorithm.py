# #-*- coding: utf-8 -*-

def linear_search(val,aList):
    for x in aList:
        if x == val:
            return aList.index(val)
    return None

numbers = [1,3,5,11,12,13,17,22,25,28]
print(numbers)
print('探したい数字を入力してください')
goal_number = int(input())

print(linear_search(goal_number, numbers))