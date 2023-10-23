# def  function1 (n):
#     x   = []
#     for i in range (n,-1,-1):
#         x.append(i)
#         print(i)
#     return x
# print(function1(5))


# def function2 (arr):
#     print(arr[0])
#     return arr[1]


# def function3(arr):
#     x = arr[0] + len(arr)
#     return x
# print(function3([2, 3, 4, 5, 6]))


# def function4(arr1):
#     arr2 = []
#     for i in range(len(arr1)):
#         if arr1[i] > arr1[1]:
#             arr2.append(arr1[i])
#     print(len(arr2))

#     if len(arr2) < 2:
#         return False
#     return arr2
# print(function4([1, 2, 4, 5, 6, 7, 8]))


def length_value(size, value):
    x = []
    for i in range(size):
        x.append(value)
    return x
result = length_value(10, 69)
print(result)
