import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BS = AES.block_size

def encrypt(key, plain):
        iv = Random.new().read(BS)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(plain)
        
def decrypt(key, enc):
        iv = enc[:BS]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.decrypt(enc[BS:])
       
# hash algoritm 이용해 키 생성
key = hashlib.sha256(Random.new().read(32)).digest()

message="nice to meet you"
print(message)
    
#encrypt
enc=encrypt(key, message)
print(enc)

#decrypt
dec=decrypt(key, enc)
print(dec)
