class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp_dict = dict()
        for i in range(len(cpdomains)):
            cp = cpdomains[i].split(' ')
            cp[0] = int(cp[0])
            cp[1] = cp[1].split(".")
            for j in range(len(cp[1])):
                key = '.'.join(cp[1][j:])
                value = cp[0]
                if key in cp_dict:
                    cp_dict[key] += cp[0]
                else:
                    cp_dict[key ] = value 
        return [f"{value} {key}" for key, value in cp_dict.items()]
        
        