# =========================================
# =========================================
# BASIC SORTING AND SEARCHING TASKS
# =========================================

# Task 1: Linear Search
# Implement a function that performs a linear search to find a target element in a list of integers.
# Return the index of the element if found, or -1 if not found.
# ---
def linear_search(arr, target): # Traverse each element of the list
 for i in range(len(arr)):
  if arr[i] == target: 
   return i # Return the index of the target element if found return -1 # Return -1 if the target element is not found # Example usage 
arr = [10, 25, 30, 45, 50] 
target = 30 
result = linear_search(arr, target) 
if result != -1: print(f"Element found at index {result}") 
else: 
 print("Element not found")


# Task 2: Binary Search
# Implement a function that performs a binary search to find a target element in a sorted list of integers.
# Return the index of the element if found, or -1 if not found.
# ---

def binary_search(arr,target):
    low,high =0,len(arr)-1
    while low<=high:
        mid +(low + high )//2
        if arr[mid]== target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        
    else:
        high = mid - 1
        return-1
    


# Task 3: Bubble Sort
# Write a function that sorts a list of integers using the bubble sort algorithm.
# Print the sorted list.
# ---
def bubble_sort(arr):
    n = len(arr)
for i in range(n):
    for j in range (0,n-i-1):
        if arr[j].arr [j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]   
        
return arr() 

# Task 4: Selection Sort
# Write a function that sorts a list of integers using the selection sort algorithm.
# Print the sorted list.
# ---

def selection_sort(nums):
    for i in range(len(nums)):
        # Find the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        nums[i], nums[min_index] = nums[min_index], nums[i]

# Main function to test the selection sort
def main():
    numbers = [64, 25, 12, 22, 11, 90]
    print("Unsorted list:", numbers)
    selection_sort(numbers)
    print("Sorted list:", numbers)

if __name__ == "__main__":
    main()


# Task 5: Insertion Sort
# Write a function that sorts a list of integers using the insertion sort algorithm.
# Print the sorted list.
# ---

def insertion_sort (arr):
    for i in range (1,len(arr)):
        key = arr [i]
        j = i -1 
        while j >= 0 and key <arr [j]:
            arr [j+1]= arr [j]
            j -=1
            arr [j+1]=key
        return arr
# Task 6: Merge Sort
# Write a function that sorts a list of integers using the merge sort algorithm.
# Print the sorted list.
# ---

def merge_sort(arr):
    if len(arr)>1:
        mid =len (arr)//2
        left_half = arr [:mid]
        right_half = arr[mid:]
        
        merge_sort (left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i <len(left_half) and j <len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]= left_half[i ]
                i +=1
            else:
             arr[k]= right_half[j]
            j +=1
            k+=1
         
        while i <len(left_half):
             arr[k]= left_half[i]
        i +=1
        k+=1
        while j <len(right_half):
            arr [k]= right_half[j]
            j+=1
            k+=1
        return arr

# Task 7: Quick Sort
# Write a function that sorts a list of integers using the quick sort algorithm.
# Print the sorted list.
# ---



# Task 8: Find Maximum Value
# Write a function to find and return the maximum value in a list of integers.
# ---


# Task 9: Find Minimum Value
# Write a function to find and return the minimum value in a list of integers.
# ---


# Task 10: Count Occurrences
# Implement a function that counts the occurrences of a specific element in a list of integers.
# ---



# =========================================
# =========================================
# ADVANCED SORTING AND SEARCHING TASKS
# =========================================

# Task 11: Binary Search on Strings
# Implement a binary search to find a target string in a sorted list of strings.
# Return the index of the string if found, or -1 if not found.
# ---

# Task 12: Merge Sort on Strings
# Write a function that sorts a list of strings using the merge sort algorithm.
# Print the sorted list.
# ---

# Task 13: Quick Sort on Custom Objects
# Create a class representing custom objects (e.g., Student with name and age).
# Implement the quick sort algorithm to sort a list of these objects based on a specific attribute (e.g., age or name).
# ---

# Task 14: Reverse List
# Write a function to reverse a list of integers in-place (without using Python's built-in reverse function).
# ---

# Task 15: Unique Elements
# Implement a function that returns a list containing unique elements from a given list of integers.
# ---

# Task 16: Search in Sorted Matrix
# Implement a function to search for a target element in a sorted matrix (matrix is sorted row-wise and column-wise).
# Return True if found, False otherwise.
# ---

# Task 17: Bubble Sort on Strings
# Write a function that sorts a list of strings using the bubble sort algorithm.
# Print the sorted list.
# ---

# Task 18: Selection Sort on Strings
# Write a function that sorts a list of strings using the selection sort algorithm.
# Print the sorted list.
# ---

# Task 19: Insertion Sort on Strings
# Write a function that sorts a list of strings using the insertion sort algorithm.
# Print the sorted list.
# ---

# Task 20: Custom Sorting Algorithm
# Design and implement your own custom sorting algorithm and use it to sort a list of integers.
# Compare its performance to other sorting algorithms.
# ---





