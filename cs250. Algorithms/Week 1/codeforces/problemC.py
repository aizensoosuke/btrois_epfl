#!/usr/bin/env python3

n = int(input())
x = [int(i) for i in input().split(' ')]
q = int(input())

x.sort()

def shops(m):
    def find(a, b): # dichotomie
        middle = a + (b - a)//2
        if(b - a <= 1):
            return a + 1
        elif(x[middle] > m):
            return find(a, middle)
        else:
            return find(middle, b)
    if(x[0] > m):
        return 0
    elif(x[n - 1] <= m):
        return n
    else:
        return find(0, n - 1)

for i in range(q):
    print(str(shops(int(input()))))
