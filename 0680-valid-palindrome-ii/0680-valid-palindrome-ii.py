class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s)-1
        if s == s[::-1]:
            return True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                str_l = s[:l] + s[l+1:]
                str_r = s[:r] + s[r+1:] 
                if str_l == str_l[::-1]:
                    return True
                elif str_r == str_r[::-1]:
                    return True
                break
        return False  


                   



        # my_dict = Counter(s)
        # count = 0
        # for k , v in my_dict.items():
        #     if v == 1:
        #       count += 1 
        # print(count)
        # if count > 2:
        #     return False
        # else:
        #     return True

    
           
            

        