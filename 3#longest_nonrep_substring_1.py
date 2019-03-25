class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        cur  = 0
        max_length = 1
        left = right = 0
        unique_chars = {}
        unique_chars[s[left]] = left
        for i in range(1,len(s)):
            if s[i] not in unique_chars.keys() and i == cur + 1:
                max_length += 1
                right += 1
                cur += 1
                unique_chars[s[i]] = i
            elif s[i] not in unique_chars.keys() and i != cur+1:
                right += 1
                if right - left + 1 >= max_length:
                    max_length = right - left +1
                    cur = right
                unique_chars[s[i]] = i
            else:
                temp = unique_chars[s[i]]+1
                for j in range(left,temp):
                    unique_chars.pop(s[j])
                left = temp
                right = i
                if right - left + 1 >= max_length:
                    max_length = right -left +1
                unique_chars[s[i]] = right
                
        return max_length