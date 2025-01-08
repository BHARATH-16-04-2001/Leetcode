<<<<<<< HEAD
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # Negative numbers are not palindromes
            return False
        temp = x
        rev = 0
        while temp != 0:
            rem = temp % 10
            rev = (rev * 10) + rem
            temp = temp // 10
        return x == rev
=======
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # Negative numbers are not palindromes
            return False
        temp = x
        rev = 0
        while temp != 0:
            rem = temp % 10
            rev = (rev * 10) + rem
            temp = temp // 10
        return x == rev
>>>>>>> c14f8dd529800cb46ac7278bd32dbe7eb2a322ec
