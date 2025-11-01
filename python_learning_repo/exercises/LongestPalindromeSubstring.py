#最长的回文字串问题
#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

def longest_palindrome(s):
    if not s:
        return ""
    start = 0
    max_len = 1
    def expand_around_center(left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left -1

    for i in range(len(s)):
        len1 = expand_around_center(i,i)# Odd length palindromes
        len2 = expand_around_center(i,i+1)# Even length palindromes
        current_len = max(len1, len2)
        if current_len > max_len:
            max_len = current_len
            start = i - (current_len -1)//2
    return s[start:start + max_len]

input_str = input()
print(longest_palindrome(input_str))