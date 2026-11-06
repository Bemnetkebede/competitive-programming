class Solution(object):
    def interpret(self, command):
        result = ''
        for i in range(len(command)):
            if command[i:i+2] == "()":
                result += "o"
            elif command[i:i+4]== "(al)":
                result += "al"
            elif command[i] == "G":
                result += "G"
        return result
              
            

        # return command.replace("()","o").replace("(al)", "al")


        

        

        
        
        