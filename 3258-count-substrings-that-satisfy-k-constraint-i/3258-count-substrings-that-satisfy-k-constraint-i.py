class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        c_o, c_z, c_s = 0, 0, 0
        l, r = 0, 0

        while l < len(s):
            # print(l,r)
            if s[r] == '0':
                c_z += 1
            else:
                c_o += 1
            if c_o > k and c_z > k:
                # print(l, r, c_z, c_o, 'in')

                l += 1
                r = l
                c_o = 0
                c_z = 0

            else:
                c_s += 1
                # print(l, r, 'l', 'r')
                r += 1
                
                if r == len(s):
                    l += 1
                    r = l
                    c_o = 0
                    c_z = 0
                    

        return c_s

        