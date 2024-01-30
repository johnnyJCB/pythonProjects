"""Exercise: Paint Job Calculator
you are tasked with creating a Python program that calculates the number of paint buckets needed for a given area. goal is to 
complete the three functions (get_bucket_count, get_bucket_count_with_dimensions, and get_bucket_count_with_area) by implementing 
the logic for calculating paint buckets.
Write a Python program to calculate the number of paint buckets needed for a given area."""

import math
# Function to calculate the number of paint buckets needed with width, height, area per bucket, and extra buckets
def get_bucket_count(width, height, area_per_bucket, extra_buckets):
    # Your code goes here
    if(width <= 0 or height <= 0 or area_per_bucket <= 0 or extra_buckets < 0):
        return - 1
    else:
        area = width * height
        bucketsNeeded = area/area_per_bucket
        bucketsNeeded -= extra_buckets
    return math.ceil(bucketsNeeded)
    # pass


# Function to calculate the number of paint buckets needed with width, height, and area per bucket
def get_bucket_count_with_dimensions(width, height, area_per_bucket):
    # Your code goes here
    if(width <= 0 or height <= 0 or area_per_bucket <= 0):
        return -1
    else:
        area = width * height
        bucketsNeeded = area/area_per_bucket
    return math.ceil(bucketsNeeded)
    # pass

# Function to calculate the number of paint buckets needed with total area and area per bucket
def get_bucket_count_with_area(area, area_per_bucket):
    # Your code goes here
    if(area <= 0 or area_per_bucket <= 0):
        return -1
    else:
        bucketsNeeded = area/area_per_bucket
        return bucketsNeeded
    # pass

# Testing the functions with print statements
result1 = get_bucket_count(20, 5, 2, 8)     # should print 20*5 = 100, 100/2 = 50, 50-8 = 42 as Integer
print("Result 1:", result1)

result2 = get_bucket_count_with_dimensions(10, 5, 2)        # should print 5*10 = 50, 50/2 = 25 as Integer
print("Result 2:", result2)

result3 = get_bucket_count_with_area(80, 2)     # should print 80/2 = 40.0 as float because did not round it to integer
print("Result 3:", result3)

result4 = get_bucket_count(0, 5, 2, 1)
print("Result 4:", result4)     # should print 0 as 1st argument (width) is 0
