with open("file1.txt") as first_file:
    list1 = first_file.readlines()
with open("file2.txt") as second_file:
    list2 = second_file.readlines()
list1_int = [int(num.strip()) for num in list1]
list2_int = [int(num.strip()) for num in list2]
result = [num for num in list1_int if num in list2_int]
print(result)
