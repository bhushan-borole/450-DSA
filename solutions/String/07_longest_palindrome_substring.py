def longestPalindrome(s):
    if not s or len(s) < 1:
        return ''
    
    start, end = 0, 0
    
    for i in range(len(s)):
        len1 = helper(s, i, i) # even palindrome
        len2 = helper(s, i, i+1) # odd palindrome
        max_len = max(len1, len2) # getting which palindrome is longest
        if max_len > end - start:
            # determing the start and end index of the string
            # based on length and i
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
        
    return s[start: end + 1]

def helper(s, left, right):
    while(left >= 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    
    return right - left - 1
