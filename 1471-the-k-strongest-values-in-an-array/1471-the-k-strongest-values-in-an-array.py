class Solution (object):
    def getStrongest(self, arr, k):
        # Step 1: Sort the array
        arr.sort()

        # Step 2: Find the median
        n = len(arr)
        median = arr[(n - 1) // 2]

        # Step 3: Use two pointers to find the k strongest values
        left = 0
        right = n - 1
        result = []

        while len(result) < k:
            # Compare the strength of arr[left] and arr[right]
            if abs(arr[left] - median) > abs(arr[right] - median):
                result.append(arr[left])
                left += 1
            elif abs(arr[left] - median) < abs(arr[right] - median):
                result.append(arr[right])
                right -= 1
            else:  # If both have the same strength, choose the larger number
                if arr[left] > arr[right]:
                    result.append(arr[left])
                    left += 1
                else:
                    result.append(arr[right])
                    right -= 1
        
        return result

        

        