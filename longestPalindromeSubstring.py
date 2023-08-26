s = "cbbd"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = "q"
        for startingLetter in range(0,len(s)):
            for nextLetter in range(startingLetter+1,len(s)):
                if s[startingLetter:nextLetter+1]==s[startingLetter:nextLetter+1][::-1]:
                    if len(longest) <= len(s[startingLetter:nextLetter+1]):
                        longest = s[startingLetter:nextLetter+1]
        if longest == "q":
            return (s[0])
        return (longest)