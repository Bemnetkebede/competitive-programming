class Solution(object):
    def maskPII(self, s):
            if '@' in s:
                s = s.lower()
                idx = s.index('@')
                return s[0] + (5 * '*') + s[idx-1:]
            else:
                st = ''
                for i in s:
                    if i.isdigit():
                        st += i
                l = len(st)
                if l % 10 == 0:
                    return '***-***-' + st[-4:] 
                elif l % 10 == 1:
                    return '+*-***-***-' + st[-4:]
                elif l % 10 == 2:
                    return '+**-***-***-' + st[-4:]
                else:
                    return '+***-***-***-' + st[-4:]
                    
                
            

                   
        
        