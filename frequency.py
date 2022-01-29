# Finding frequency of each element in a list

from collections import Counter

my_list = ['a','a','a','a','a','b','c','c','c','c','c','d','d','d','d']
count = Counter(my_list) 

print(count) # ALL ELEMENTS

print(count['c']) # One Element

print(count.most_common(1)) # Most Frequent
                    #1,2,3 elements 
