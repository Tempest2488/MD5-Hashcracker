import csv
import hashlib

def cracking():
    passwordlist = bytes(open("passwordlist.txt").read(),'utf-8')
    return passwordlist

passwordlist = cracking()

with    open("md5_hashes.csv","r") as read_obj:
    file = csv.reader(read_obj)
    for i in file:
        for check in passwordlist.split():
            hash = hashlib.md5(check).hexdigest()

            if hash == i[0]:
                print("the password is ",check.decode('utf-8'))

                pass

            elif hash != i[0]:
                pass
