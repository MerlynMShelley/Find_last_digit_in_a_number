numbers = [2,3,4,4,5,6,7,7,8,9,2,3,4]
uniques = []
for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)