# RSA_algorithmn_Fintech_UEH
Diễn giải mã hóa RSA bằng code và giải thích giải thuật cho ae
# **Thuật toán RSA**

Trong mật mã học, `RSA` là một thuật toán mật mã hóa khóa công khai. Đây là thuật toán đầu tiên phù hợp với việc tạo ra chữ ký điện tử đồng thời với việc mã hóa. Nó đánh dấu một sự tiến bộ vượt bậc của lĩnh vực mật mã học trong việc sử dụng khóa công cộng. RSA đang được sử dụng phổ biến trong thương mại điện tử và được cho là đảm bảo an toàn với điều kiện độ dài khóa đủ lớn.

## **1. Chuyển văn bản thành bản mã bằng ASCII**

## **2. Các bước trong quá trình sinh khóa**

1. Chọn 2 số nguyên tố lớn p và q, lựa chọn ngẫu nhiên và độc lập.
2. Tính: n = p.q
3. Tính hàm phi Euler: phi(n) = phi(q).phi(p).
4. Chọn 1 số e sao cho 1 < e < phi(n) và gcd(e, phi(n)) = 1
5. Tính d: d.e = 1 (mod phi(n))

## **3. Mã hóa**

Giả sử thông điệp cần mã hóa là một số nguyên m sao cho m < n. Để mã hóa, ta thực hiện:

`c = m^e mod n`

## **4. Giải mã**

Để giải mã bản mã c, người nhận sử dụng khóa bí mật d theo công thức:

`m = c^d mod n`

## ***Hàm `mod_pow()`***

Hàm `mod_pow` trong thuật toán RSA là một phần quan trọng giúp tính toán hiệu quả biểu thức dạng `base^exponent mod modulus`. Đây là yếu tố then chốt trong cả quá trình `mã hóa và giải mã` RSA.

### **Tại sao cần `mod_pow`?**

Trong RSA, chúng ta phải tính các biểu thức:

- **Mã hóa:** `c = m^e mod n`
- **Giải mã:** `m = c^d mod n`

Vấn đề ở đây là các số mũ `e` và `d` thường rất lớn, dẫn đến:

- Nếu tính trực tiếp `m^e` hoặc `c^d`, kết quả sẽ là một số khổng lồ vượt quá khả năng lưu trữ của máy tính.
- Việc tính toán trực tiếp sẽ rất chậm và không hiệu quả.

---

### **Cách `mod_pow` hoạt động**
Hàm `mod_pow` sử dụng thuật toán **"Bình phương và nhân"** (*Square and Multiply*) để tính lũy thừa modulo hiệu quả. Đây là cách tiếp cận giúp giảm độ lớn của các phép tính, đặc biệt khi `base^exponent` (ví dụ `m^e`) có thể rất lớn.

### **Nguyên lý hoạt động**

1. **Chuyển đổi số mũ sang nhị phân**  
    Số mũ `exponent` được chuyển từ dạng thập phân sang nhị phân.  
    Ví dụ:  
    `exponent = 13 (thập phân) = 1101 (nhị phân)`  
    Tương ứng:  
    `13 = 1×2^3 + 1×2^2 + 0×2^1 + 1×2^0`

2. **Phân rã lũy thừa**  
    Từ biểu diễn nhị phân, ta có:  
    `base^13 = base^(1×2^3 + 1×2^2 + 0×2^1 + 1×2^0)`  
    Tương đương:  
    `base^13 = base^(2^3) × base^(2^2) × base^(2^0)`

3. **Tính toán modulo từng bước**  
    Sử dụng tính chất nhân đồng dư:  
    `(a × b) mod p = [(a mod p) × (b mod p)] mod p`  
    Ví dụ với `base = 3` và `modulus = 7`:  
    `3^13 mod 7 = [(3^(2^3) mod 7) × (3^(2^2) mod 7) × (3^(2^0) mod 7)] mod 7`

### **Lợi ích**
- Giảm số phép toán từ O(n) xuống O(log n).
- Tránh việc xử lý các số quá lớn, đảm bảo hiệu quả và chính xác.


### **Code**
```python 
def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2  # Lấy exponent chia 2 lấy phần nguyên dư, giống như cách chuyển từ số thập phân sang nhị phân
        base = (base * base) % modulus # Bình phương base lấy dư 
    return result
```

Giải thích chi tiết thuật toán:

Khởi tạo result = 1
Đưa base về dạng đồng dư trong modulo (base % modulus)
Với mỗi bit trong biểu diễn nhị phân của số mũ:

Nếu bit là 1 (exponent % 2 == 1), nhân result với base và lấy modulo
Bình phương base và lấy modulo
Dịch bit exponent sang phải (chia 2)


Kết quả cuối cùng là result
