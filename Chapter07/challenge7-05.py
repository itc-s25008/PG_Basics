list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

x = []
for i in list1:
    for j in list2:
        x.append(i + j)
print(x)
