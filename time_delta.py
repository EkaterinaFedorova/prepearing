# You are given 2 timestamps in the format given below:
#
# Day dd Mon yyyy hh:mm:ss +xxxx
#
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
#
# Input Format
#
# The first line contains , the number of testcases.
# Each testcase contains  lines, representing time  and time .
#
# Sample Input 0
#
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0
#
# 25200
# 88200

import datetime

user_input1 = "Fri 11 Feb 2078 00:05:21 +0400"
user_input2 = "Mon 29 Dec 2064 03:33:48 -1100"


with open('input', 'r') as f:
    for i in range(int(f.readline().strip())):
        t1 = datetime.datetime.strptime(f.readline().strip(), "%a %d %b %Y %X %z")
        t2 = datetime.datetime.strptime(f.readline().strip(), "%a %d %b %Y %X %z")
        result = t1 - t2
        print(abs(int(result.total_seconds())))
