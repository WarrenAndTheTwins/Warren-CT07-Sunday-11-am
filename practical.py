
#################################################################
# Question 1
# A e-commerce store keeps track of their sales figures each day 
# for the month of August. 
# The sales for the 31 days are provided in the list below. 

# Write Code to:
# a) Find the day with the highest sales 
# b) Find the day with the lowest sales
# c) Find the average daily sales for August (to 2 decimal place)
    

# Example Output/ Answer:
# 5 August has highest sales of $15741
# 7 August has lowest sales of $800
# Average daily sales for August is $6714.71


# Assume that first item in list is 1 August (not zero!)
# You are allowed to use the inbuilt functions e.g. max()
##########################################################
daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
               13056, 952, 1100, 1025, 8574, 14014, 9987, 
               1238, 1458, 7803, 900, 13674, 14539, 13241, 
               10886, 7541, 8743, 1482, 11523, 977, 12181, 
               8903, 1008, 1530]
# Write your code here.

sum = 0
average = 0
maximum_sale = max(daily_sales)
maximum_day = daily_sales.index(maximum_sale) + 1
print("August " + str(maximum_day) + " had the highest sales of :" + str(maximum_sale))
minimum_sale = min(daily_sales)
minimum_day = daily_sales.index(minimum_sale) + 1
print("August " + str(minimum_day) + " had the lowest sales of :" + str(minimum_sale))
for day_sale in daily_sales:
    sum += day_sale 
    average = round(sum / len(daily_sales), 2)
print("The average sale per day in August was " + str(average))

# You are given a list of 100 random numbers. 
# Your task is to check if each number is odd or even.

# To check if the number is odd or even 
# Write a function to determine if a number is even.
# if number is even, return True, else return False.

# Example Output:
# 2944 is even.
# 5490 is even.
# 2357 is odd.
# 2619 is odd.


##### Task 1: COMPLETE THIS FUNCTION TO CHECK ODD/ EVEN
def is_even(num):

    pass # remove this when you code. Ask Code Mentor if unsure.
    # Write your code to check if the number is even
    
    # return True or False

# Example output:
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

###### Task 2: COMPLETE THE FOR LOOP TO CALL is_even() here.
for i in list1:
    pass # remove this when you code. Ask Code Mentor if unsure.

    # call the function to check if the number is odd or even

