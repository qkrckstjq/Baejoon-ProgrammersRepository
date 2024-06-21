class Solution:
    def simplifyPath(self, path: str) -> str:
        splited = path.split('/')
        stack = []
        for s in splited:
            if s == '.':
                continue
            elif s == '..' and stack:
                stack.pop()
            elif s != '' and s != '..':
                stack.append(s)
                        
        answer = '/'.join(stack)
        return '/' + answer
        