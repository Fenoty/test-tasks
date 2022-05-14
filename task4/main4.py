import math 
import numpy as np

import sys
import argparse
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', '--name', type=argparse.FileType())
 
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    text = namespace.name.read()
    result = [int(item) for item in text.split()]


nums = result
result_digit = math.ceil((max(nums))/2)
count = 0
for id, i in enumerate(nums):
    while i != result_digit:
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
            i -= 1
            count += 1
        else:
            nums[id] = i
print('Минимальное кол-во ходов = ',count)

