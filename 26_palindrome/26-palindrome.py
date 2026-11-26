class Solution:
    def isPalindrome(self, s: str):
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


s1 = Solution()
print(s1.isPalindrome("A man, a plan, a canal: Panama"))
print(s1.isPalindrome("0P"))

          
def is_panagram(s: str):
    c = [ch.lower() for ch in s if ch.isalpha()]
    converted_str = "".join(c)
    if converted_str == converted_str[::-1]:
        return "palindrome"
    return "not a palindrome"

s = "A man, a plan, a canal: Panama"
print(is_panagram(s))