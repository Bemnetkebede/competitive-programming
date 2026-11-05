class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        result = []
        for word in words:
            shortest = word  
            for root in dictionary:
                if word.startswith(root) and len(root) < len(shortest):
                    shortest = root
            result.append(shortest)
        return ' '.join(result)

            
            
        