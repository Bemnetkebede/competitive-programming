class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        de = deque()
        for card in reversed(deck):
            if de:
                de.appendleft(de.pop()) 
            de.appendleft(card)
        return list(de)




        # deck.sort()
        # even = []
        # odd = []
        # for i in range(len(deck)):
        #     if i % 2 == 0:
        #         even.append(deck[i])
        #     else:
        #         odd.append(deck[i])
        # even.sort()
        # odd.sort()
        # result = []
        # z = zip(even,odd)
        # print(z)
        # for x, y in z:
        #     result.extend([x, y])
        # result.extend(even[len(odd):])  
        # result.extend(odd[len(even):])
        # return result
       
           
        
        
        
        