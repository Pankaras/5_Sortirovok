def puzirik_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                
print("Пузырьковая сортировкa:")
random_nums = [5, 2, 1, 8, 4]
puzirik_sort(random_nums)
print(random_nums)

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

print("Шейкерная сортировка:")
random_nums_2 = [8, 13, 4, 9, 11]
shaker_sort(random_nums_2)
print(random_nums_2)

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
print("Сортировка слиянием:")
print(nums_3)