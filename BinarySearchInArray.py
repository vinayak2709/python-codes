# Python code to demonstrate working
# of binary search in library
from bisect import bisect_left
from bisect import bisect_right


def BinarySearch1st(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def BinarySearchlast(a, x):
    i = bisect_right(a, x)
    if  i != len(a) and a[i] >= x:
        return i-1
    else:
        return -1


def BinarySearch2nd(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i+1] == x:
        return i+1
    else:
        return -1


def LeftmostGreater(a, x):
    #'Find leftmost value greater than x' x=3 then. [ 1 , 2 ,3 ,3, 5, 7] leftmostgreater 5  & rightmostGrt is a[len(a)-1]

    i = bisect_right(a, x)      #keep right side of x in list for checking
    if i != len(a):
        return a[i]
    else :
        print("there is no greater element than x")


def RightmostLess(a, x):
    #'Find rightmost value less than x'
    i = bisect_left(a, x)    #keep left side of x in list for checking
    if i:
        return a[i-1]
    else :
        print("there is no lesser element than x")


a = [1, 6, 7,0 ,4, 4,4,4,4,4, 8, 9]
a.sort()                                          # array sorting in ascending order
print(a)

b= a[::-1]                                        #array reverse
print(b)


x = int(4)
res = BinarySearch1st(a, x)                       #search array for integer value 4 for 1st occurrence

if res == -1:
    print(x, "is absent")
else:
    print("after sorting First occurrence of", x, "is present at", res )

occ = BinarySearch2nd(a, x)                         #search array for integer value 4 for 2nd occurrence

if occ == -1 :
    print(x," 2nd occurrence absent")
else :
    print("2nd occurrence at   " , occ)

rl = RightmostLess(a, x)
lg = LeftmostGreater(a, x)
lge=  BinarySearchlast(a, x)

print(" RightMost less no  ", rl,"   LeftMostGreater no   ",lg ,"    Last occurance ",lge)