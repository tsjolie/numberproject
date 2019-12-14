from functools import reduce
from operator import mul
from itertools import permutations
import math

def generate():
    nmlst2 = []
    j = 1
    magicnumber = 0
    answers=[]
    x = 277777788888899
    #x = 210
    cbn = math.factorial(15)
    nmlst1 = permutations(str(x))
    for i in nmlst1:
	lst = convert(i)
	print(lst)
        if factor(lst)[-1] == 1: magicnumber = lst
	#nmlst2.append(lst)
        j += 1
        print("%2.10f " % (j / cbn))
        if magicnumber != 0: print(factor(magicnumber), magicnumber)

def persistence(number, count=0):
    # recursion base case - exit once the number is less than 10
    if number < 10:
        return count

    # get new number by multiplying digits of a number
    new_number = reduce(mul, map(int, str(number)))

    return persistence(new_number, count + 1)


#code I wrote to check the single digit prime factors of a number
def factor(y):
    i_2 = 0
    i_3 = 0
    i_5 = 0
    i_7 = 0
    while y % 2 == 0:
        y /= 2
        i_2 += 1
    while y % 3 == 0:
	y /= 3
	i_3 += 1
    while y % 5 == 0:
	y /= 5
	i_5 += 1
    while y % 7 == 0:
   	y /= 7
	i_7 += 1
    return(i_2, i_3, i_5, i_7, y)


# Python3 program to convert a list 
# of integers into a single integer 
def convert(list): 
      
    # Converting integer list to string list 
    s = [str(i) for i in list] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res) 
