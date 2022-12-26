#!/usr/bin/python3
import sys
if len(sys.argv) != 2:
    print("Usage: factors <file>")
    exit()
try:
    f = open(sys.argv[1], "r")
except:
    f.close()
my_list = []
for line in f:
    my_list.append(int(line))
for num in my_list:
    n = 2
    while n ** 2 <= num:
        if num % n == 0:
            p = int(num / n)
            q = n
            print("{}={}*{}".format(num, p, q))
            break
        else:
            n += 1
f.close()
