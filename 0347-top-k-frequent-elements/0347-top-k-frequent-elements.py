class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mx = Counter(nums)
        res = []
        sorted_mx = sorted(mx.items() ,key = lambda x:x[1] , reverse= True)
        print(sorted_mx)
        for i in range(k):
            res.append(sorted_mx[i][0])
        return res