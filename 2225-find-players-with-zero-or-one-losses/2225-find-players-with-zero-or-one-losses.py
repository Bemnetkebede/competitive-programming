class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = []
        lost_dict = {}
        for i in matches:
            for j in i:
                winners.add(i[0])
                losers.append(i[1])
                break
                
                
        for num in losers:
            if num in lost_dict.keys():
               lost_dict[num] += 1
            else:
                lost_dict[num] = 1
        ans_2 = []
        for k , v in lost_dict.items():
            if v == 1:
                ans_2.append(k)
        ans_2.sort()
        
    
        ans_1 = []
        for win in winners:
            if win not in lost_dict:
                ans_1.append(win)
        ans_1.sort()
        return [ans_1,ans_2]
        







        