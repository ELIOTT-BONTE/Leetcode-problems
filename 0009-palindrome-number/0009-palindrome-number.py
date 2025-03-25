class Solution:
    def isPalindrome(self, x: int) -> bool:
        #convert to str
        #left, right pointer on the string

        temp = str(x)
        l, r = 0, len(temp)-1

        while l<=r:
            if temp[l] != temp[r]:
                return False
            l+=1
            r-=1
        return True