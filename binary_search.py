def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if(guess == item):
            return item
        if(guess > item):
            high = mid - 1
    return None

# def show_list(list):
#     print(list)
# show_list(my_list)

my_list = [1,2,3,4,5]
print(binary_search(my_list, 3))