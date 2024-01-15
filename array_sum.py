def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:]) # list[1:] replicates the array without the first index

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max # calls the function again, like a loop

print(sum([1,2,3,4]))
print(count([1,2,3,4]))
print(max([1,2,3,4]))
