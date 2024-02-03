import random
import time
import numpy
import sys

################################
#####    SELECTION SORT    #####
################################

def selection_sort(array):
    for i in range(0,len(array)-1):                     
        min = i
        for j in range(i+1,len(array)):                
            if array[j] < array[min]:
                min = j
        array[i] , array[min] = array[min] , array[i]  

################################
#####    INSERTION SORT    #####
################################

def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key

#############################
#####    BUBBLE SORT    #####
#############################

def bubble_sort(array):
    sorted = False
    last = len(array) - 1
    i = 0
    while i < last and (not sorted):
        sorted = True
        j = last
        while j > i:
            if array[j-1] > array[j]:
                array[j-1] , array[j] = array[j] , array[j-1]
                sorted = False
            j = j - 1
        i = i + 1

#############################
#####   BINARY SEARCH   #####
#############################

def binary_search(array, first, last, k):
    if last >= first:
        mid = (first + last) // 2
        if arrya[mid] == k:
            return mid
        elif array[mid] > k:
            return binary_search(array, first, mid - 1, k)
        else:
            return binary_search(array, mid + 1, last, k)
    else:
        return -1

############################
#####    MERGE SORT    #####
############################

def merge_sort(array):
    sort_for_merge(array,0,len(array)-1)

def sort_for_merge(array,first,last):
    if first < last:
        sort_for_merge(array,first,(first + last) // 2)
        sort_for_merge(array,(first + last) // 2 + 1,last)
        merge(array,first,(first + last) // 2,last)

def merge(array,first,middle,last):
    temp = [0 for i in range(0,len(array))]
    first1 = first
    last1 = middle
    first2 = middle + 1
    last2 = last
    key = first1
    while first1 <= last1 and first2 <= last2:
        if array[first1] < array[first2]:
            temp[key] = array[first1]
            first1 = first1 + 1
        else : 
            temp[key] = array[first2] 
            first2 = first2 + 1
        key = key + 1
    while first1 <= last1:
        temp[key] = array[first1]
        first1 = first1 + 1
        key = key + 1
    while first2 <= last2:
        temp[key] = array[first2]
        first2 = first2 + 1
        key = key + 1
    for i in range(first,last+1):
        array[i] = temp[i]

############################
#####    QUICK SORT    #####
############################

def quick_sort(array):
    sort_for_quick(array,0,len(array)-1)

def sort_for_quick(array,first,last):
    if first < last:
        pivot_index = random_partition(array,first,last)
        sort_for_quick(array,first,pivot_index - 1)
        sort_for_quick(array,pivot_index + 1,last)

def random_partition(array,first,last):
    pivot_index = random.choice(range(first,last+1))
    array[pivot_index] , array[last] = array[last] , array[pivot_index]
    return partition(array,first,last)

def partition(array,first,last):
    pivot_index = last
    pivot = array[pivot_index]
    while first < last:
        while first < last and array[first] < pivot:
            first = first + 1
        while array[last] >= pivot and last > first:
            last = last - 1
        if first < last:
            array[first] , array[last] = array[last] , array[first]
    array[last] , array[pivot_index] = array[pivot_index] , array[last]
    return last

#########################
#####    MIN HEAP   #####
#########################

def min_heap(array):
    size = len(array)
    for i in range(size // 2 - 1, -1, -1):
        min_heapify(array,size,i)

def min_heapify(array,size,index):
    smallest = index
    left = 2 * smallest + 1
    right = 2 * smallest + 2
    if left < size and array[smallest] > array[left]:
        smallest = left
    if right < size and array[smallest] > array[right]:
        smallest = right
    if smallest != index:
        array[index] , array[smallest] = array[smallest] , array[index]
        min_heapify(array,size,smallest)

#########################
#####    MAX HEAP   #####
#########################

def max_heap(array):
    size = len(array)
    for i in range(size // 2 - 1, -1, -1):
        max_heapify(array,size,i)

def max_heapify(array,size,index):
    largest = index
    left = 2 * largest + 1
    right = 2 * largest + 2
    if left < size and array[largest] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != index:
        array[index] , array[largest] = array[largest] , array[index]
        max_heapify(array,size,largest)

###########################
#####    HEAP SORT    #####
###########################

def heap_sort(array):
    size = len(array)
    option = int(input("\n1. Using min heap[Descending]\n2. Using max heap[Ascending]\n"))
    if option == 1:
        min_heap(array)
        for i in range(size - 1, -1 , -1):
            array[i] , array[0] = array[0] , array[i]
            min_heapify(array,i,0)
    elif option == 2:
        max_heap(array)
        for i in range(size - 1, 0, -1):
            array[i] , array[0] = array[0] , array[i]
            max_heapify(array,i,0)
    else :
        print("\nWrong Input")
        heap_sort(array)

##########################
#####    PART ONE    #####
##########################

def run_time_calculator():
    size = int(input("\nEnter size of the array: "))
    sample = random_array_generator(size)
    copied_samples = [0 for i in range(0,5)]

    for i in range(0,5):
        copied_samples[i] = sample.copy()

    selection_start = time.time()
    selection_sort(copied_samples[0])
    selection_finish = time.time()
    selection_time = (selection_finish - selection_start) * 1000000
    print("-Selection Sorting Algorithm:\t\t"      +str(selection_time)   + "\t\tmicroseconds")

    insertion_start = time.time()
    insertion_sort(copied_samples[1])
    insertion_finish = time.time()
    insertion_time = (insertion_finish - insertion_start) * 1000000
    print("-Insertion Sorting Algorithm:\t\t"      +str(insertion_time)   + "\t\tmicroseconds")

    bubble_start = time.time()
    bubble_sort(copied_samples[2])
    bubble_finish = time.time()
    bubble_time = (bubble_finish - bubble_start) * 1000000
    print("-Bubble Sorting Algorithm:\t\t"         +str(bubble_time)      + "\t\tmicroseconds")

    merge_start = time.time()
    merge_sort(copied_samples[3])
    merge_finish = time.time()
    merge_time = (merge_finish - merge_start) * 1000000
    print("-Merge Sorting Algorithm:\t\t"          +str(merge_time)       + "\t\tmicroseconds")

    quick_start = time.time()
    quick_sort(copied_samples[4])
    quick_finish = time.time()
    quick_time = (quick_finish - quick_start) * 1000000
    print("-Quick Sorting Algorithm:\t\t"          +str(quick_time)       + "\t\tmicroseconds")

######################################################
#####    HYBRID MERGE AND SELECTION ALGORITHM    #####
######################################################

def hybrid_sort(array):
    threshold = int(input("\nEnter threshold value of hybrid merge and selection algorithm: "))
    sort_for_hybrid(array,0,len(array)-1,threshold)

def sort_for_hybrid(array,first,last,threshold):
    if len(array) <= threshold and first < last:
        selection_sort(array)
    elif first < last:
        sort_for_hybrid(array,first,(first + last) // 2,threshold)
        sort_for_hybrid(array,(first + last) // 2 + 1,last,threshold)
        merge(array,first,(first + last) // 2,last)

###################################################################
#####    FUNCTION TO FIND KTH ELEMENT IN AN UNSORTED ARRAY    #####
###################################################################

def element(array):
    k = int(input("\nEnter the order of k: "))
    return find_element(array,0,len(array)-1,k)

def find_element(array,first,last,k):
    if k <= len(array):
        pivot_index = random_partition(array,first,last)
        if pivot_index == k - 1:
            return array[pivot_index]
        elif pivot_index > k - 1:
            return find_element(array,first,pivot_index - 1,k)
        elif pivot_index < k - 1:
            return find_element(array,pivot_index + 1,last,k)
    else :
        return "Not Found!\nKth element must be smaller than the length of the array!"

#########################
#####    PROGRAM    #####
#########################

def menu():
    option = int(input("\n\n#####    MENU    #####\n\n1. Selection Sort\n2. Insertion Sort\n3. Bubble Sort\n4. Merge Sort\n5. Quick Sort\n6. Hybrid Sort\n7. Find Kth Element\n8. Test running time of the first five sorting algorithms\n9. Build minimum heap\n10. Build maximum heap\n11. Heap Sort\nOtherwise- Exit\n"))
    return option

def array_generator():
    option = int(input("\n1. Random array\n2. Enter an array\n"))
    if option == 1:
        size = int(input("\nEnter size of the array: "))
        return random_array_generator(size)
    elif option == 2:
        array = []
        size = int(input("\nEnter size of the array: "))
        print("Enter the elements: ")
        for i in range(0,size):
            element = int(input())
            array.append(element)
        return array
    else : 
        print("Error: Enter either 1 or 2")
        return array_generator()
    
def random_array_generator(size):
    return numpy.random.randint(0,99,size)

sys.setrecursionlimit(10000)
run = True    
print("\nStarting Program...\n")
while(run):
    menu_option = menu()
    if menu_option == 1:
        array = array_generator()
        if len(array) <= 50:
            print("Before Sorting: " + str(array))
        selection_sort(array)
        if len(array) <= 50:
            print("After Sorting: " + str(array))
        continue
    elif menu_option == 2:
        array = array_generator()
        if len(array) <= 50:
            print("Before Sorting: " + str(array))
        insertion_sort(array)
        if len(array) <= 50:
            print("After Sorting: " + str(array))
        continue
    elif menu_option == 3:
        array = array_generator()
        if len(array) <= 50:
            print("Before Sorting: " + str(array))
        bubble_sort(array)
        if len(array) <= 50:
            print("After Sorting: " + str(array))
        continue
    elif menu_option == 4:
        array = array_generator()
        if len(array) <= 50:
            print("Before Sorting: " + str(array))
        merge_sort(array)
        if len(array) <= 50:
            print("After Sorting: " + str(array))
        continue
    elif menu_option == 5:
        array = array_generator()
        if len(array) <= 50:
            print("Before Sorting: " + str(array))
        quick_sort(array)
        if len(array) <= 50:
            print("After Sorting: " + str(array))
        continue
    elif menu_option == 6:
        array = array_generator()
        if len(array) <= 50:
            print("Before Sorting: " + str(array))
        hybrid_sort(array)
        if len(array) <= 50:
            print("After Sorting: " + str(array))
        continue
    elif menu_option == 7:
        array = array_generator()
        if len(array) <= 50:
            print("\n" + str(array))
        num = element(array)
        print("The element is: " + str(num))
        continue
    elif menu_option == 8:
        run_time_calculator()
        continue
    elif menu_option == 9:
        array = array_generator()
        if len(array) <= 50:
            print("Original Array: " + str(array))
        min_heap(array)
        if len(array) <= 50:
            print("Minimum Heap: " + str(array))
        continue
    elif menu_option == 10:
        array = array_generator()
        if len(array) <= 50:
            print("Original Array: " + str(array))
        max_heap(array)
        if len(array) <= 50:
            print("Maximum Heap: " + str(array))
        continue
    elif menu_option == 11:
        array = array_generator()
        if len(array) <= 50:
            print("Before Sorting: " + str(array))
        heap_sort(array)
        if len(array) <= 50:
            print("After Sorting: " + str(array))
        continue
    else :
        print("\nExiting Program...")
        run = False
        break