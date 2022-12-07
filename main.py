def puzirik_sort(nums_1):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums_1) - 1):
            if nums_1[i] > nums_1[i + 1]:
                nums_1[i], nums_1[i + 1] = nums_1[i + 1], nums_1[i]
                swapped = True

random_nums_1 = [5, 2, 1, 8, 4]
puzirik_sort(random_nums_1)
print("-----------------------------------------------------------------")
print("Пузырьковая сортировкa:", random_nums_1)

def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1
    while (swapped == True):
        swapped = False
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if (not (swapped)):
            break
        swapped = False
        end_index = end_index - 1
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start_index = start_index + 1

random_nums_2 = [8, 13, 4, 9, 11]
shaker_sort(random_nums_2)
print("-----------------------------------------------------------------")
print("Шейкерная сортировка:", random_nums_2)

print("-----------------------------------------------------------------")
def sliyanie(nums_3):
    if len(nums_3) > 1:
        mid = len(nums_3) // 2
        left = nums_3[:mid]
        right = nums_3[mid:]
        sliyanie(left)
        sliyanie(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums_3[k] = left[i]
                i+=1
            else:
                nums_3[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            nums_3[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums_3[k] = right[j]
            j+=1
            k+=1

nums_3 = [11, 14, 2, 6, 1, 4, 3]
sliyanie(nums_3)
print("Сортировка слиянием:", nums_3)

print("-----------------------------------------------------------------")
print("Сортировка расчёской:")
massiv = [23, 91, 558, 55, 13]
def rascheska(massiv):
    step = int(len(massiv)/1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(massiv):
            if massiv[i] > massiv[i+step]:
                massiv[i], massiv[i+step] = massiv[i+step], massiv[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)
            print(massiv)
print(massiv)
rascheska(massiv)
print('Результат сортировки:', massiv)


def quicksort(nums_5, start, end):
    if end - start > 1:
        p = partition(nums_5, start, end)
        quicksort(nums_5, start, p)
        quicksort(nums_5, p + 1, end)


def partition(nums_5, start, end):
    pivot = nums_5[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and nums_5[i] <= pivot):
            i = i + 1
        while (i <= j and nums_5[j] >= pivot):
            j = j - 1

        if i <= j:
            nums_5[i], nums_5[j] = nums_5[j], nums_5[i]
        else:
            nums_5[start], nums_5[j] = nums_5[j], nums_5[start]
            return j


nums_5 = [12, 14, 88, 11, 99, 4, 3]
nums_5 = [int(x) for x in nums_5]
quicksort(nums_5, 0, len(nums_5))
print("-----------------------------------------------------------------")
print('Быстрая сортировка:', nums_5)
print("-----------------------------------------------------------------")