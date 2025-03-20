from rsa_utils import RSAUtils

class RSA:
    def __init__(self, k=0, p=None, q=None, e=None, d=None, n=None):
        """
        Khởi tạo đối tượng RSA
        k: kích thước khóa (bit)
        p, q: hai số nguyên tố
        e: khóa công khai
        d: khóa riêng tư
        n: modulus (p*q)
        """
        self.k = k
        
        # Nếu đã có sẵn thông số, sử dụng chúng
        if n is not None and (e is not None or d is not None):
            self.n = n
            if e is not None:
                self.e = e
            if d is not None:
                self.d = d
            return
        
        # Ngược lại, tạo khóa mới
        if k > 0:
            self.p = p if p else RSAUtils.find_biggest_prime(k)
            self.q = q if q else RSAUtils.find_biggest_prime(self.p)
            self.n = self.p * self.q
            self.phi = (self.p - 1) * (self.q - 1)
            self.e = e if e else RSAUtils.find_random_prime_together(self.phi)
            self.d = d if d else self._find_d()
            print(f"p = {self.p}, q = {self.q}, n = {self.n}, phi = {self.phi}, e = {self.e}, d = {self.d}")

    def _find_d(self):
        """Tìm d theo công thức e*d = 1 mod phi"""
        for i in range(1, self.phi):
            if (i * self.e) % self.phi == 1 and i != self.e:
                return i
        return None

    def encrypt(self, plaintext):
        """Mã hóa văn bản"""
        encrypted = []
        for char in plaintext:
            m = ord(char) # gán cho một ký tự theo sơ đồ mã hóa Unicode
            c = RSAUtils.mod_pow(m, self.e, self.n)
            encrypted.append(c)
        return encrypted

    def decrypt(self, ciphertext):
        """Giải mã ciphertext"""
        decrypted = ""
        for c in ciphertext:
            m = RSAUtils.mod_pow(c, self.d, self.n)
            decrypted += chr(m)
        return decrypted

    def get_public_key(self):
        """Trả về khóa công khai (e, n)"""
        return (self.e, self.n)
    
    def get_private_key(self):
        """Trả về khóa riêng tư (d, n)"""
        return (self.d, self.n)