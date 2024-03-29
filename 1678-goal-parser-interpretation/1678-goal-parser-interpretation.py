class Solution:
    def interpret(self, command: str) -> str:
        
        #store the command in hashmap
        stack_command = []
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans += "G"
            elif command[i] == "(":
                stack_command.append(command[i])
            elif stack_command and command[i] == ")":
                if stack_command.pop() == "(":
                    ans += "o"
                else:
                    ans += "al"
            else:
                stack_command.append(command[i])
        
        return ans
                
        