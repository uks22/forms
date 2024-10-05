def findMedianSortedArrays(A, B):
    # Ensure A is the smaller array
    if len(A) > len(B):
        A, B = B, A

    m, n = len(A), len(B)
    low, high = 0, m

    while low <= high:
        i = (low + high) // 2  # Partition A
        j = (m + n + 1) // 2 - i  # Partition B

        # Find the elements on the left and right of the partitions
        max_left_A = float('-inf') if i == 0 else A[i - 1]
        min_right_A = float('inf') if i == m else A[i]

        max_left_B = float('-inf') if j == 0 else B[j - 1]
        min_right_B = float('inf') if j == n else B[j]

        # Check if we have found a valid partition
        if max_left_A <= min_right_B and max_left_B <= min_right_A:
            # If the combined length is odd, return the max of left side
            if (m + n) % 2 == 1:
                return max(max_left_A, max_left_B)
            # If even, return the average of the two middle elements
            else:
                return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2
        elif max_left_A > min_right_B:
            # We are too far right in A, move left
            high = i - 1
        else:
            # We are too far left in A, move right
            low = i + 1

    raise ValueError("Input arrays are not sorted or invalid input.")

# Example Usage
if __name__ == "__main__":
    # Test 1
    A1 = [3,5,7,8,10]
    B1 = [1,4,5,6,12]
    print(f"Median of A1 and B1: {findMedianSortedArrays(A1, B1)}")  # Output: 2.0

    # Test 2
    A2 = [1, 2]
    B2 = [3, 4]
    print(f"Median of A2 and B2: {findMedianSortedArrays(A2, B2)}")  # Output: 2.5

    # Test 3
    A3 = [0, 0]
    B3 = [0, 0]
    print(f"Median of A3 and B3: {findMedianSortedArrays(A3, B3)}")  # Output: 0.0

    # Test 4 (One array empty)
    A4 = []
    B4 = [1]
    print(f"Median of A4 and B4: {findMedianSortedArrays(A4, B4)}")  # Output: 1.0
