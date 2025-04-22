class Solution:
    def intToRoman(self, num: int) -> str:
        # if you can, remove 1000, add "M" to result each time
        # if you can, remove 900, add "CM" each time
        # same for rest of numbers

        # roman to values, in descending order
        values = [("M",1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

        res = ""

        for R, V in values: #Roman, Value
            while num >= V:
                num -= V
                res += R
        return res