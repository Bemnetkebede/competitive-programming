class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
            res = []
            c = Counter(nums)
            print(c)
            for k , v in c.items():
                if v == 2:
                    res.append(k)
            return res
            

            # duplicates = []
            # i = 0
            # while i < len(nums):
            #     correct = nums[i] - 1
            #     if 0 <= correct < len(nums) and nums[i] != nums[correct]:
            #         nums[i], nums[correct] = nums[correct], nums[i]
            #     else:
            #         i += 1
            
            # # Find duplicates after sorting
            # for i in range(len(nums)):
            #     if nums[i] != i + 1:
            #         duplicates.append(nums[i])
            # return duplicates