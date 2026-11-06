class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dict_tuple = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                dict_tuple[nums[i] * nums[j]] += 1
        tuples = 0
        for v in dict_tuple.values():
            if v > 1:
                tuples += (v * (v - 1) // 2) * 8
        return tuples 
        

