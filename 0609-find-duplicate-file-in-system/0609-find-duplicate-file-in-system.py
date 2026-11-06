class Solution(object):
    def findDuplicate(self, paths):
        file_path = dict()
        for path in paths:
           path = path.split()
           for i in range(1 , len(path)):
               s = path[i].index('(')
               e = path[i].index(')')
               key = path[i][s+1:e]
               value= path[0] + '/' + path[i][:path[i].index('(')]
               if key in file_path:
                  file_path[key].append(value)
               else:
                  file_path[key] = [value]
        fn = []
        for i in file_path.values():
            if len(i) > 1:
               fn.append(i)
        return fn
              
              
        