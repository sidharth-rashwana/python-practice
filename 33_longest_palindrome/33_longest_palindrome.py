import re


def longest_palindrome(s):
                                                   
    def is_palindrome(sub):
        return sub == sub[::-1]

                                                   
    palindromes = re.findall(r'(?=(\w+))', s)

                                           
    palindromes = [sub for sub in palindromes if is_palindrome(sub)]

                                 
    longest_palindrome = max(palindromes, key=len, default="")

    return longest_palindrome


               
input_string = "babad"
result = longest_palindrome(input_string)
print("Longest Palindrome:", result)
