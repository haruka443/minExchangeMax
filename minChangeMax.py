lst = [1, 5, -1, -2, 10, 15, 22]
minIndex = None
maxIndex = None
for index, value in enumerate(lst):
    if minIndex is None or value < lst[minIndex]:
        minIndex = index
    if maxIndex is None or value > lst[maxIndex]:
        maxIndex = index
print(f'The minimum number is {lst[minIndex]}')
print(f'The maximum is {lst[maxIndex]}')
if minIndex is not None and maxIndex is not None:
    lst[minIndex], lst[maxIndex] = lst[maxIndex], lst[minIndex]
    print('After the exchage the list presents itself in this way:', lst)
