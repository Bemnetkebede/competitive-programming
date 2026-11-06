class Solution(object):
    def printVertically(self, s):
        words = s.split(' ')
        max_len = max(len(word) for word in words)
        result = []
        for i in range(max_len):  
            vertical_word = "".join(words[j][i] if i < len(words[j]) else " " for j in range(len(words)))
            result.append(vertical_word.rstrip())  

        return result
       
        
        
        

            
            


        