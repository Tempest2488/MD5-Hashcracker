import hashlib

hashvalue = input("Enter a string: ")
hashobj1= hashlib.md5()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())