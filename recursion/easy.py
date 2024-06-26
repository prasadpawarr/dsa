"""
Check if array is sorted or not
arr = [1, 2, 3, 5, 9]
ans = True
"""
# def f(arr):
#     if len(arr) == 1:
#         return True

#     if arr[0] > arr[1]: return False

#     return f(arr[1:])

# arr = [1, 2, 2, 3, 3]
# print(f(arr))


"""
Implement linear search with recursion.
arr = [1, 2, 3, 4]
target = 3, ans = 2
"""
# def f(arr, idx, target):
#     if idx == len(arr):
#         return -1

#     if arr[idx] == target:
#         return idx

#     return f(arr, idx + 1, target)

# arr = [1, 2, 3, 4]
# target = 0
# print(f(arr, 0, target))

"""
Recursive function to print sum of all digits
"""
# num = 1234
# result = 10

# def sum(num):
#     if num == 0: return 0
#     return num % 10 + sum(num//10)

"""
Binary Search with Recursion
"""
# def f(arr, target, start, end):
#     if start > end:
#         return -1
    
#     mid = start + (end - start) // 2
#     if target == arr[mid]:
#         return mid

#     elif target > arr[mid]:
#         return f(arr, target, mid + 1, end)
#     else:
#         return f(arr, target, start, mid - 1)


# arr = []
# target = 2
# p = f(arr, target, 0, len(arr) - 1)
# print(p)

"""
Check if palindrome or not.
"""
# def palindrome(s: str, i: int):
#     n = len(s)
#     if i >= n/2: return True
#     if s[i] != s[n - i - 1]: return False
#     return palindrome(s, i + 1)

# s =  "madwam"
# print(palindrome(s, 0))

"""
Return all indices of element in array.
arr = [1, 2, 3, 3, 4]
ans = [2, 3]
"""

# def f(arr, idx, target, ans=[]):

#     if idx == len(arr): return ans
#     if arr[idx] == target: 
#         ans.append(idx)

#     return f(arr, idx + 1, target, ans)

# arr = [1, 2, 3, 3, 4]
# target = -1
# print(f(arr, 0, target, []))

"""
Same as above but don't take list as arg
"""

# def f(arr, target, idx):
#     ans = []
#     if idx == len(arr): 
#         return []

#     if arr[idx] == target:
#         ans.append(idx)

#     return ans +  f(arr, target, idx + 1)


# arr = [1, 2, 3, 3, 4]
# target = 3
# print(f(arr, target, 0))

"""
Binary Search in rotated sorted array
arr = [5, 6, 7, 1, 2, 3]
target = 6
"""

# def f(arr, target):
#     start = 0
#     end = len(arr) - 1
#     while start <= end:
#         mid = start + (end - start) // 2
#         if arr[mid] == target:
#             return mid

#         if arr[start] <= arr[mid]:
#             # sorted
#             if arr[start] <= target < arr[mid]: end = mid - 1
#             else: start = mid + 1
#         else:
#             if arr[mid] < target <= arr[end]:
#                 start = mid + 1
#             else:
#                 end = mid -1
#     return -1

# arr = [5, 6, 7, 1, 2, 3]
# target = 6
# print(f(arr, target))


# def f(arr, target, start, end):
#     if start > end: return -1

#     mid = start + (end - start) // 2
#     if arr[mid] == target: return mid

#     if arr[start] < arr[mid]:
#         if arr[start] < target <= arr[mid]:
#             return f(arr, target, start, mid - 1)
#         else:
#             return f(arr, target, mid + 1, end)
#     else:
#         if arr[mid] < target <= arr[end]:
#             return f(arr, target, mid + 1, end)
#         else:
#             return f(arr, target, start, mid - 1)

# arr = [5, 6, 7, 8, 1, 2]
# target = -1
# print(f(arr, target, 0, len(arr) - 1))

""""
Bubble sort
"""


# def bubble(arr, N, idx):
#     if N == 0: return

#     if idx < N:
#         if arr[idx] > arr[idx + 1]:
#             arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
#         bubble(arr, N, idx + 1)
#     else:
#         bubble(arr, N - 1, 0)

# arr = [3, 2, 1, 9]
# bubble(arr, 2, 0)
# print(arr)


"""
Selection sort
"""

# def f(arr, N):
#     idx = 0
#     while N:
#         maxE = float('-inf')
#         for i in range(N):
#             if arr[i] > maxE:
#                 maxE = arr[i]
#                 idx = i
#         arr[idx], arr[N-1] = arr[N-1], arr[idx]
#         N -= 1

# arr = [3, 1, 5, 4, 2, 0]
# f(arr, 6)
# print(arr)

# def f(arr, N, idx, max):
#     if N == 0: return

#     if idx < N:
#         if arr[idx] > arr[max]:
#             f(arr, N, idx + 1, idx)
#         else:
#             f(arr, N, idx + 1, max)
#     else:
#         arr[N-1], arr[max] = arr[max], arr[N-1]
#         f(arr, N - 1, 0, 0)


# arr = [3, 1, 5, 4, 2, 0]
# f(arr, 6, 0, -1)
# print(arr)


"""
Merge Sort
"""

# def mergesort(arr):
#     if len(arr) == 1: return arr

#     mid = len(arr) // 2

#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])

#     return merge(left, right)

# def merge(first, second):
#     ans = []
#     N = len(first)
#     M = len(second)
#     i = j = 0

#     while i < N and j < M:
#         if first[i] < second[j]:
#             ans.append(first[i])
#             i += 1
#         else:
#             ans.append(second[j])
#             j += 1
    
#     if i == N:
#         while j < M:
#             ans.append(second[j])
#             j += 1
#     if j == M:
#         while i < N:
#             ans.append(first[i]) 
#             i += 1
#     return ans


# print(merge([1, 4, 5], [0, 2, 6]))
# print(mergesort([4, 2, 3, 6, 5, 1, 9, 2, 4]))

