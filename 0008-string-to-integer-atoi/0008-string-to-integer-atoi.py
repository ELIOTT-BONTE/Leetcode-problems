class Solution:
    def myAtoi(self, s: str) -> int:
        digits = 0
        sign = 1
        res = 0
        i, n = 0, len(s)
        MAX_INT, MIN_INT = 2**31 -1 , -2**31

        # trim leading whitespace
        while i<n and s[i] == " ":
            i += 1


            



        # check sign
        if i<n and s[i] in ["+", "-"]:
            sign = -1 if s[i] =="-" else 1
            i += 1


        # extract digits
        while i<n and s[i].isdigit():
            digit = int(s[i])

            # handle overflow
            if res * 10 + digit > MAX_INT:
                return MAX_INT if sign == 1 else MIN_INT
            res = res * 10 + digit
            i += 1


        
        

        # return result
        return sign * res