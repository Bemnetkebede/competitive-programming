class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        same = dict()
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                same[list1[i]] = j + i
        mn = min(same.values())
        for k , v in same.items():
            if v == mn:
                res.append(k)
        return res


        
        # res = []
        # d = dict()
        # d2 = dict()
        # for i in range(len(list1)):
        #     d[list1[i]] = i 
        # for j in range(len(list2)):
        #     d2[list2[j]] = j 
        # res = dict()
        # for k , v in d.items():
        #     if k in d2:
        #         res[k] = v + d2[k]
        # mn = min(res.values())
        # rs = []
        # for key , value in res.items():
        #     print(res.items())
        #     if value == mn:
        #         rs.append(key)
        # return rs
                

    

               
            

        

         