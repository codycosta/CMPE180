'''
Author:     Cody Costa
Date:       5/13/2025

'''

sample_text = 'Racecar'
sample_two = 'Cody Costa'

def is_palindrome(text: str) -> bool:
    for idx, char in enumerate(reversed(text.lower())):
        if char != text.lower()[idx]:
            return False
    
    return True

print(is_palindrome(sample_text))   # true
print(is_palindrome(sample_two))    # false
