#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    notifications = 0
    count = [0] * 201  
    def find_median(d):
        count_sum = 0
        median_1, median_2 = None, None
        for i in range(len(count)):
            count_sum += count[i]
            if median_1 is None and count_sum >= d // 2:
                median_1 = i
            if median_2 is None and count_sum >= d // 2 + 1:
                median_2 = i
                break
        return median_2 if d % 2 == 1 else (median_1 + median_2) / 2
    for i in range(d):
        count[expenditure[i]] += 1
    for i in range(d, len(expenditure)):
        median = find_median(d)

        if expenditure[i] >= 2 * median:
            notifications += 1
        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1

    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
