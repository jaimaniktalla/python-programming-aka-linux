# import sys
# str1 = "Hello, World!"
# str2 = str1.replace("Hello", "Hi")
# print(str1)
# print(type(str1))
# print(id(str1))
# print(str2)
# print(type(str2))
# print(id(str2))
# print(str1, len(str1))
# print(bool(0.5))
# name = input("Enter your name: ")
# print(name)
# x = 42
# size = sys.getsizeof(x)
# print(f"Size of x: {size} bytes.")

# a = 1
# b = 1
# print(id(a))
# print(id(b))

# Write a program that takes user input in numeric form and prints its table

# inp = int(input("Enter your number: "))
# for i in range(1, 11):
#     print(inp, "x", i, "=", inp * i)

# a user has a 3x3 matrix. Store this matrix in a variable, copy this matrix in another variable, and then in the copied matrix multiply each value by a constant and store the result in place. After this, print both the matrices.

# # define empty matrix
# matrix = []

# # print input line
# print("Enter the elements of the 3x3 matrix row-wise:")

# # for loop for input for each row
# for i in range(3):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# # copy the matrix into a new variable
# calculated_matrix = [row[:] for row in matrix]

# # define a constant
# constant = 2

# # run for loop to multiply each data value with the constant
# for i in range(3):
#     for j in range(3):
#         calculated_matrix[i][j] *= constant

# # print original matrix
# print("\nOriginal Matrix:")
# for row in matrix:
#     print(row)

# # print calculated matrix
# print("\nCalculated Matrix after multiplication:")
# for row in calculated_matrix:
#     print(row)

# def add(a, b, c):
#     return a + b + c

# result = add(5, 3, 4)
# print(result)

# Write a program to add 3 numbers and return its value

# list1 = []
# print("Enter your values: ")
# for i in range(5):
#     inp = int(input())
#     list1.append(inp)
# print(list1)
# sum1 = 0
# for i in list1:
#     sum1 += i
# print(sum1)


# write a function that takes one input argument and return its sum cumulative sum, average , min max using for loop. define function documentation using doc string and show its uses

# def compute_stats(numbers):
#     cumulative_sum = []
#     total_sum = 0
#     min_value = numbers[0]
#     max_value = numbers[0]
#     for number in enumerate(numbers):
#         total_sum += number
#         cumulative_sum.append(total_sum)
#         if number < min_value:
#             min_value = number
#         if number > max_value:
#             max_value = number
#     average = total_sum / len(numbers)
#     return {
#         'cumulative_sum': cumulative_sum,
#         'average': average,
#         'min': min_value,
#         'max': max_value
#     }

# # Example usage:
# numbers = [10, 20, 30, 40]
# stats = compute_stats(numbers)
# print(stats)


# def compute_stats(numbers):
#     cumulative_sum = []
#     total_sum = min_value = max_value = numbers[0]
#     for i in numbers:
#         total_sum += i
#         cumulative_sum.append(total_sum)
#         min_value = min(min_value, i)
#         max_value = max(max_value, i)
#     return {
#         'cumulative_sum': cumulative_sum,
#         'total_sum': total_sum,
#         'average': total_sum / len(numbers),
#         'min': min_value,
#         'max': max_value
#     }
# numbers = [10, 20, 30, 40]
# stats = compute_stats(numbers)
# print(stats)


list1 = []
inp = int(input("Enter the number inputs to be given: "))
for i in range(inp):
    inp2 = input("Enter you input: ")
    list1.append(inp2)
print(list1)