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