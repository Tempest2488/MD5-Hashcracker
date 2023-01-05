import hashlib
import csv
import datetime
import time

def sleep(): 
    time.sleep(3)

def menu(): # Here is the menu to choose user input or file input
    print("Choose an option: ")
    print("1. File")
    print("2. Direct\n")
    choice = int(input("Enter your choice: "))

    if choice == 1: # Using file input
        def cracking():
            passwordlist = bytes(open("passwordlist.txt").read(), 'utf-8')
            return passwordlist


        passwordlist = cracking()
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print("Time started:", time, '\n')
        with open("md5_hashes.csv", "r") as read_obj:
            file = csv.reader(read_obj)
            for i in file: # A loop is made to read the hashes which is provided in the given csv file
                for check in passwordlist.split(): # A loop is created so that it can read the passwords from a given wordlist
                    hash = hashlib.md5(check).hexdigest() # This line is used to come if the hashes matches
                    if hash == i[0]: # If the output matches 
                        time_finish = datetime.datetime.now().strftime('%H:%M:%S')
                        print("the password is ", check.decode('utf-8'))
                        print("Time finished:", time_finish, '\n')
                        sleep()
                        
                        pass

                    elif hash != i[0]: # If the output doesn't matches
                        pass
    elif choice == 2:
        # Using user input method

        md5 = input("Enter the Hash: ") # input the hashes

        passwordlist= bytes(open("passwordlist.txt").read(), encoding='utf8')
        for i in passwordlist.split(): # A loop is made to read the hashes which is provided by the wordlist
            check=hashlib.md5(i).hexdigest() 

            if check == md5: # If the output matches 
                print("The password is cracked ,The password is", '"' + i.decode() + '"')
                
                quit()
                

            elif check != md5: # If the output doen't matches
                pass
        print("The password could not be cracked")



menu()