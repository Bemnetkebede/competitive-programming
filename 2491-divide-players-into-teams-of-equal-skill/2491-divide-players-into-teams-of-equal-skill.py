class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        skill.sort()
        l = 0
        r = len(skill) - 1
        skill_val = skill[l] + skill[r]
        print(skill_val)
        while l < r:
            if skill[l] + skill[r] != skill_val:
                return -1
            else:
                res += skill[l] * skill[r]
                l += 1
                r -= 1
        return res 
