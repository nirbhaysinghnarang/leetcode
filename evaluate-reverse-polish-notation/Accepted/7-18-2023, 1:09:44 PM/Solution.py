// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token == '-':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(op_2 - op_1)

            elif token == '+':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(op_2 + op_1)
            
            elif token == '*':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(op_2 * op_1)

            elif token == '/':
                op_1 = st.pop()
                op_2 = st.pop()
                st.append(int(op_2 / op_1))
            else:
                st.append(int(token))
        print(st)
        return st[0]