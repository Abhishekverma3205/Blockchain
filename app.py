
import hashlib

data = "Hello Blockchain"

hash_value = hashlib.sha256(data.encode()).hexdigest()

print(hash_value)