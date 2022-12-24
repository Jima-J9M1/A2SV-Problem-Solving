class Solution:
    def interpret(self, command: str) -> str:
        
        #store the command in hashmap
        hash_command = {"G":"G", "()":"o","(al)":"al"}
        stack_command = []
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans += hash_command[command[i]]
            elif command[i] == "(":
                stack_command.append(command[i])
            elif stack_command and command[i] == ")":
                if stack_command.pop() == "(":
                    ans += hash_command["()"]
                else:
                    ans += hash_command["(al)"]
            else:
                stack_command.append(command[i])
        
        return ans
                
        