class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        cntr_set = []
        max_res = 0
        for i in range(len(fruits)):
            if fruits[i] not in cntr_set and len(cntr_set) < 2:
                cntr_set.append(fruits[i])
            elif fruits[i] not in cntr_set and len(cntr_set) >= 2:
                old = fruits[i - 1]
                l = i - 1
                while l > 0 and fruits[l] == old:
                    l -= 1
                l += 1
                cntr_set = [old, fruits[i]]
            max_res = max(max_res , i - l + 1)
        return max_res



              
