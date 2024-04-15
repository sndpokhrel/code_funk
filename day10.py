#!/bin/python3

import math
import os
import random
import re
import sys


def consecutive(string, value):
    count = 0
    rep = 0
    
    for char in string:
        if char == value:
            count +=1
            rep = max(rep, count)
        else:
            count = 0
    return rep


if __name__ == '__main__':
    n = int(input().strip())
    binary = format(int(n),'b')
    print(consecutive(binary,'1'))
 
