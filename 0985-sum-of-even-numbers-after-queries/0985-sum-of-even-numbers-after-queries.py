class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
            even_sum = sum(num for num in nums if num % 2 == 0)  # Initial sum of even numbers
            res = []

            for val, index in queries:
                old_value = nums[index]
                
                if old_value % 2 == 0:
                    even_sum -= old_value

                
                nums[index] += val
              
                
                if nums[index] % 2 == 0:
                    even_sum += nums[index]

                res.append(even_sum)
            return res

        
            

                




            
            
            
            
            
            
            
            
            


                
                
                


            
            