import hashlib
print("made by Talen Serrao")

def menu():
    print("Select your input:")
    print("1. ")



md5=input("Enter the Hash: ")

passwordlist= bytes(open("passwordlist.txt").read(), encoding='utf8')
for i in passwordlist.split():
    check=hashlib.md5(i).hexdigest()
    
    if check == md5:
        print("The password is cracked ,The password is", '"', i.decode()), '"'
        
        quit()
        
    
    elif check != md5:
        pass
print("The password could not be cracked")

    


