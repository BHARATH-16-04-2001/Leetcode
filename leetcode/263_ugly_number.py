<<<<<<< HEAD
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        l = [2,3,5]
        for i in l:
            while n % i == 0:
                n = n // i
                
=======
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        l = [2,3,5]
        for i in l:
            while n % i == 0:
                n = n // i
>>>>>>> c14f8dd529800cb46ac7278bd32dbe7eb2a322ec
        return n == 1
