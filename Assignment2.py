import winsound
import time

#method to merge two sorted arrays
def merge(array, left, mid, right):
    #temporary array
    temp = []
    i = left
    j = mid + 1

    #Merge the two sorted subarrays
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    #put the remaining elements from the left subarray
    while i <= mid:
        temp.append(array[i])
        i += 1

    #put the remaining elements from the right subarray
    while j <= right:
        temp.append(array[j])
        j += 1

    #put elements from temp back to original array
    for idx, val in enumerate(temp):
        array[left + idx] = val

#Method to perform merge sort algorithm
def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2

        #sort the two halves using recursion
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)

        #print("Iteration:", array[left:right + 1])

        #Merge the sorted halves
        merge(array, left, mid, right)

        #output current iteration of Merge sort. (Show steps)
        print("Merge Sort Step:", array[left:right + 1])
       
       #use winsound to make beep sfx when sorting
        winsound.Beep(1000, 100)

#main method
def main():

    #Prompt for User Input
    array_str = input("Enter array elements and separate them by using spaces: ")
    #split the array input by the spaces
    array = list(map(int, array_str.split()))

    #print the original array that was inputted
    print("Original array:", array)

    #sort the merge sort array
    merge_sort(array, 0, len(array) - 1)

    #print the array that was sorted through merge sort
    print("Sorted array:", array)

# Run through main method
if __name__ == "__main__":
    #call main method
    main()