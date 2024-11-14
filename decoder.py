from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

key = bytes.fromhex(input("请输入密钥 (key) 的16进制字符串: "))
iv = bytes.fromhex(input("请输入初始化向量 (IV) 的16进制字符串: "))
encrypted_text = bytes.fromhex(input("请输入加密后的内容的16进制字符串: "))

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_padded_text = decryptor.update(encrypted_text) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted_text = unpadder.update(decrypted_padded_text) + unpadder.finalize()

print("解密后的内容:", decrypted_text.decode())