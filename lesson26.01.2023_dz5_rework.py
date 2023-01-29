#Универсальное решение для четных, нечетных элементов и для пустого списка
lst = [2, 4, 6, 8,9,12]
#lst = [3, 9, 10, 4, 7]
#lst = [1]
#lst = []

size = len(lst)
if size % 2 == 0:
    middle = int(size/2)
else:
    middle = int(size/2) + 1
new_lst = lst[:middle], lst[middle:]
print(new_lst)

