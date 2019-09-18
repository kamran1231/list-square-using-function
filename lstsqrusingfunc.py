


i = 0
def square_of_list(l):
    list1 = []
    for i in l:
        list1.append(i**2)
    return list1

numbers = list(range(1,11))
print(square_of_list(numbers))