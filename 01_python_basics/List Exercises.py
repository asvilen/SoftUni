# 1. Reverse  a list in Python
# list1 = [100, 200, 300, 400, 500]

# Solution 1
# list1.reverse()
# print(list1)

# Solution 2
# listr = list1[::1]
# print(listr)

# 2. Concatenate 2 lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# Solution 1
# result = [list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]]
# print(result)

# Solution 2
# list3 = [i + j for i,j in zip(list1, list2)]
# print(list3)

# 3. Turn every item of a list into a square
# numbers = [1, 2, 3, 4, 5, 6, 7]

# Solution 1
# sq = [i * i for i in numbers]
# print(sq)

# Solution 2
# sq = []
# for i in numbers:
#    sq.append(i * i)
# print(sq)

# 4. Concatenate two lists in the following order ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# list = [i + j for i in list1 for j in list2]
# print(list)