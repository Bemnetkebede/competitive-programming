class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        my_dict = Counter(answers)
        total = 0
        for val , freq in my_dict.items():
            group = val + 1
            num_groups = math.ceil(freq / group)
            total += num_groups * group
        return total





        


        