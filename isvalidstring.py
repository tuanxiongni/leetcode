class Solution():
    def isvallid(self,str):
        stack=[None]
        dic={')':'(','}':'{',']':'['}
        for element in str:
            if element in dic and dic[element]==stack[len(stack)-1]:
                stack.pop()
            else:
                stack.append(element)
        return len(stack)==1