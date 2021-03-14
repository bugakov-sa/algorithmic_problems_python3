class Solution:

    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(s: str) -> str:
            if len(s) < 2:
                return True
            left_i = 0
            right_i = len(s) - 1
            while right_i > left_i:
                if s[left_i] != s[right_i]:
                    return False
                else:
                    left_i += 1
                    right_i -= 1
            return True

        def getPalindrome(s: str, palindrome_len: int):
            for start_i in range(0, len(s) - palindrome_len + 1):
                test_str = s[start_i:start_i + palindrome_len]
                if isPalindrome(test_str):
                    return test_str
            return ''

        def getLongestPalindrom(s: str, lens) -> str:
            if len(lens) == 1:
                return getPalindrome(s, lens[0])
            center_i = len(lens) // 2
            p = getPalindrome(s, lens[center_i])
            if p != '':
                lens = lens[center_i + 1:]
            else:
                lens = lens[0:center_i]
            if len(lens) == 0:
                return p
            p2 = getLongestPalindrom(s, lens)
            if p2 != '':
                return p2
            else:
                return p

        if len(s) < 2:
            return s

        longest_odd_p = getLongestPalindrom(s, list(range(1, len(s) + 1, 2)))
        odd_len = len(longest_odd_p)

        longest_even_p = getLongestPalindrom(s, list(range(odd_len - 1, len(s) + 1, 2)))
        even_len = len(longest_even_p)

        if odd_len > even_len:
            return longest_odd_p
        else:
            return longest_even_p

print(Solution().longestPalindrome("babad"))