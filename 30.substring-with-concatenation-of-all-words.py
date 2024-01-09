#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#


# @lc code=start
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        
        word_len = len(words[0])
        words_count = len(words)
        total_len = word_len * words_count
        s_len = len(s)
        words_counter = Counter(words)
        res = []
        
        for i in range(word_len):
            left = i
            right = i
            curr_counter = Counter()
            
            while right + word_len <= s_len:
                w = s[right:right + word_len]
                right += word_len
                curr_counter[w] += 1
                
                while curr_counter[w] > words_counter[w]:
                    left_w = s[left:left + word_len]
                    left += word_len
                    curr_counter[left_w] -= 1
                
                if right - left == total_len:
                    res.append(left)
        
        return res

        
# @lc code=end

