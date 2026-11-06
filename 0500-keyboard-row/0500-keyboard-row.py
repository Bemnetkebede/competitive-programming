class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        my_dict = {
            "first" : "qwertyuiop",
            "second" : "asdfghjkl",
            "third" : "zxcvbnm"
        }
        res = []
        for i in range(len(words)):
            temp = words[i].lower()
            print(set(temp))
            if set(temp) <= set(my_dict["second"]) :
               res.append(words[i])
            elif set(temp) <= set(my_dict["first"]):
                res.append(words[i])
            elif set(temp) <= set(my_dict["third"]):
                res.append(words[i])
        return res
            