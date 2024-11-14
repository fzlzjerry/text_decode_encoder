from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

text = input("请输入你想要加密的内容: ")

key = os.urandom(16)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
padder = padding.PKCS7(128).padder()
padded_text = padder.update(text.encode()) + padder.finalize()
encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
print("密钥 (key):", key.hex())
print("初始化向量 (IV):", iv.hex())
print("加密后的内容:", encrypted_text.hex())