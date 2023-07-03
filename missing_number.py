def missing_number(array: list):
    for i in range(len(array)+1):
        for j in array:
            if i in array:
                break
            else:
                return i
 


# print(missing_number([0, 1, 3, 4, 5]))
# print(missing_number([6, 1, 3, 4, 5, 0, 2]))
print(missing_number([9, 8, 7, 6, 5, 4, 3, 2, 1]))