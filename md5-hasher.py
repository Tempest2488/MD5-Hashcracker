import hashlib

try:
    
    input = input("Enter your word: ")
    x = bytes(input.encode('utf-8'))
    hashed = hashlib.md5(x).hexdigest()
    print(hashed)

except KeyboardInterrupt:
    print("\n\nBye bye!")
