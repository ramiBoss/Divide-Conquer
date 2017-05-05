#!/usr/bin/python
# Author : Ramiz Khan
# GitHub : www.github.com/ramiBoss

# Recurrance Relation : { T(n/2)+1 if n>1,
#                         0 if n=1
#                        }
# A recursive program that uses divide & conquer technique to calculate the solution of a number raisesd to the power
def power(num, powr):
    if(powr == 1):
        return num
    else:
        numB = power(num, int(powr/2))
        numB = numB*numB
        return numB

def main():
    print 'Enter integer and its power number :\n'
    num = raw_input()
    powr = raw_input()
    if(num == 0):
        print 'Output : ', int(num)
        return
    if(powr == 0):
        print 'Output : ', 1
        return
    print 'Output : ',power(int(num), int(powr))
    return

if __name__ == '__main__':
    main()
