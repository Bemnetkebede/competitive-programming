class Solution(object):
    def countCharacters(self, words, chars):
        count = 0
        cn =    Counter(chars)
        for i in range(len(words)):
            c = 0
            cnt = Counter(words[i])
            for j in range(len(words[i])):
                
                if cnt[words[i][j]] <= cn[words[i][j]]:
                    if words[i][j] not in chars:
                        break
                    else:
                        c += 1
            if len(words[i]) == c:
               count += len(words[i])
        return count

                

        
        