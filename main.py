import hashlib

def hash(text):
    hashed = hashlib.sha256(text.encode()).hexdigest()
    return hashed
