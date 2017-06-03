# #-*- coding: utf-8 -*-

numbers = [1,3,5,11,12,13,17,22,25,28]
print(numbers)
print('探したい数字を入力してください')
goal_number = int(input())

def binary_search(numbers, goal_number):
    low = 0
    high = len(numbers)

    t = (low + high) / 2 

    while (low<=high):
       try:
         if (goal_number==numbers[t]):
                  break
         elif (goal_number > numbers[t]):
                  low = t + 1
         elif (goal_number < numbers[t]):
                  high = t - 1
         t = (low + high) / 2
       except IndexError:
         break
            
    try:
      if (goal_number==numbers[t]):
        print str(t + 1)
    except IndexError:
        print "None"

binary_search(numbers, goal_number)