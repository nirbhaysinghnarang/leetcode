class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ret = ""
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                toRep = ''
                while stack and stack[-1]!='[':
                   toRep = stack.pop() + toRep
                
                cnt = ''
                stack.pop()
                while stack and stack[-1].isnumeric():
                    cnt = stack.pop() + cnt

                stack.append(toRep*(int(cnt)))
        return ''.join(stack)
                

