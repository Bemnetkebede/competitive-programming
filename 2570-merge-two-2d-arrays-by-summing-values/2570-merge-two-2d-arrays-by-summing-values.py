class Solution(object):
    def mergeArrays(self, nums1, nums2):
        i, j = 0, 0
        output = []
        
        # Merge arrays while both have elements
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                idsum = nums1[i][1] + nums2[j][1]
                output.append([nums1[i][0], idsum])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                output.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                output.append([nums2[j][0], nums2[j][1]])
                j += 1
        
        # Add remaining elements from nums1
        while i < len(nums1):
            output.append(nums1[i])
            i += 1
        
        # Add remaining elements from nums2
        while j < len(nums2):
            output.append(nums2[j])
            j += 1
        
        return output

                

        