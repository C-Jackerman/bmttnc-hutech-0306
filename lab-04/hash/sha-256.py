import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8')) #chuyen doi du lieu thanh bytes va cap nhat vao doi tuong hash
    return sha256_hash.hexdigest() #tra ve bieu dien hex chuoi hash

data_to_hash = input("Nhap du lieu de hash bang SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print("Gia tri hash SHA-256: ", hash_value)                    