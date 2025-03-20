import random
from math import gcd

class RSAUtils:
    @staticmethod
    def is_prime(x):
        """Kiểm tra số nguyên tố"""
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    @staticmethod
    def find_biggest_prime(n):
        """Tìm số nguyên tố lớn nhất nhỏ hơn n"""
        for i in range(n - 1, 1, -1):
            if RSAUtils.is_prime(i):
                return i
        return 0

    @staticmethod
    def prime_factors(n):
        """Tìm các thừa số nguyên tố của n"""
        factors = []
        i = 2
        while i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1
        return factors

    @staticmethod
    def find_random_prime_together(a):
        """Tìm số nguyên tố cùng nhau với a"""
        prime_together = [i for i in range(2, a) if gcd(i, a) == 1]
        if len(prime_together) > 0:
            return random.choice(prime_together)
        return None

    @staticmethod
    def mod_pow(base, exponent, modulus):
        """Tính lũy thừa theo modulo hiệu quả"""
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent >> 1
            base = (base * base) % modulus
        return result