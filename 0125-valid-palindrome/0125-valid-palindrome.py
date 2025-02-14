class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c.isalnum():
                stack.append(c.lower())

        print(stack)
        
        for c in s:
            if c.isalnum():
                if c.lower() != stack.pop():
                    return False
        
        return True