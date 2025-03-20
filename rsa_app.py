
import json
import tkinter as tk
from tkinter import messagebox
from rsa_core import RSA

class RSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Encryption App by Minh Le")
        self.root.geometry("500x700")
        
        # Tạo giao diện
        self.create_widgets()
        
        # Khởi tạo đối tượng RSA
        self.rsa = None
    
    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        # Frame cho phần tạo khóa
        key_frame = tk.LabelFrame(self.root, text="Tạo và quản lý khóa", padx=10, pady=10)
        key_frame.pack(padx=10, pady=10, fill="x")
        
        tk.Label(key_frame, text="Kích thước khóa:").grid(row=0, column=0, sticky="w")
        self.key_size_spin = tk.Spinbox(key_frame, from_=20, to=100, width=10)
        self.key_size_spin.grid(row=0, column=1, sticky="w")
        
        self.generate_key_btn = tk.Button(key_frame, text="Tạo khóa RSA", command=self.generate_keys)
        self.generate_key_btn.grid(row=0, column=2, padx=10)
        
        tk.Label(key_frame, text="Khóa công khai (e, n):").grid(row=1, column=0, sticky="w", pady=5)
        self.public_key_entry = tk.Entry(key_frame, width=50)
        self.public_key_entry.grid(row=1, column=1, columnspan=2, sticky="w")
        
        tk.Label(key_frame, text="Khóa riêng tư (d, n):").grid(row=2, column=0, sticky="w", pady=5)
        self.private_key_entry = tk.Entry(key_frame, width=50)
        self.private_key_entry.grid(row=2, column=1, columnspan=2, sticky="w")
        
        # Frame cho phần mã hóa
        encrypt_frame = tk.LabelFrame(self.root, text="Mã hóa văn bản", padx=10, pady=10)
        encrypt_frame.pack(padx=10, pady=10, fill="both")
        
        tk.Label(encrypt_frame, text="Văn bản cần mã hóa:").pack(anchor="w")
        self.input_text = tk.Text(encrypt_frame, height=5, width=50)
        self.input_text.pack(fill="both")
        self.input_text.insert("1.0", "Nhập văn bản để mã hóa...")
        
        self.encrypt_btn = tk.Button(encrypt_frame, text="Mã hóa", command=self.encrypt_text)
        self.encrypt_btn.pack(pady=5)
        
        tk.Label(encrypt_frame, text="Văn bản đã mã hóa:").pack(anchor="w")
        self.encrypted_text = tk.Text(encrypt_frame, height=5, width=50)
        self.encrypted_text.pack(fill="both")
        
        # Frame cho phần giải mã
        decrypt_frame = tk.LabelFrame(self.root, text="Giải mã văn bản", padx=10, pady=10)
        decrypt_frame.pack(padx=10, pady=10, fill="both")
        
        self.decrypt_btn = tk.Button(decrypt_frame, text="Giải mã", command=self.decrypt_text)
        self.decrypt_btn.pack(pady=5)
        
        tk.Label(decrypt_frame, text="Văn bản đã giải mã:").pack(anchor="w")
        self.decrypted_text = tk.Text(decrypt_frame, height=5, width=50)
        self.decrypted_text.pack(fill="both")
    
    def generate_keys(self):
        """Tạo cặp khóa mới"""
        try:
            k = int(self.key_size_spin.get())
            self.rsa = RSA(k=k)
            
            # Hiển thị khóa
            public_key = f"{self.rsa.e}, {self.rsa.n}"
            private_key = f"{self.rsa.d}, {self.rsa.n}"
            
            self.public_key_entry.delete(0, tk.END)
            self.public_key_entry.insert(tk.END, public_key)
            
            self.private_key_entry.delete(0, tk.END)
            self.private_key_entry.insert(tk.END, private_key)
            
            messagebox.showinfo("Thông báo", "Đã tạo khóa RSA thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo khóa: {str(e)}")
    
    def encrypt_text(self):
        """Mã hóa văn bản nhập vào"""
        try:
            # Lấy khóa công khai từ trường nhập liệu
            e, n = map(int, self.public_key_entry.get().split(","))
            
            # Lấy văn bản cần mã hóa
            plaintext = self.input_text.get("1.0", tk.END).strip()
            
            # Tạo đối tượng RSA tạm thời với khóa công khai
            temp_rsa = RSA(k=0)
            temp_rsa.e = e
            temp_rsa.n = n
            
            # Mã hóa văn bản
            encrypted = temp_rsa.encrypt(plaintext)
            
            # Hiển thị kết quả
            self.encrypted_text.delete("1.0", tk.END)
            self.encrypted_text.insert(tk.END, json.dumps(encrypted))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mã hóa: {str(e)}")
    
    def decrypt_text(self):
        """Giải mã văn bản đã mã hóa"""
        try:
            # Lấy khóa riêng tư từ trường nhập liệu
            d, n = map(int, self.private_key_entry.get().split(","))
            
            # Lấy văn bản đã mã hóa
            encrypted_text = self.encrypted_text.get("1.0", tk.END).strip()
            ciphertext = json.loads(encrypted_text)
            
            # Tạo đối tượng RSA tạm thời với khóa riêng tư
            temp_rsa = RSA(k=0)
            temp_rsa.d = d
            temp_rsa.n = n
            
            # Giải mã văn bản
            decrypted = temp_rsa.decrypt(ciphertext)
            
            # Hiển thị kết quả
            self.decrypted_text.delete("1.0", tk.END)
            self.decrypted_text.insert(tk.END, decrypted)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể giải mã: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RSAApp(root)
    root.mainloop()