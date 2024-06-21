class Solution:
    def simplifyPath(self, path: str) -> str:
        splited = path.split('/')
        stack = []
        for s in splited:
            if s == '..' and stack:
                stack.pop()
            elif s != '' and s != '.' and s != '..':
                stack.append(s)
                        
        answer = '/'.join(stack)
        return '/' + answer
        