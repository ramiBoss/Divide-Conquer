#!/usr/bin/python

# Author : Ramiz Khan
# GitHub : www.github/ramiBoss
# This programs uses divide & conquer technique to find out the minimum and maximum element in an array


# maxMin funtion is recursively called to sub-divide the array and to find max and min in each sub-array
def maxMin(i,j,Max, Min):
    if(i == j):
        Max = Min = array[i]
        return Max, Min
    elif(i == j-1):
        if(array[i] > array[j]):
            Max = array[i]
            Min = array[j]
            return Max, Min
        else:
            Max = array[j]
            Min = array[i]
            return Max, Min
    else:
        mid = int((i+j)/2)
        Max, Min = maxMin(i,mid,Max,Min)
        Max1, Min1 = maxMin(mid, j, Max, Min)
        if(Max1 > Max):
            Max = Max1
        if(Min1 < Min):
            Min = Min1           
    return Max, Min


def main():
    global array
    array = []
    print 'Enter the array elements, type -1 end the array'
    while True:
        n = raw_input()
        if(int(n) == -1):
            break
        else:
            array.append(int(n))
    Max, Min = maxMin(0, len(array)-1, 0, 0)
    print 'Max : ', Max, 'Min : ', Min
    return

if __name__ == '__main__':
    main()
