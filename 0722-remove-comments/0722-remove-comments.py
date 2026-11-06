class Solution(object):
    def removeComments(self, source):
      res = []
      st = ''
      flag = False
      for word in source:
        i = 0
        while i < len(word):
            if not flag and word[i:i+2] == "/*":
                flag = True
                i += 1
            elif flag and word[i:i+2] == "*/":
                flag = False
                i += 1
            elif not flag and word[i:i+2] == "//":
                break
            elif not flag:
                st += word[i]
            i+= 1
        if st and not flag:
                res.append(st)
                st = ""       
      return res