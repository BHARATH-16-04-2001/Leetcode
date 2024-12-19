<<<<<<< HEAD
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # To track numbers we've already seen

        while n != 1 and n not in visited:
            visited.add(n)
            hap = 0

            # Calculate the sum of squares of digits
            while n != 0:
                rem = n % 10
                hap += rem ** 2
                n = n // 10

            n = hap

        return n == 1  # Return True if n becomes 1
=======
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # To track numbers we've already seen

        while n != 1 and n not in visited:
            visited.add(n)
            hap = 0

            # Calculate the sum of squares of digits
            while n != 0:
                rem = n % 10
                hap += rem ** 2
                n = n // 10

            n = hap

        return n == 1  # Return True if n becomes 1
>>>>>>> c14f8dd529800cb46ac7278bd32dbe7eb2a322ec
