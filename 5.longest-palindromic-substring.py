#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Go for each ubstring letter and check if is palindromic?
        # That would take n^2
        # But if we lts say a windows strategy? ad check the front and end?
        # Then go along until you find the substring that matches the palindrome?
        # That would be n^2 and then because you have to find . to palindromic you have to find also going for each word and you can expand outward.
        maxlen = 0
        maxstr = ""
        if len(s) <= 1:
            return s

        for i in range(1, len(s)):
            # Get to the letter and the left and then try to push right. Then both at the same time.
            l = i
            r = i

            # Find and expand the base
            while(l>0 and s[l - 1] == s[l]):
                l -= 1
            while(r < len(s)-1 and s[r + 1] == s[r]):
                r += 1
            
            while( l > 0 and r < len(s) - 1 and s[l-1] == s[r+1] ):
                l-=1
                r+=1

            if maxlen < (r-l+1):
                maxlen = r-l+1
                maxstr = s[l:(r+1)]
        return maxstr



        
# @lc code=end

