import random

#======= SORTING =========
#6 main algos used for sorting
    #Bubble Sort
    #Selection Sort
    #Insertion Sort
    #Shell Sort
    #Merge Sort
    #Quick Sort

#Common interview questions consits of being asked to implement a sorting algorthm, but in real life we'll never really have to use one because they are built in

#--------------- BUBBLE SORT -------------

#Bubble Sort 
    #Makes multiple passes through a list
    #Compares adjacent items and exchanges those that are out of order
    #Each pass through the list places the next largest value in its proper place
    #Each item 'bubbles' up to the location where it belongs

    #If we have (n) items, we make (n-1) pairs that need to be compared in the first pass
    #Once the largest value in a list is part of a pair, it will continually be moved along until the pass is complete
    #After first pass, the largest value is now in place, so no we have (n-1) items to check and therefore (n-2) pairs

def bubblesort(arr):
    for n in range( len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                tmp = arr[k+1]
                arr[k+1] = arr[k]
                arr[k] = tmp
    return arr

# arr = [5,3,7,2]

# print(bubblesort(arr))



#--------------- SELECTION SORT ---------------

#Selection Sort
    #Selection sort improves on the bubble sort by making only one exchange for every pass through the list
    #A selection sort looks for the largest value as it makes a pass, and, after completing the pass, places it in the proper location
    #After the first pass, the largest item is in the correct place. After the second pass, the next largest is in place
    #This process continues and requires n-1 passes to sort n items, since the final item must be in place after the (n-1)st pass

def selectionsort_myversion(arr):
    max = random.randint(0,10)
    for n in range (len(arr)-1, 0, -1):

        for i in range(n+1):
            if arr[i] > max:
                max = arr[i]
                index = i
                
        tmp = arr[n]
        arr[n] = max
        max = arr[index] = tmp

    return arr
 
arr = [40,32,6,7,90,12,54]

print(selectionsort_myversion(arr))


#--------------- INSERTION SORT ---------------
    #Insertion sort always maintains a sorted sublist in the lower positions of the list
    #Each new item is then 'inserted' back into the previous sublist such that the sorted sublist is one item larger
    #So you have this little sublist which you assume is already sorted, and you're passing the other elements into that sublist

    #We begin by assuming that a list with one item (position 0) is already sorted
    #On each pass, one for reach item 1 through n-1, the current item is checked against those in the already sorted sublist
    #As we look back into the already sorted sublist, we shift those items that are greater to the right
    #When we reach a smaller item or the end of the sublist, the current item can be inserted

def insertionsort(arr):

    for i in range(1,len(arr)):
        
        currentvalue = arr[i]
        position = i

        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position-1]
            position = position-1

        arr[position] = currentvalue

    return arr

arr = [4,6,2,7,4,1,9,11]

#Shifting is better/faster than exchange
#Shift operation requires approx 1/3 energy when compared to an exchange  

print(insertionsort(arr))


#--------------- SHELL SORT ---------------
    #Shell sort improves on the insertion sort by breaking the original list into a number of smaller sublists
    #Each of those sublists are sorted using an insertion sort
    #Unique way that these sublists are chosen is the key to to the shell sort

    #Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment 'i' to create a sublist by choosing all items that are 'i' items apart

def shell_sort(arr):

    sublistcount = len(arr)//2
    
    while sublistcount > 0:
        
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)

        sublistcount = sublistcount//2 
    
    return arr

def gap_insertion_sort(arr, start, gap):
    
    for i in range(start+gap, len(arr), gap):
        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position-gap] > currentvalue:
            arr[position] = arr[position-gap]
            position = position - gap
        
        arr[position] = currentvalue

arr = [45,1,5,87,6,4,3,2,7,9]
print(shell_sort(arr))



#=========== DIVIDE & CONQUER STRATEGIES ==========

#--------------- MERGE SORT ---------------

    #Merge sort is a recursive algorithm that continually splits a list in half
    #If the list is empty or has one item, it is sorted by definition (the base case)
    #If the list has more than one item, we split the list and recursively invoke a merge sort on both halves
    #Once the two halves are sorted, the fundamental operation, called a merge, is performed
    #Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list

# -- IMPLENTATION OF MERGE SORT

def merge_sort(arr):

    if len(arr) > 1:            #base case check
        mid = len(arr)//2       #calculate midpoint
        
        lefthalf = arr[:mid]    #Split list into two halves
        righthalf = arr[mid:]

        merge_sort(lefthalf)    #Call mergesort on both halves, i.e. split again until base case
        merge_sort(righthalf)

        i=0     #tracker for left half
        j=0     #for right half
        k=0     #for final array


        #These 3 while loops are doing the merging

        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1

            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    return arr

arr = [12,5,80,78,677,43,3,4,1]
print(merge_sort(arr))
                

#--------------- QUICK SORT -----------------
    #The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage
    #As a trade-off, however,it is possible that the list may not be divided in half
    #When this happens, we will see that performance is diminished

    #A quicksort first selects a value, which is called the 'pivot' value
    #The role of the pivot value is to assist with splitting the list
    #The actual position where the pivot value belongs in the final sorted list, (commonly called split point), will be used to divide the list for subsequent calls to the quick sort

def quick_sort(arr):
     
     quick_sort_help(arr, 0, len(arr)-1 )

def quick_sort_help(arr, first, last):

    if first < last:
        splitpoint = partition(arr, first, last)
        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint + 1, last)

def partition(arr, first, last):

    pivotvalue = arr[first]
    leftmark = first+1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

#Use print statements to check what is going on...
#Check out jupyter notebook for more resources

