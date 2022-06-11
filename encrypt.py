import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Public (shared) Key Read
def read_public (filename = "public_shared.pem"):
    with open("public_shared.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

# Encrypt and Save to file
#data = [b'My secret weight', b'My secret id']
data = ['Hello World'.encode()] # your data
public_key = read_public()
open('test.txt', "wb").close() # clear file
for encode in data:
    encrypted = public_key.encrypt(
        encode,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    with open('test.txt', "ab") as f: f.write(encrypted)