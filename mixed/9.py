# 9.	Find the average of numbers in a list using a for loop.
# def find_average(lst):
#     if not lst:
#         return None  # Return None if the list is empty
#     total = 0
#     for num in lst:
#         total += num

#     average = total / len(lst)
#     return average

# # Example usage:
# numbers = [10, 20, 30, 40, 50]
# average_number = find_average(numbers)
# print("The average of the numbers in the list is:", average_number)

n = [10, 20, 30, 40, 50]
t=0
for i in n:
    t+=i
print(t)
print(t/len(n))