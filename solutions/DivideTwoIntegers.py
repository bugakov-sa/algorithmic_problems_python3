class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        dividend_sign = dividend >= 0
        dividend = abs(dividend)
        divisor_sign = divisor >= 0
        divisor = abs(divisor)

        res = 0
        while dividend >= divisor:
            diff = dividend - divisor
            subtrahend = divisor
            i = 1
            while subtrahend + subtrahend < diff:
                subtrahend += subtrahend
                i += i
            res += i
            dividend -= subtrahend

        if not dividend_sign:
            res = -res
        if not divisor_sign:
            res = -res

        if res >= 2147483647:
            res = 2147483647

        return res

print(Solution().divide(7, -3))