# row = 1
# while row < 6:
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#
#     print("")
#     row += 1

#
# row = int(input("Enter the number of first row: "))
#
# n = int(input("Enter the number of total rows in the pattern: "))
#
# while row < n:     # if we put 10 as value of n then, the last pattern contains 9 stars
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#     print("")
#     row += 1


# row = int(input("Enter the number of first row: "))
#
# n = int(input("Enter the number of total rows in the pattern: "))
#
# while row < n + 1:   # this will give the same number of stars in tha last line
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#     print("")
#     row += 1

# row = 1
#
# while row < 6:
#     col = 5
#     while col >= row:
#         print("*", end=" ")
#         col -= 1
#
#     print("")
#     row += 1


# row = 1
# n = int(input("Enter the no. of total rows in the pattern: "))
# column = int(input("Enter the no. of columns of first pattern: "))
# while row < n + 1:
#     col = column
#     while col >= row:
#         print("*", end=" ")
#         col -= 1
#
#     print("")
#     row += 1


# making a pyramid using for loop(right triangle)
# for rows in range(10):
#     print("*" * rows)

# number = int(input("Enter the total number of rows of pattern: "))
#
# for i in range(1, number + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#
#     print("")

# for i in range(6, 1, -1):
#     for j in range(1, i):
#         print("*", end=" ")
#     print()
#
# num = int(input("Enter the number of total rows in pattern: "))
#
# for i in range(num+1, 1, -1):
#     for j in range(1, i):
#         print("*", end=" ")
#
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end="")
#
#     print()

# number = int(input("Enter the number of columns of last row: "))
#
# for i in range(1, number + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#
#     print()


# n = int(input("Enter the range of the pattern: "))
# for i in range(1, n + 1):
#
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# n = int(input("Enter the range of the pattern: "))
# for i in range(1, n + 1):
#
#     for j in range(1, i):
#         print(j, end="")
#     print(i)

# n = int(input("Enter the range of the pattern: "))
# for i in range(1, n + 1):
#
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()


# recursive function example which repeat itself over and over and over
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return  1
#     elif n > 2:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# for n in range(1, 11):
#     print(n, ":", fibonacci(n))

# Memoization ( to delete the cache values )

# from functools import lru_cache
#
# @lru_cache(maxsize= 1000)
#
# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# for n in range(1, 100):
#     print(n, ":", fibonacci(n))


# row = 1
# x = "   "
# row2 = 5
# while row <= 5 and row2 >= 1:
#
#     # print(row2 * x, end="")
#     print("*")
#     print(row2 * x, end="")
#     print("*")
#     print(row*x, end="")
#
#     row += 1
#     row2 -= 1

x = " "
for row in range(5):

    print(row*x, end="")
    print("*")
