class Solution(object):
    def frequencySort(self, s):
       x =  Counter(s)
       lst = list(s)
       lst.sort(key= lambda char:(x[char], char) ,reverse = True)
       return ''.join(lst)

        
            
           
           
            

       
       
            
          